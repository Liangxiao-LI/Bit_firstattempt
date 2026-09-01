"""Diagnostics and sanity checks."""

import pandas as pd
import numpy as np


class ResearchDiagnostics:
    """Provides research-level diagnostics."""
    
    @staticmethod
    def check_look_ahead_bias(feature_dates: pd.DatetimeIndex, target_dates: pd.DatetimeIndex) -> bool:
        """
        Check if features have any future target dates (look-ahead bias).
        
        Args:
            feature_dates: Dates when features were available
            target_dates: Dates when targets were available
            
        Returns:
            True if no look-ahead bias, False otherwise
        """
        # Features should never use future targets
        return (feature_dates <= target_dates).all()
    
    @staticmethod
    def check_data_leakage(data: pd.DataFrame, split_date: str) -> bool:
        """
        Check if data contains future information relative to split date.
        
        Args:
            data: DataFrame with data
            split_date: Date to check against (ISO format)
            
        Returns:
            True if no leakage, False otherwise
        """
        split = pd.to_datetime(split_date)
        return (data.index <= split).all()
    
    @staticmethod
    def analyze_signal_distribution(signal: pd.Series) -> dict:
        """
        Analyze signal distribution.
        
        Args:
            signal: Signal series
            
        Returns:
            Dictionary with distribution statistics
        """
        return {
            "long_pct": (signal == 1).sum() / len(signal),
            "neutral_pct": (signal == 0).sum() / len(signal),
            "short_pct": (signal == -1).sum() / len(signal),
            "transitions": (signal.diff() != 0).sum(),
        }
    
    @staticmethod
    def analyze_return_distribution(returns: pd.Series) -> dict:
        """
        Analyze return distribution.
        
        Args:
            returns: Return series
            
        Returns:
            Dictionary with distribution statistics
        """
        return {
            "mean": returns.mean(),
            "std": returns.std(),
            "skew": returns.skew(),
            "kurtosis": returns.kurtosis(),
            "positive_pct": (returns > 0).sum() / len(returns),
        }
