"""Test metrics module."""

import pytest
import pandas as pd
import numpy as np
from crypto_quant.research.diagnostics import ResearchDiagnostics


class TestDiagnostics:
    """Test research diagnostics."""
    
    def test_signal_distribution(self):
        """Test signal distribution analysis."""
        signal = pd.Series([1, 0, -1, 1, 1, 0, 0, -1, -1, 1])
        
        dist = ResearchDiagnostics.analyze_signal_distribution(signal)
        
        assert dist['long_pct'] == 0.4
        assert dist['neutral_pct'] == 0.3
        assert dist['short_pct'] == 0.3
        assert dist['transitions'] > 0
    
    def test_return_distribution(self):
        """Test return distribution analysis."""
        returns = pd.Series(np.random.normal(0.001, 0.01, 100))
        
        dist = ResearchDiagnostics.analyze_return_distribution(returns)
        
        assert 'mean' in dist
        assert 'std' in dist
        assert 'skew' in dist
        assert 'kurtosis' in dist
        assert 'positive_pct' in dist
        
        assert 0 <= dist['positive_pct'] <= 1
