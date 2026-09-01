"""Transaction cost modeling."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class TransactionCosts:
    """Transaction cost breakdown."""
    trading_fees: float  # Taker/maker fees
    slippage: float      # Slippage costs
    funding_costs: float  # Funding payments
    total: float


class CostModel:
    """Models trading costs."""
    
    def __init__(
        self,
        maker_fee_bps: float = 2.0,
        taker_fee_bps: float = 5.0,
        slippage_bps: float = 2.0,
    ):
        """
        Initialize cost model.
        
        Args:
            maker_fee_bps: Maker fee in basis points
            taker_fee_bps: Taker fee in basis points
            slippage_bps: Slippage in basis points
        """
        self.maker_fee_bps = maker_fee_bps
        self.taker_fee_bps = taker_fee_bps
        self.slippage_bps = slippage_bps
    
    def calculate_trading_cost(
        self,
        notional_value: float,
        is_maker: bool = False,
        include_slippage: bool = True,
    ) -> float:
        """
        Calculate trading cost.
        
        Args:
            notional_value: Trade notional value
            is_maker: True for maker, False for taker
            include_slippage: Include slippage in cost
            
        Returns:
            Total cost in base currency
        """
        fee_bps = self.maker_fee_bps if is_maker else self.taker_fee_bps
        cost = notional_value * fee_bps / 10000
        
        if include_slippage:
            cost += notional_value * self.slippage_bps / 10000
        
        return cost
    
    def calculate_funding_cost(
        self,
        notional_value: float,
        funding_rate: float,
        position_size: float,
    ) -> float:
        """
        Calculate funding payments.
        
        Args:
            notional_value: Position notional value
            funding_rate: Funding rate
            position_size: Position size (-1, 0, 1)
            
        Returns:
            Funding cost
        """
        return notional_value * funding_rate * position_size
