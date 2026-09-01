"""Data schemas and validation schemas using Pydantic."""

from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class KlineSchema(BaseModel):
    """Schema for 1-minute kline data."""
    
    timestamp: datetime = Field(..., description="UTC timestamp")
    open: float = Field(..., gt=0, description="Open price")
    high: float = Field(..., gt=0, description="High price")
    low: float = Field(..., gt=0, description="Low price")
    close: float = Field(..., gt=0, description="Close price")
    volume: float = Field(..., ge=0, description="Base asset volume")
    quote_volume: float = Field(..., ge=0, description="Quote asset volume")
    trade_count: int = Field(..., ge=0, description="Number of trades")
    taker_buy_base_volume: float = Field(..., ge=0, description="Taker buy base volume")
    taker_buy_quote_volume: float = Field(..., ge=0, description="Taker buy quote volume")
    
    class Config:
        validate_assignment = True


class FundingRateSchema(BaseModel):
    """Schema for funding rate data."""
    
    timestamp: datetime = Field(..., description="UTC timestamp")
    symbol: str = Field(..., description="Trading pair")
    funding_rate: float = Field(..., description="Funding rate")
    mark_price: Optional[float] = Field(None, gt=0, description="Mark price")
    
    class Config:
        validate_assignment = True


class OpenInterestSchema(BaseModel):
    """Schema for open interest data."""
    
    timestamp: datetime = Field(..., description="UTC timestamp")
    symbol: str = Field(..., description="Trading pair")
    open_interest: float = Field(..., ge=0, description="Open interest")
    open_interest_value: Optional[float] = Field(None, ge=0, description="Open interest value in USD")
    
    class Config:
        validate_assignment = True
