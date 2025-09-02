from pydantic import BaseModel
from datetime import datetime

class TrendRunBase(BaseModel):
    trend1: str | None = None
    trend2: str | None = None
    trend3: str | None = None
    trend4: str | None = None
    trend5: str | None = None
    finished_at: datetime
    ip_address: str

class TrendRunCreate(TrendRunBase):
    pass

class TrendRunOut(TrendRunBase):
    id: int

    model_config = {
        "from_attributes": True
    }
