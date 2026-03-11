from fastapi import FastAPI
from .routes.CandidateRoutes import router
from pathlib import Path

UPLOAD_DIR = Path("app/resources/files")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

app = FastAPI()

app.include_router(router)