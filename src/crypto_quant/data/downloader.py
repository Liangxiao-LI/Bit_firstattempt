"""Data downloading and collection utilities."""

from typing import Optional
from datetime import datetime
import pandas as pd


def download_klines(
    symbol: str = "BTCUSDT",
    interval: str = "1m",
    start_date: str = "2022-01-01",
    end_date: Optional[str] = None,
    output_dir: str = "./data/raw/klines",
) -> None:
    """
    Download historical kline data from Binance.
    
    Args:
        symbol: Trading pair
        interval: Kline interval
        start_date: Start date (YYYY-MM-DD)
        end_date: End date (YYYY-MM-DD)
        output_dir: Output directory for raw data
    """
    # TODO: Implement kline downloading with validation
    raise NotImplementedError("Kline downloading not yet implemented")


def download_funding_rate(
    symbol: str = "BTCUSDT",
    start_date: str = "2022-01-01",
    end_date: Optional[str] = None,
    output_dir: str = "./data/raw/funding",
) -> None:
    """
    Download historical funding rate data.
    
    Args:
        symbol: Trading pair
        start_date: Start date (YYYY-MM-DD)
        end_date: End date (YYYY-MM-DD)
        output_dir: Output directory for raw data
    """
    # TODO: Implement funding rate downloading
    raise NotImplementedError("Funding rate downloading not yet implemented")


def download_open_interest(
    symbol: str = "BTCUSDT",
    start_date: str = "2022-01-01",
    end_date: Optional[str] = None,
    output_dir: str = "./data/raw/open_interest",
) -> None:
    """
    Download historical open interest data.
    
    Args:
        symbol: Trading pair
        start_date: Start date (YYYY-MM-DD)
        end_date: End date (YYYY-MM-DD)
        output_dir: Output directory for raw data
    """
    # TODO: Implement open interest downloading
    raise NotImplementedError("Open interest downloading not yet implemented")
