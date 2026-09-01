"""Composite signals combining multiple signal sources."""

import pandas as pd
from typing import List, Dict
from .base import BaseSignal


class CompositeSignal(BaseSignal):
    """Combines multiple signals using weighted averaging or voting."""
    
    def __init__(self, signals: List[BaseSignal], weights: Dict[str, float] = None):
        """
        Initialize composite signal.
        
        Args:
            signals: List of BaseSignal instances
            weights: Dict mapping signal name to weight (default: equal weights)
        """
        super().__init__(name="CompositeSignal")
        self.signals = signals
        
        if weights is None:
            # Equal weighting
            self.weights = {sig.name: 1.0 / len(signals) for sig in signals}
        else:
            self.weights = weights
    
    def generate(self, data: pd.DataFrame) -> pd.Series:
        """
        Generate composite signal.
        
        Args:
            data: DataFrame with feature data
            
        Returns:
            Weighted signal series
        """
        weighted_signal = pd.Series(0.0, index=data.index)
        
        for signal in self.signals:
            sig = signal.generate(data)
            weight = self.weights.get(signal.name, 1.0 / len(self.signals))
            weighted_signal += sig * weight
        
        # Quantize to [-1, 0, 1]
        result = pd.Series(0, index=data.index, dtype=int)
        result[weighted_signal > 0.1] = 1
        result[weighted_signal < -0.1] = -1
        
        return result
