"""
Example script for building the canonical research dataset.

Steps:
1. Load raw data
2. Validate
3. Align timestamps
4. Compute features
5. Save processed dataset

Usage:
    python scripts/build_dataset.py
"""

from pathlib import Path
import pandas as pd

from crypto_quant.data.loaders import load_klines, load_funding_rate, load_open_interest
from crypto_quant.data.storage import save_canonical_dataset
from crypto_quant.features.feature_pipeline import FeaturePipeline
from crypto_quant.utils.logging import setup_logging

logger = setup_logging(__name__)


def main():
    """Build canonical research dataset."""
    logger.info("Starting dataset building...")
    
    try:
        # Load raw data
        logger.info("Loading raw data...")
        klines = load_klines()
        funding_rate = load_funding_rate()
        open_interest = load_open_interest()
        
        # TODO: Align datasets by timestamp
        # TODO: Validate alignments
        
        logger.info("Building feature pipeline...")
        pipeline = FeaturePipeline(klines)
        canonical_dataset = pipeline.compute_all_features()
        
        logger.info("Saving canonical dataset...")
        save_canonical_dataset(canonical_dataset)
        
        logger.info("Dataset building completed successfully")
        logger.info(f"Dataset shape: {canonical_dataset.shape}")
        logger.info(f"Date range: {canonical_dataset.index[0]} to {canonical_dataset.index[-1]}")
        
    except Exception as e:
        logger.error(f"Error building dataset: {e}")
        raise


if __name__ == "__main__":
    main()
