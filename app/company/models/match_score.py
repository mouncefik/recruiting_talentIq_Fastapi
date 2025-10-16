import uuid
from datetime import datetime, timezone

from sqlalchemy import JSON, Column, DateTime, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base


class MatchScoreModel(Base):
    __tablename__ = "match_score"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    talent_id = Column(UUID(as_uuid=True), ForeignKey("talent.id"))
    job_id = Column(UUID(as_uuid=True), ForeignKey("job.id"))
    score = Column(Float)
    match_details = Column(JSON)
    calculated_at = Column(DateTime, default=datetime.now(timezone.utc))

    talent = relationship("TalentModel", back_populates="match_scores")
    job = relationship("JobModel", back_populates="match_scores")
