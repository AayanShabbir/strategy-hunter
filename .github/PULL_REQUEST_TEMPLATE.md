## What and why
<!-- one paragraph; link the doc/phase it belongs to -->

## Checklist
- [ ] Research only: no orders, no broker/live code paths, no keys
- [ ] No secrets, market data, vault data, `*.pt`, or the live SDE ledger committed
- [ ] `engine/` pass-bar gates, vault and ledger-N counting untouched (or change approved in writing, see CHANGELOG)
- [ ] `make test` green (SDE 73 + engine 18, or updated counts stated here)
- [ ] CHANGELOG.md and the relevant `docs/` page updated
- [ ] Results reported honestly, including misses against targets
