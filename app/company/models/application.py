import uuid
from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base


class ApplicationModel(Base):
    __tablename__ = "application"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    talent_id = Column(UUID(as_uuid=True), ForeignKey("talent.id"))
    job_id = Column(UUID(as_uuid=True), ForeignKey("job.id"))
    status = Column(String)
    applied_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    updated_at = Column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )

    talent = relationship("TalentModel", back_populates="applications")
    job = relationship("JobModel", back_populates="applications")
