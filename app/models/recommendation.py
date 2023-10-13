from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.models.base_model import BaseModel, AuditUpdateModel, AuditCreateModel
from app.models.combinations import Combinations


class Recommendation(BaseModel, AuditCreateModel, AuditUpdateModel):
    __tablename__ = "recommendation"
    __table_args__ = (
        {"schema": "application"},
    )
    consequence = Column(String(512), unique=True, nullable=False)
    recommendation = Column(String(512), unique=True, nullable=False)
    combination_id = Column(UUID(as_uuid=True), ForeignKey(Combinations.id))
