"""Open interest feature engineering."""

import pandas as pd
import numpy as np


def oi_change(open_interest: pd.Series, periods: int = 1) -> pd.Series:
    """
    Calculate change in open interest.
    
    Args:
        open_interest: Open interest series
        periods: Number of periods for change calculation
        
    Returns:
        Change series
    """
    return open_interest.diff(periods=periods)


def oi_pct_change(open_interest: pd.Series, periods: int = 1) -> pd.Series:
    """
    Calculate percentage change in open interest.
    
    Args:
        open_interest: Open interest series
        periods: Number of periods for change calculation
        
    Returns:
        Percentage change series
    """
    return open_interest.pct_change(periods=periods)


def oi_zscore(open_interest: pd.Series, window: int = 60) -> pd.Series:
    """
    Calculate open interest Z-score.
    
    Args:
        open_interest: Open interest series
        window: Rolling window size
        
    Returns:
        Z-score series
    """
    mean = open_interest.rolling(window=window).mean()
    std = open_interest.rolling(window=window).std()
    
    return (open_interest - mean) / std


def price_oi_interaction(
    close: pd.Series,
    open_interest: pd.Series,
    price_window: int = 5,
    oi_window: int = 5,
) -> pd.Series:
    """
    Classify price + OI regimes.
    
    Regimes:
    1: price up, OI up (trend with increasing leverage)
    2: price up, OI down (trend with decreasing leverage)
    3: price down, OI up (downtrend with increasing leverage)
    4: price down, OI down (downtrend with decreasing leverage)
    
    Args:
        close: Close price series
        open_interest: Open interest series
        price_window: Window for price direction
        oi_window: Window for OI direction
        
    Returns:
        Regime indicator series (1, 2, 3, 4)
    """
    price_direction = close.diff(price_window) > 0
    oi_direction = open_interest.diff(oi_window) > 0
    
    regime = pd.Series(0, index=close.index)
    regime[(price_direction) & (oi_direction)] = 1
    regime[(price_direction) & (~oi_direction)] = 2
    regime[(~price_direction) & (oi_direction)] = 3
    regime[(~price_direction) & (~oi_direction)] = 4
    
    return regime
