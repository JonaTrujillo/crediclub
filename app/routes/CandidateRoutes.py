from fastapi import APIRouter
from app.models.Candidate import Candidate
from app.services import CandidateService
from typing import List
from fastapi import UploadFile
from fastapi import File

router = APIRouter()

#Create candidate
@router.post("/applications")
def createUser(candidates:List[Candidate]):
    return CandidateService.application(candidates)

#Upload File
@router.post("/applications/{id}/documents")
async def uploadCandidateDocument(id:str,document:UploadFile = File(...)):
    return await CandidateService.uploadCandidateDocument(id,document)

#Get candidate score
@router.get("/get/creditscore/{id}")
def getCreditScore(id:str):
    return CandidateService.getCreditScore(id)

#Get candidate status
@router.get("/applications/{id}")
def validateCreditStatus(id:str):
    return CandidateService.validateCreditStatus(id)
    




