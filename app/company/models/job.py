import uuid
from datetime import datetime, timezone

from sqlalchemy import JSON, Column, DateTime, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base


class JobModel(Base):
    __tablename__ = "job"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(Text)
    requirements = Column(JSON)
    status = Column(String)
    department_id = Column(UUID(as_uuid=True), ForeignKey("department.id"))
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )

    applications = relationship("ApplicationModel", back_populates="job")
    match_scores = relationship("MatchScoreModel", back_populates="job")
    department = relationship("DepartmentModel", back_populates="jobs")
