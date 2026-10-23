"""Strategy Hunter engine (Phase 1). Research/paper only: no order code, no desk access.
Credits: vectorbt (Oleg Polakow, Apache-2.0 w/ Commons Clause) for backtests; arch (Kevin Sheppard, NCSA)
for Hansen SPA; CSCV/PBO per Bailey, Borwein, Lopez de Prado & Zhu (2014), logic adapted from
research_lab/vendor/pypbo (esvhd, MIT); DSR per Bailey & Lopez de Prado (2014)."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
