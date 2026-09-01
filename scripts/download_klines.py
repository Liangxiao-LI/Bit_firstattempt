"""
Example script for downloading historical kline data.

Usage:
    python scripts/download_klines.py
"""

from pathlib import Path
from crypto_quant.data.downloader import download_klines
from crypto_quant.utils.logging import setup_logging

logger = setup_logging(__name__)


def main():
    """Download historical kline data."""
    logger.info("Starting kline download...")
    
    output_dir = Path("./data/raw/klines")
    
    try:
        download_klines(
            symbol="BTCUSDT",
            interval="1m",
            start_date="2022-01-01",
            end_date="2026-08-31",
            output_dir=str(output_dir),
        )
        logger.info("Kline download completed successfully")
    except Exception as e:
        logger.error(f"Error downloading klines: {e}")
        raise


if __name__ == "__main__":
    main()
