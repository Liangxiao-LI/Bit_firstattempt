"""Volatility feature engineering."""

import pandas as pd
import numpy as np


def realized_volatility(returns: pd.Series, window: int = 20, annualized: bool = True) -> pd.Series:
    """
    Calculate realized volatility.
    
    Args:
        returns: Returns series
        window: Rolling window size
        annualized: Return annualized volatility if True
        
    Returns:
        Volatility series
    """
    vol = returns.rolling(window=window).std()
    
    if annualized:
        # Assume 252 trading days per year, 1440 minutes per day
        vol = vol * np.sqrt(252 * 1440)
    
    return vol


def parkinson_volatility(high: pd.Series, low: pd.Series, window: int = 20) -> pd.Series:
    """
    Calculate Parkinson volatility (range-based).
    
    Args:
        high: High price series
        low: Low price series
        window: Rolling window size
        
    Returns:
        Volatility series
    """
    hl_ratio = np.log(high / low)
    return hl_ratio.rolling(window=window).std() * np.sqrt(252)


def garman_klass_volatility(
    high: pd.Series,
    low: pd.Series,
    close: pd.Series,
    open: pd.Series,
    window: int = 20,
) -> pd.Series:
    """
    Calculate Garman-Klass volatility estimator.
    
    Args:
        high: High price series
        low: Low price series
        close: Close price series
        open: Open price series
        window: Rolling window size
        
    Returns:
        Volatility series
    """
    hl = np.log(high / low)
    co = np.log(close / open)
    
    gk = 0.5 * (hl ** 2) - (2 * np.log(2) - 1) * (co ** 2)
    
    return np.sqrt(gk.rolling(window=window).mean()) * np.sqrt(252)
