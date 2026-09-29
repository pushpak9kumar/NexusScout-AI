from pydantic import BaseModel
from typing import Optional # <-- 1. Import Optional

class CompetitorCreate(BaseModel):
    name: str
    url: str

class CompetitorResponse(BaseModel):
    id: int
    name: str
    url: str
    analysis: Optional[str] = None # <-- 2. ADDED THIS LINE

    model_config = {
        "from_attributes": True
    }