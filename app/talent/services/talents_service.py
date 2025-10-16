from datetime import datetime, timezone
from typing import Optional

from sqlalchemy.orm import Session

from app.company.models.application import ApplicationModel
from app.core.database import SessionLocal
from app.talent.models.resume import ResumeModel
from app.talent.models.talent import TalentModel


def get_talent_by_id(talent_id: str, db: Session = None):
    if db is None:
        db = SessionLocal()
    try:
        talent = db.query(TalentModel).filter(TalentModel.id == talent_id).first()
        return talent
    finally:
        if db:
            db.close()


def update_talent(
    talent_id: str,
    name: Optional[str] = None,
    email: Optional[str] = None,
    phone: Optional[str] = None,
    skills: Optional[list] = None,
    experience_years: Optional[int] = None,
    db: Session = None,
):
    if db is None:
        db = SessionLocal()
    try:
        talent = db.query(TalentModel).filter(TalentModel.id == talent_id).first()
        if not talent:
            return None
        if name is not None:
            talent.name = name
        if email is not None:
            talent.email = email
        if phone is not None:
            talent.phone = phone
        if skills is not None:
            talent.skills = skills
        if experience_years is not None:
            talent.experience_years = experience_years
        talent.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(talent)
        return talent
    finally:
        if db:
            db.close()


def get_resumes_for_talent(talent_id: str, db: Session = None):
    if db is None:
        db = SessionLocal()
    try:
        resumes = db.query(ResumeModel).filter(ResumeModel.talent_id == talent_id).all()
        return resumes
    finally:
        if db:
            db.close()


def create_talent(
    name: str,
    email: str,
    phone: Optional[str] = None,
    skills: Optional[list] = None,
    experience_years: Optional[int] = None,
    db: Session = None,
):
    if db is None:
        db = SessionLocal()
    try:
        new_talent = TalentModel(
            name=name,
            email=email,
            phone=phone,
            skills=skills,
            experience_years=experience_years,
        )
        db.add(new_talent)
        db.commit()
        db.refresh(new_talent)
        return new_talent
    finally:
        if db:
            db.close()


def get_applications_for_talent(talent_id: str, db: Session = None):
    if db is None:
        db = SessionLocal()
    try:
        applications = (
            db.query(ApplicationModel)
            .filter(ApplicationModel.talent_id == talent_id)
            .all()
        )
        return applications
    finally:
        if db:
            db.close()


def search_talents(
    name: Optional[str] = None,
    skills: Optional[list] = None,
    experience_years_min: Optional[int] = None,
    experience_years_max: Optional[int] = None,
    db: Session = None,
):
    if db is None:
        db = SessionLocal()
    try:
        query = db.query(TalentModel)
        if name:
            query = query.filter(TalentModel.name.ilike(f"%{name}%"))
        if skills:
            for skill in skills:
                query = query.filter(TalentModel.skills.contains(skill))
        if experience_years_min is not None:
            query = query.filter(TalentModel.experience_years >= experience_years_min)
        if experience_years_max is not None:
            query = query.filter(TalentModel.experience_years <= experience_years_max)
        talents = query.all()
        return talents
    finally:
        if db:
            db.close()


def create_resume(
    talent_id: str,
    file_path: Optional[str] = None,
    extracted_text: Optional[str] = None,
    analysis_result: Optional[dict] = None,
    db: Session = None,
):
    if db is None:
        db = SessionLocal()
    try:
        new_resume = ResumeModel(
            talent_id=talent_id,
            file_path=file_path,
            extracted_text=extracted_text,
            analysis_result=analysis_result,
        )
        db.add(new_resume)
        db.commit()
        db.refresh(new_resume)
        return new_resume
    finally:
        if db:
            db.close()
