import uuid
from datetime import datetime, timezone

from sqlalchemy import JSON, Column, DateTime, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base


class TalentModel(Base):
    __tablename__ = "talent"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String)
    skills = Column(JSON)  # Using JSON for list of skills
    experience_years = Column(Integer)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )

    applications = relationship("ApplicationModel", back_populates="talent")
    resumes = relationship("ResumeModel", back_populates="talent")
    match_scores = relationship("MatchScoreModel", back_populates="talent")
