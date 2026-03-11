from fastapi import FastAPI
from .routes.CandidateRoutes import router

app = FastAPI()

app.include_router(router)