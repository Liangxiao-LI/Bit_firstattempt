"""Mean reversion signals."""

import pandas as pd
import numpy as np
from .base import BaseSignal


class MeanReversionSignal(BaseSignal):
    """
    Mean reversion signal based on volatility and price deviation.
    
    Long when price is unusually low, short when unusually high.
    """
    
    def __init__(self, window: int = 20, threshold: float = 1.5):
        """
        Initialize mean reversion signal.
        
        Args:
            window: Rolling window for mean and std
            threshold: Z-score threshold for signal
        """
        super().__init__(name=f"MeanReversion_{window}")
        self.window = window
        self.threshold = threshold
    
    def generate(self, data: pd.DataFrame) -> pd.Series:
        """
        Generate mean reversion signal.
        
        Args:
            data: DataFrame with price data
            
        Returns:
            Signal series
        """
        close = data['close']
        sma = close.rolling(window=self.window).mean()
        std = close.rolling(window=self.window).std()
        
        zscore = (close - sma) / std
        
        signal = pd.Series(0, index=data.index, dtype=int)
        signal[zscore < -self.threshold] = 1  # Oversold, buy
        signal[zscore > self.threshold] = -1   # Overbought, sell
        
        return signal
