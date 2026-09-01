"""Test features module."""

import pytest
import pandas as pd
import numpy as np
from crypto_quant.features.returns import simple_returns, log_returns
from crypto_quant.features.volatility import realized_volatility
from crypto_quant.features.volume import volume_zscore, taker_buy_ratio


class TestReturns:
    """Test return calculations."""
    
    def test_simple_returns(self):
        """Test simple return calculation."""
        prices = pd.Series([100, 110, 121, 115])
        returns = simple_returns(prices, periods=1)
        
        expected = pd.Series([np.nan, 0.10, 0.1, -0.0495867...])
        pd.testing.assert_series_equal(returns, expected, atol=1e-5)
    
    def test_log_returns(self):
        """Test log return calculation."""
        prices = pd.Series([100, 110, 121, 115])
        log_ret = log_returns(prices, periods=1)
        
        # Log return should be close to simple return for small changes
        simple_ret = simple_returns(prices, periods=1)
        pd.testing.assert_series_equal(log_ret, simple_ret, atol=0.01)


class TestVolatility:
    """Test volatility calculations."""
    
    def test_realized_volatility(self):
        """Test realized volatility calculation."""
        returns = pd.Series(np.random.normal(0, 0.01, 100))
        vol = realized_volatility(returns, window=20, annualized=False)
        
        assert vol.iloc[-1] > 0
        assert not vol.isna().any()


class TestVolume:
    """Test volume feature calculations."""
    
    def test_volume_zscore(self):
        """Test volume Z-score calculation."""
        volume = pd.Series(np.random.uniform(100, 1000, 50))
        zscore = volume_zscore(volume, window=20)
        
        # Z-scores should have mean ~0
        assert abs(zscore.mean()) < 1.0
    
    def test_taker_buy_ratio(self):
        """Test taker buy ratio calculation."""
        taker_buy = pd.Series(np.random.uniform(0, 100, 50))
        total_volume = taker_buy * 2  # Ensure total >= taker buy
        
        ratio = taker_buy_ratio(taker_buy, total_volume)
        
        assert (ratio >= 0).all() and (ratio <= 1).all()
