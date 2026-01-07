from pydantic import BaseModel, Field
from typing import Tuple
from datetime import datetime


class CCTVFrame(BaseModel):
    id: int
    vrijeme_snimanja: datetime
    koordinate: Tuple[float, float] = Field(default=(0.0, 0.0))
