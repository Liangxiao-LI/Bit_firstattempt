"""Test data module."""

import pytest
import pandas as pd
import numpy as np
from crypto_quant.data.validation import validate_klines, validate_funding_rate


class TestKlineValidation:
    """Test kline data validation."""
    
    def test_valid_klines(self):
        """Test validation of valid kline data."""
        df = pd.DataFrame({
            'timestamp': pd.date_range('2024-01-01', periods=10, freq='1min'),
            'open': np.random.uniform(40000, 50000, 10),
            'high': np.random.uniform(40000, 50000, 10),
            'low': np.random.uniform(40000, 50000, 10),
            'close': np.random.uniform(40000, 50000, 10),
            'volume': np.random.uniform(1, 100, 10),
        })
        
        # Ensure high >= low and close is within bounds
        df['high'] = df[['open', 'high', 'close']].max(axis=1)
        df['low'] = df[['open', 'low', 'close']].min(axis=1)
        
        is_valid, errors = validate_klines(df)
        assert is_valid, f"Valid klines marked as invalid: {errors}"
    
    def test_duplicate_timestamps(self):
        """Test detection of duplicate timestamps."""
        df = pd.DataFrame({
            'timestamp': [pd.Timestamp('2024-01-01')] * 5,
            'open': np.random.uniform(40000, 50000, 5),
            'high': np.random.uniform(40000, 50000, 5),
            'low': np.random.uniform(40000, 50000, 5),
            'close': np.random.uniform(40000, 50000, 5),
            'volume': np.random.uniform(1, 100, 5),
        })
        
        is_valid, errors = validate_klines(df)
        assert not is_valid
        assert any('duplicate' in err.lower() for err in errors)
    
    def test_missing_columns(self):
        """Test detection of missing columns."""
        df = pd.DataFrame({
            'timestamp': pd.date_range('2024-01-01', periods=5, freq='1min'),
            'open': np.random.uniform(40000, 50000, 5),
            'high': np.random.uniform(40000, 50000, 5),
            # Missing 'low', 'close', 'volume'
        })
        
        is_valid, errors = validate_klines(df)
        assert not is_valid
        assert any('missing' in err.lower() for err in errors)


class TestFundingRateValidation:
    """Test funding rate data validation."""
    
    def test_valid_funding_rate(self):
        """Test validation of valid funding rate data."""
        df = pd.DataFrame({
            'timestamp': pd.date_range('2024-01-01', periods=10, freq='8h'),
            'symbol': ['BTCUSDT'] * 10,
            'funding_rate': np.random.uniform(-0.01, 0.01, 10),
        })
        
        is_valid, errors = validate_funding_rate(df)
        assert is_valid, f"Valid funding rate marked as invalid: {errors}"
