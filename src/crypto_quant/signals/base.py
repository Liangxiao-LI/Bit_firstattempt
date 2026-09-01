"""Base signal class and interface."""

from abc import ABC, abstractmethod
import pandas as pd


class BaseSignal(ABC):
    """Abstract base class for trading signals."""
    
    def __init__(self, name: str):
        """
        Initialize signal.
        
        Args:
            name: Signal name
        """
        self.name = name
    
    @abstractmethod
    def generate(self, data: pd.DataFrame) -> pd.Series:
        """
        Generate trading signal.
        
        Args:
            data: Feature DataFrame
            
        Returns:
            Signal series with values in [-1, 0, 1] or [-1.0, 1.0]
            -1: Short signal
            0: Neutral/no position
            1: Long signal
        """
        pass
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r})"
