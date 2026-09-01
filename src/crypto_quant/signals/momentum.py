"""Momentum-based signals."""

import pandas as pd
from .base import BaseSignal


class MomentumSignal(BaseSignal):
    """
    Simple momentum signal based on recent returns.
    
    Long when momentum > threshold, short when momentum < -threshold, neutral otherwise.
    """
    
    def __init__(self, lookback: int = 5, threshold: float = 0.001):
        """
        Initialize momentum signal.
        
        Args:
            lookback: Lookback period for momentum calculation
            threshold: Threshold for signal generation
        """
        super().__init__(name=f"Momentum_{lookback}")
        self.lookback = lookback
        self.threshold = threshold
    
    def generate(self, data: pd.DataFrame) -> pd.Series:
        """
        Generate momentum signal.
        
        Args:
            data: DataFrame with price data
            
        Returns:
            Signal series
        """
        if 'return_' + str(self.lookback) + 'm' not in data.columns:
            # Fallback to close price if specific return not available
            returns = data['close'].pct_change(periods=self.lookback)
        else:
            returns = data['return_' + str(self.lookback) + 'm']
        
        signal = pd.Series(0, index=data.index, dtype=int)
        signal[returns > self.threshold] = 1
        signal[returns < -self.threshold] = -1
        
        return signal
