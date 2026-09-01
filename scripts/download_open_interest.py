"""
Example script for downloading open interest data.

Usage:
    python scripts/download_open_interest.py
"""

from pathlib import Path
from crypto_quant.data.downloader import download_open_interest
from crypto_quant.utils.logging import setup_logging

logger = setup_logging(__name__)


def main():
    """Download historical open interest data."""
    logger.info("Starting open interest download...")
    
    output_dir = Path("./data/raw/open_interest")
    
    try:
        download_open_interest(
            symbol="BTCUSDT",
            start_date="2022-01-01",
            end_date="2026-08-31",
            output_dir=str(output_dir),
        )
        logger.info("Open interest download completed successfully")
    except Exception as e:
        logger.error(f"Error downloading open interest: {e}")
        raise


if __name__ == "__main__":
    main()
