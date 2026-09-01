"""Performance metrics calculation."""

import pandas as pd
import numpy as np
from typing import Dict


class MetricsCalculator:
    """Calculates backtest performance metrics."""
    
    def __init__(self, equity_curve: pd.Series, risk_free_rate: float = 0.02):
        """
        Initialize metrics calculator.
        
        Args:
            equity_curve: Equity curve series with DatetimeIndex
            risk_free_rate: Annual risk-free rate
        """
        self.equity_curve = equity_curve
        self.risk_free_rate = risk_free_rate
        self.returns = equity_curve.pct_change()
    
    def calculate_total_return(self) -> float:
        """Calculate total return."""
        return (self.equity_curve.iloc[-1] / self.equity_curve.iloc[0]) - 1
    
    def calculate_annualized_return(self) -> float:
        """Calculate annualized return."""
        years = (self.equity_curve.index[-1] - self.equity_curve.index[0]).days / 365.25
        total_return = self.calculate_total_return()
        return (1 + total_return) ** (1 / years) - 1
    
    def calculate_annualized_volatility(self) -> float:
        """Calculate annualized volatility."""
        # Assume 1-minute returns, so 252 * 1440 per year
        return self.returns.std() * np.sqrt(252 * 1440)
    
    def calculate_sharpe_ratio(self) -> float:
        """Calculate Sharpe ratio."""
        annual_return = self.calculate_annualized_return()
        annual_vol = self.calculate_annualized_volatility()
        
        if annual_vol == 0:
            return 0.0
        
        return (annual_return - self.risk_free_rate) / annual_vol
    
    def calculate_sortino_ratio(self) -> float:
        """Calculate Sortino ratio."""
        annual_return = self.calculate_annualized_return()
        
        downside_returns = self.returns[self.returns < 0]
        downside_vol = downside_returns.std() * np.sqrt(252 * 1440)
        
        if downside_vol == 0:
            return 0.0
        
        return (annual_return - self.risk_free_rate) / downside_vol
    
    def calculate_max_drawdown(self) -> float:
        """Calculate maximum drawdown."""
        cummax = self.equity_curve.cummax()
        drawdown = (self.equity_curve - cummax) / cummax
        return drawdown.min()
    
    def calculate_metrics(self) -> Dict[str, float]:
        """Calculate all metrics."""
        return {
            "total_return": self.calculate_total_return(),
            "annualized_return": self.calculate_annualized_return(),
            "annualized_volatility": self.calculate_annualized_volatility(),
            "sharpe_ratio": self.calculate_sharpe_ratio(),
            "sortino_ratio": self.calculate_sortino_ratio(),
            "max_drawdown": self.calculate_max_drawdown(),
        }
