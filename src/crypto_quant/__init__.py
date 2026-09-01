"""
Crypto Quant Research - Modular cryptocurrency quantitative research and trading system.
"""

__version__ = "0.1.0"
__author__ = "Quantitative Research Team"

from . import data, features, signals, backtest, research, utils

__all__ = [
    "data",
    "features",
    "signals",
    "backtest",
    "research",
    "utils",
]
