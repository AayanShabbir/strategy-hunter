"""Signed inter-agent bundles (blueprint Table 2: "Absolute (Strict Boolean Thresholding with Signed Signatures)").

Each role (miner, worker, auditor) owns an Ed25519 key pair. A bundle is signed over its canonical JSON (sorted keys, no whitespace):
  miner   -> worker   : the task payload (expression, ast, ast_hash, dsl, source, agent)         verified by the Worker before it evaluates
  worker  -> auditor  : {trial_id, ast_hash, sha256 of the metrics + net/gross/turnover/cost vectors}   verified by the Auditor
  auditor -> trader   : {trial_id, ast_hash, verdict, failed gates, N at audit, sha256 of the gates}      verified by the Trader
A signature carries the role and a key id (fingerprint of the public key); `verify` also checks the role is the one the stage expects,
so a bundle signed by the wrong agent is refused. Keys live in `data/swarm/keys/<role>.key` (0600, created on first use, never
committed). Honest scope: all roles run as the same OS user on one box, so this is integrity + provenance protection against a
corrupted or hand-edited database and against role confusion - it is not a defence against someone who can read the key files.
"""
from __future__ import annotations

import base64
import hashlib
import json
import os
from typing import Any, Optional

import numpy as np
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey

from . import DATA_DIR

ROLES = ("miner", "worker", "auditor")
DEFAULT_KEY_DIR = os.path.join(DATA_DIR, "keys")


def canonical_bytes(payload: Any) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), default=float, allow_nan=True).encode()


def digest(payload: Any) -> str:
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()


def vectors_digest(*arrays: Optional[np.ndarray]) -> str:
    h = hashlib.sha256()
    for a in arrays:
        h.update(b"-" if a is None else np.ascontiguousarray(a, dtype="<f8").tobytes())
    return h.hexdigest()


class KeyStore:
    def __init__(self, directory: Optional[str] = None):
        self.dir = str(directory or DEFAULT_KEY_DIR)
        self._priv: dict[str, Ed25519PrivateKey] = {}

    def _path(self, role: str) -> str:
        return os.path.join(self.dir, f"{role}.key")

    def _private(self, role: str, create: bool = True) -> Ed25519PrivateKey:
        if role not in ROLES:
            raise ValueError(f"unknown role {role!r}")
        if role in self._priv:
            return self._priv[role]
        p = self._path(role)
        if not os.path.exists(p):
            if not create:
                raise FileNotFoundError(p)
            os.makedirs(self.dir, mode=0o700, exist_ok=True)
            key = Ed25519PrivateKey.generate()
            raw = key.private_bytes(serialization.Encoding.Raw, serialization.PrivateFormat.Raw, serialization.NoEncryption())
            fd = os.open(p, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)       # O_EXCL: two processes cannot both create it
            try:
                os.write(fd, base64.b64encode(raw))
            except Exception:
                os.close(fd)
                raise
            os.close(fd)
        with open(p, "rb") as f:
            self._priv[role] = Ed25519PrivateKey.from_private_bytes(base64.b64decode(f.read().strip()))
        return self._priv[role]

    def public_bytes(self, role: str) -> bytes:
        return self._private(role).public_key().public_bytes(serialization.Encoding.Raw, serialization.PublicFormat.Raw)

    def key_id(self, role: str) -> str:
        return hashlib.sha256(self.public_bytes(role)).hexdigest()[:16]

    def sign(self, role: str, payload: Any) -> dict:
        sig = self._private(role).sign(canonical_bytes(payload))
        return {"role": role, "kid": self.key_id(role), "alg": "ed25519", "sig": base64.b64encode(sig).decode()}

    def verify(self, payload: Any, signature: Optional[dict], expected_role: str) -> tuple[bool, str]:
        if not isinstance(signature, dict):
            return False, "missing signature"
        if signature.get("role") != expected_role:
            return False, f"signed by role {signature.get('role')!r}, expected {expected_role!r}"
        try:
            pub = Ed25519PublicKey.from_public_bytes(self.public_bytes(expected_role))
            if signature.get("kid") != self.key_id(expected_role):
                return False, "unknown key id"
            pub.verify(base64.b64decode(signature["sig"]), canonical_bytes(payload))
            return True, "ok"
        except Exception as e:                      # InvalidSignature, bad base64, missing key ...
            return False, f"bad signature ({type(e).__name__})"


# ---- the three signed payloads (single source of truth for both signer and verifier)
def task_payload(task: dict) -> dict:
    return {k: task.get(k) for k in ("protocol", "expression", "ast_hash", "ast", "dsl", "source", "agent_id")}


def result_payload(trial_id: int, ast_hash: str, worker: str, metrics: dict, net, gross, turnover, cost) -> dict:
    return {"trial_id": int(trial_id), "ast_hash": ast_hash, "worker": worker, "metrics_sha256": digest(metrics),
            "vectors_sha256": vectors_digest(net, gross, turnover, cost)}


def audit_payload(trial_id: int, ast_hash: str, bundle: dict) -> dict:
    return {"trial_id": int(trial_id), "ast_hash": ast_hash, "overall_status": bundle["overall_status"], "failed_gates": bundle["failed_gates"],
            "n_trials_at_audit": bundle["n_trials_at_audit"], "gates_sha256": digest(bundle["gates"])}
