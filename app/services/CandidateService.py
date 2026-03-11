from app.repositories import CandidateRepository
from app.utilities import *
from fastapi import HTTPException
import shutil
from datetime import datetime


def application(candidates):
    #data = [candidate.model_dump() for candidate in candidates]
    dataEvaluated = []
    for candidate in candidates:
        candidateExists = CandidateRepository.verifyCandidateExists(candidate.name,candidate.rfc,candidate.curp)
        if candidateExists:
            dataEvaluated.append({
                "name": candidate.name,
                "message": "This candidate is already registered"
            })
        else:
            CandidateRepository.application(candidate.model_dump())
            dataEvaluated.append({
                "name": candidate.name,
                "message": "Candidate registered correctly"
            })
    return dataEvaluated
    # insertedRecords = CandidateRepository.application(data)
    # return {"message": f"Total of record saved: {len(insertedRecords.inserted_ids)}" }

async def uploadCandidateDocument(id,document):
    candidateDocument = {}
    if parseToMb(document.size) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400,detail="The document must be less than 5MB")
    
    if document.content_type not in VALID_DOCUMENT_TYPES:
        raise HTTPException(status_code=400,detail="Only PDF or images files are allowed")
    
    candidateExists =  CandidateRepository.getCandidateById(id)
    if not candidateExists:
        raise HTTPException(status_code=400,detail="User not found")
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fileName = f"{timestamp}_{document.filename}"
    filePath = UPLOAD_DIR / fileName
    try:
        candidateDocument["userId"] = id
        candidateDocument["name"] = fileName
        candidateDocument["size"] = document.size
        candidateDocument['path'] = str(filePath)
        insertedRecord =  CandidateRepository.uploadCandidateDocument(candidateDocument)

        with open(filePath, "wb") as buffer:
            shutil.copyfileobj(document.file,buffer)
    except Exception as e:
        raise HTTPException(status_code=500,detail="Something wrong with the file")
    finally:
        await document.close()
    return {"filename": document.filename, "content_type": document.content_type, "patidh": str(filePath), "id": str(insertedRecord.inserted_id)}

def getCreditScore(id):
    candidateScore =  CandidateRepository.getCandidateScoreById(id)
    if not candidateScore:
        raise HTTPException(status_code=400,detail="User not found")
    candidateScore["_id"] = str(candidateScore["_id"])
    return candidateScore

def validateCreditStatus(id):
    candidate = CandidateRepository.getCandidateById(id)

    if not candidate:
        raise HTTPException(status_code=400,detail="User not found") 
    
    results = [
        amountValue(candidate['amountRequested']),
        scoreRule(candidate['score']),
        ageRule(candidate['age']),
        experienceRule(candidate['yearExperience']),
        incomeGenderRule(candidate['income'],candidate['amountRequested'],candidate['gender'])
    ]
    approved = all(r["approved"] for r in results)
    reasons = [r["reason"] for r in results if r["reason"]]

    return {
        "name": candidate['name'],
        "credit_tatus": "Approved" if approved else "Rejected",
        "reasons": "The credit has been accepted" if approved else reasons
    }
    