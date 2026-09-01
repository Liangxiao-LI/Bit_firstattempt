"""Returns feature engineering."""

import pandas as pd
import numpy as np


def simple_returns(prices: pd.Series, periods: int = 1) -> pd.Series:
    """
    Calculate simple returns.
    
    Args:
        prices: Price series
        periods: Number of periods for return calculation
        
    Returns:
        Simple returns series
    """
    return prices.pct_change(periods=periods)


def log_returns(prices: pd.Series, periods: int = 1) -> pd.Series:
    """
    Calculate log returns.
    
    Args:
        prices: Price series
        periods: Number of periods for return calculation
        
    Returns:
        Log returns series
    """
    return np.log(prices / prices.shift(periods))


def calculate_forward_returns(
    prices: pd.Series,
    periods: int = 1,
) -> pd.Series:
    """
    Calculate forward-looking returns (target variable).
    
    Critical: This uses future data and must be kept separate from features.
    
    Args:
        prices: Price series
        periods: Number of periods forward
        
    Returns:
        Forward returns series
    """
    return prices.shift(-periods).pct_change(periods=periods)
