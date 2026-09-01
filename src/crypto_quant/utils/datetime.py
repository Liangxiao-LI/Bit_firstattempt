"""Datetime utilities."""

import pandas as pd
from datetime import datetime, timedelta


def to_utc(dt: datetime) -> datetime:
    """Convert datetime to UTC."""
    if dt.tzinfo is None:
        return dt.replace(tzinfo=pd.Timestamp.now().tz)
    return dt.astimezone(pd.Timestamp.now().tz)


def get_minute_boundaries(start: datetime, end: datetime) -> pd.DatetimeIndex:
    """Get all 1-minute boundaries between start and end."""
    return pd.date_range(start, end, freq='1T', tz='UTC')


def align_to_minute(dt: datetime) -> datetime:
    """Align datetime to the nearest minute boundary."""
    return dt.replace(second=0, microsecond=0)
