import uuid
from datetime import datetime, timezone

from sqlalchemy import JSON, Column, DateTime, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base


class ResumeModel(Base):
    __tablename__ = "resume"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    talent_id = Column(UUID(as_uuid=True), ForeignKey("talent.id"))
    file_path = Column(String)
    extracted_text = Column(Text)
    analysis_result = Column(JSON)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    talent = relationship("TalentModel", back_populates="resumes")
