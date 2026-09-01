"""Funding rate feature engineering."""

import pandas as pd
import numpy as np


def funding_zscore(funding_rate: pd.Series, window: int = 60) -> pd.Series:
    """
    Calculate funding rate Z-score.
    
    Args:
        funding_rate: Funding rate series
        window: Rolling window size
        
    Returns:
        Z-score series
    """
    mean = funding_rate.rolling(window=window).mean()
    std = funding_rate.rolling(window=window).std()
    
    return (funding_rate - mean) / std


def funding_change(funding_rate: pd.Series, periods: int = 1) -> pd.Series:
    """
    Calculate change in funding rate.
    
    Args:
        funding_rate: Funding rate series
        periods: Number of periods for change calculation
        
    Returns:
        Change series
    """
    return funding_rate.diff(periods=periods)


def extreme_funding_indicator(funding_rate: pd.Series, threshold: float = 0.02) -> pd.Series:
    """
    Identify extreme funding periods.
    
    Args:
        funding_rate: Funding rate series
        threshold: Threshold for extreme funding (e.g., 0.02 = 2%)
        
    Returns:
        Binary series (1 = extreme, 0 = normal)
    """
    return (np.abs(funding_rate) > threshold).astype(int)


def cumulative_funding_pnl(
    funding_rate: pd.Series,
    position: pd.Series,
    notional_value: float = 1.0,
) -> pd.Series:
    """
    Calculate cumulative funding payments.
    
    Args:
        funding_rate: Funding rate series (8-hourly for Binance)
        position: Position series (-1, 0, 1)
        notional_value: Notional value of position
        
    Returns:
        Cumulative funding PnL series
    """
    # Funding is paid per position per funding period
    funding_payment = funding_rate * position * notional_value
    return funding_payment.cumsum()
