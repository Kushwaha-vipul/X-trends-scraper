from datetime import datetime, timezone
from typing import Optional
from sqlmodel import SQLModel, Field
def get_utc_now():
    return datetime.now(timezone.utc)

class TrendRun(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    trend1: Optional[str] = None
    trend2: Optional[str] = None
    trend3: Optional[str] = None
    trend4: Optional[str] = None
    trend5: Optional[str] = None
    finished_at: datetime = Field(default_factory=get_utc_now)
    ip_address: Optional[str] = None
