"""Test backtest module."""

import pytest
import pandas as pd
import numpy as np
from crypto_quant.backtest.metrics import MetricsCalculator
from crypto_quant.backtest.costs import CostModel


class TestMetrics:
    """Test performance metrics calculation."""
    
    def test_sharpe_ratio(self):
        """Test Sharpe ratio calculation."""
        # Create simple equity curve
        dates = pd.date_range('2024-01-01', periods=252*1440, freq='1min', tz='UTC')
        equity = pd.Series(100000 * (1 + np.random.normal(0, 0.0001, len(dates))).cumprod(), index=dates)
        
        metrics_calc = MetricsCalculator(equity)
        sharpe = metrics_calc.calculate_sharpe_ratio()
        
        assert isinstance(sharpe, float)
    
    def test_max_drawdown(self):
        """Test maximum drawdown calculation."""
        dates = pd.date_range('2024-01-01', periods=100, freq='D')
        equity = pd.Series([100000, 110000, 105000, 115000, 95000, 98000, 110000], index=dates[:7])
        
        metrics_calc = MetricsCalculator(equity)
        max_dd = metrics_calc.calculate_max_drawdown()
        
        assert max_dd < 0  # Drawdown should be negative
        assert max_dd >= -1  # Drawdown should not exceed -100%


class TestCostModel:
    """Test transaction cost modeling."""
    
    def test_trading_cost_calculation(self):
        """Test trading cost calculation."""
        cost_model = CostModel(maker_fee_bps=2, taker_fee_bps=5, slippage_bps=2)
        
        cost = cost_model.calculate_trading_cost(100000, is_maker=False, include_slippage=True)
        
        # Cost should be approximately (5 + 2) bps = 70 USD
        expected = 100000 * (7 / 10000)
        assert abs(cost - expected) < 1
    
    def test_funding_cost(self):
        """Test funding cost calculation."""
        cost_model = CostModel()
        
        funding_cost = cost_model.calculate_funding_cost(
            notional_value=100000,
            funding_rate=0.0001,  # 0.01%
            position_size=1,  # Long
        )
        
        expected = 100000 * 0.0001 * 1
        assert abs(funding_cost - expected) < 0.01
