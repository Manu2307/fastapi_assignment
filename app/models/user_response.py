from sqlalchemy import Column, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.models.base_model import BaseModel, AuditUpdateModel, AuditCreateModel
from app.models.user import User
from app.models.questions import Questions



class UserResponse(BaseModel, AuditCreateModel,AuditUpdateModel):
    __tablename__ = "user_response"
    __table_args__ = (
        {"schema": "application"},
    )
    user_id = Column(UUID(as_uuid=True), ForeignKey(User.id))
    question_id = Column(UUID(as_uuid=True), ForeignKey(Questions.id))
    response_flag = Column(Boolean, nullable=False)
