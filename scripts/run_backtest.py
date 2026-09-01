"""
Example script for running a backtest.

Steps:
1. Load canonical dataset and features
2. Generate signals
3. Run backtest
4. Calculate metrics
5. Save results

Usage:
    python scripts/run_backtest.py
"""

import pandas as pd

from crypto_quant.data.loaders import load_canonical_dataset
from crypto_quant.signals.momentum import MomentumSignal
from crypto_quant.signals.mean_reversion import MeanReversionSignal
from crypto_quant.signals.composite import CompositeSignal
from crypto_quant.backtest.engine import BacktestEngine
from crypto_quant.backtest.metrics import MetricsCalculator
from crypto_quant.utils.logging import setup_logging

logger = setup_logging(__name__)


def main():
    """Run backtest."""
    logger.info("Starting backtest...")
    
    try:
        # Load data
        logger.info("Loading canonical dataset...")
        data = load_canonical_dataset()
        
        # Generate signals
        logger.info("Generating signals...")
        momentum_signal = MomentumSignal(lookback=5, threshold=0.001)
        mean_reversion_signal = MeanReversionSignal(window=20, threshold=1.5)
        
        composite_signal = CompositeSignal(
            signals=[momentum_signal, mean_reversion_signal],
            weights={"Momentum_5": 0.5, "MeanReversion_20": 0.5},
        )
        
        signal = composite_signal.generate(data)
        
        # Run backtest
        logger.info("Running backtest...")
        backtest = BacktestEngine(
            data=data,
            signal=signal,
            initial_capital=100000.0,
            maker_fee=0.0002,
            taker_fee=0.0005,
            slippage=0.0002,
        )
        
        results = backtest.run()
        
        # Calculate metrics
        logger.info("Calculating metrics...")
        metrics_calc = MetricsCalculator(results['equity_curve'])
        metrics = metrics_calc.calculate_metrics()
        
        # Print results
        logger.info("=== BACKTEST RESULTS ===")
        for key, value in metrics.items():
            logger.info(f"{key}: {value:.4f}")
        
        logger.info("Backtest completed successfully")
        
    except Exception as e:
        logger.error(f"Error running backtest: {e}")
        raise


if __name__ == "__main__":
    main()
