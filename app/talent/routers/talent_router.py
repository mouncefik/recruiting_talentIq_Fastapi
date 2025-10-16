from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.talent.schemas.talent import (
    Resume,
    ResumeCreate,
    SearchTalent,
    Talent,
    TalentUpdate,
)
from app.talent.services.talents_service import (
    create_resume,
    get_applications_for_talent,
    get_resumes_for_talent,
    get_talent_by_id,
    search_talents,
    update_talent,
)

router = APIRouter()


@router.get("/talents/{id}/resume", response_model=List[Resume])
def get_talent_resumes(id: str, db: Session = Depends(get_db)):
    resumes = get_resumes_for_talent(id, db)
    return resumes


@router.post("/talents/{id}/resume", response_model=Resume)
def upload_talent_resume(
    id: str, resume_data: ResumeCreate, db: Session = Depends(get_db)
):
    # Check if talent exists
    talent = get_talent_by_id(id, db)
    if not talent:
        raise HTTPException(status_code=404, detail="Talent not found")
    new_resume = create_resume(
        talent_id=id,
        file_path=resume_data.file_path,
        extracted_text=resume_data.extracted_text,
        analysis_result=resume_data.analysis_result,
        db=db,
    )
    return new_resume


@router.put("/talents/{id}", response_model=Talent)
def update_talent_info(
    id: str, talent_data: TalentUpdate, db: Session = Depends(get_db)
):
    updated_talent = update_talent(
        talent_id=id,
        name=talent_data.name,
        email=talent_data.email,
        phone=talent_data.phone,
        skills=talent_data.skills,
        experience_years=talent_data.experience_years,
        db=db,
    )
    if not updated_talent:
        raise HTTPException(status_code=404, detail="Talent not found")
    return updated_talent


@router.get("/talents/{id}/applications")
def get_talent_applications(id: str, db: Session = Depends(get_db)):
    applications = get_applications_for_talent(id, db)
    return applications


@router.get("/talents/search", response_model=List[Talent])
def search_talents_endpoint(
    search_params: SearchTalent = Depends(), db: Session = Depends(get_db)
):
    talents = search_talents(
        name=search_params.name,
        skills=search_params.skills,
        experience_years_min=search_params.experience_years_min,
        experience_years_max=search_params.experience_years_max,
        db=db,
    )
    return talents
