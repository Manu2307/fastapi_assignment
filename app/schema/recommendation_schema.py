from typing import List
from uuid import UUID

from pydantic import BaseModel, Field


class RecommendationRequestBaseModel(BaseModel):
    consequence: str = Field(..., title="Possible Consequence")
    recommendation: str = Field(..., min_length=5)
    combination_id: int = Field(..., le=12, ge=1)


class RecommendationResponseModel(BaseModel):
    id: UUID = Field(..., title="Recommendation id")

    class Config:
        orm_mode = True
