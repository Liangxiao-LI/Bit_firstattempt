"""Information Coefficient calculation and analysis."""

import pandas as pd
import numpy as np
from scipy.stats import spearmanr, pearsonr


class ICCalculator:
    """Calculates Information Coefficient."""
    
    @staticmethod
    def calculate_ic(factor: pd.Series, returns: pd.Series, method: str = "spearman") -> float:
        """
        Calculate IC between factor and future returns.
        
        Args:
            factor: Factor values
            returns: Forward returns (target)
            method: "pearson" or "spearman"
            
        Returns:
            IC value
        """
        if method == "spearman":
            ic, _ = spearmanr(factor, returns)
        elif method == "pearson":
            ic, _ = pearsonr(factor, returns)
        else:
            raise ValueError(f"Unknown method: {method}")
        
        return ic
    
    @staticmethod
    def calculate_rolling_ic(
        factor: pd.Series,
        returns: pd.Series,
        window: int = 60,
        method: str = "spearman",
    ) -> pd.Series:
        """
        Calculate rolling IC.
        
        Args:
            factor: Factor values
            returns: Forward returns
            window: Rolling window size
            method: "pearson" or "spearman"
            
        Returns:
            Rolling IC series
        """
        rolling_ic = pd.Series(0.0, index=factor.index)
        
        for i in range(window, len(factor)):
            factor_window = factor.iloc[i-window:i]
            returns_window = returns.iloc[i-window:i]
            
            rolling_ic.iloc[i] = ICCalculator.calculate_ic(
                factor_window, returns_window, method
            )
        
        return rolling_ic
