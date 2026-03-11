from pydantic import BaseModel, Field
from datetime import datetime, timezone

class CandidateDocument(BaseModel):
    userId: str
    name: str
    size: int
    path: str
    dateCreated: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))