"""
Example script for downloading funding rate data.

Usage:
    python scripts/download_funding.py
"""

from pathlib import Path
from crypto_quant.data.downloader import download_funding_rate
from crypto_quant.utils.logging import setup_logging

logger = setup_logging(__name__)


def main():
    """Download historical funding rate data."""
    logger.info("Starting funding rate download...")
    
    output_dir = Path("./data/raw/funding")
    
    try:
        download_funding_rate(
            symbol="BTCUSDT",
            start_date="2022-01-01",
            end_date="2026-08-31",
            output_dir=str(output_dir),
        )
        logger.info("Funding rate download completed successfully")
    except Exception as e:
        logger.error(f"Error downloading funding rates: {e}")
        raise


if __name__ == "__main__":
    main()
