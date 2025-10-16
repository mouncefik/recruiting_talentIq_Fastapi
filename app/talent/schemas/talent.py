from typing import List, Optional

from pydantic import BaseModel


class TalentBase(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    skills: Optional[List[str]] = None
    experience_years: Optional[int] = None


class TalentCreate(TalentBase):
    pass


class TalentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    skills: Optional[List[str]] = None
    experience_years: Optional[int] = None


class SearchTalent(BaseModel):
    name: Optional[str] = None
    skills: Optional[List[str]] = None
    experience_years_min: Optional[int] = None
    experience_years_max: Optional[int] = None


class Talent(TalentBase):
    id: str
    created_at: str
    updated_at: str


class ResumeBase(BaseModel):
    file_path: Optional[str] = None
    extracted_text: Optional[str] = None
    analysis_result: Optional[dict] = None


class ResumeCreate(ResumeBase):
    talent_id: str


class Resume(ResumeBase):
    id: str
    talent_id: str
    created_at: str
