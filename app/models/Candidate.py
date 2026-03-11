from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import Optional
import random

class Candidate(BaseModel):
    name: str
    age: int = Field(...,ge=1,le=101)
    gender: str
    rfq: str
    curp: str
    income: float = Field(...,ge=0)
    amountRequested: float = Field(...,ge=1)
    yearExperience: int
    status: Optional[int] = None
    score: int = Field(default_factory=lambda:random.randint(300,900))
    dateCreated: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))