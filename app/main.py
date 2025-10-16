from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.talent.routers.talent_router import router as talent_router

from .core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="TalentIQ")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(talent_router)


@app.get("/")
async def root():
    return {"message": "Welcome to TalentIQ"}
