"""Volume feature engineering."""

import pandas as pd
import numpy as np
from scipy import stats


def volume_zscore(volume: pd.Series, window: int = 20) -> pd.Series:
    """
    Calculate volume Z-score (deviation from rolling mean).
    
    Args:
        volume: Volume series
        window: Rolling window size
        
    Returns:
        Z-score series
    """
    mean = volume.rolling(window=window).mean()
    std = volume.rolling(window=window).std()
    
    return (volume - mean) / std


def volume_change(volume: pd.Series, periods: int = 1) -> pd.Series:
    """
    Calculate volume change.
    
    Args:
        volume: Volume series
        periods: Number of periods for change calculation
        
    Returns:
        Volume change series
    """
    return volume.pct_change(periods=periods)


def taker_buy_ratio(taker_buy_volume: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Calculate ratio of taker buy volume to total volume.
    
    Args:
        taker_buy_volume: Taker buy volume series
        volume: Total volume series
        
    Returns:
        Ratio series (0 to 1)
    """
    return taker_buy_volume / volume


def on_balance_volume(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Calculate On-Balance Volume (OBV).
    
    Args:
        close: Close price series
        volume: Volume series
        
    Returns:
        OBV series
    """
    obv = pd.Series(0.0, index=close.index)
    
    for i in range(1, len(close)):
        if close.iloc[i] > close.iloc[i-1]:
            obv.iloc[i] = obv.iloc[i-1] + volume.iloc[i]
        elif close.iloc[i] < close.iloc[i-1]:
            obv.iloc[i] = obv.iloc[i-1] - volume.iloc[i]
        else:
            obv.iloc[i] = obv.iloc[i-1]
    
    return obv
