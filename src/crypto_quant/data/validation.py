"""Data validation utilities."""

import pandas as pd
from typing import Tuple, List


def validate_klines(df: pd.DataFrame) -> Tuple[bool, List[str]]:
    """
    Validate kline DataFrame.
    
    Args:
        df: DataFrame with kline data
        
    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    errors = []
    
    # Check required columns
    required_cols = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        errors.append(f"Missing columns: {missing_cols}")
    
    # Check for duplicates
    if df['timestamp'].duplicated().any():
        errors.append("Duplicate timestamps found")
    
    # Check for missing data
    if df.isnull().any().any():
        errors.append("Missing data (NaN) found")
    
    # Check price bounds
    if (df['low'] > df['high']).any():
        errors.append("Low > High in some rows")
    
    if (df['open'] < df['low']).any() or (df['open'] > df['high']).any():
        errors.append("Open not within [Low, High] range")
    
    # TODO: Add more validation rules
    
    return len(errors) == 0, errors


def validate_funding_rate(df: pd.DataFrame) -> Tuple[bool, List[str]]:
    """
    Validate funding rate DataFrame.
    
    Args:
        df: DataFrame with funding rate data
        
    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    errors = []
    
    required_cols = ['timestamp', 'symbol', 'funding_rate']
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        errors.append(f"Missing columns: {missing_cols}")
    
    if df['timestamp'].duplicated().any():
        errors.append("Duplicate timestamps found")
    
    if df.isnull().any().any():
        errors.append("Missing data (NaN) found")
    
    # TODO: Add more validation rules
    
    return len(errors) == 0, errors


def validate_open_interest(df: pd.DataFrame) -> Tuple[bool, List[str]]:
    """
    Validate open interest DataFrame.
    
    Args:
        df: DataFrame with open interest data
        
    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    errors = []
    
    required_cols = ['timestamp', 'symbol', 'open_interest']
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        errors.append(f"Missing columns: {missing_cols}")
    
    if df['timestamp'].duplicated().any():
        errors.append("Duplicate timestamps found")
    
    if df.isnull().any().any():
        errors.append("Missing data (NaN) found")
    
    # TODO: Add more validation rules
    
    return len(errors) == 0, errors
