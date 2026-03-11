from app.database import db
from app.models.CandidateDocument import CandidateDocument
from bson import ObjectId

candidateCollection = db.candidate
candidateDocumentCollection = db.candidateDocument

def getCandidateById(id):
    return candidateCollection.find_one({"_id":ObjectId(id)})

def verifyCandidateExists(name,rfc,curp):
    return candidateCollection.find_one({"name":name, "rfc":rfc, "curp":curp})

def application(candidate):
    return candidateCollection.insert_one(candidate)

def uploadCandidateDocument(document):
    data = CandidateDocument (
        userId=document["userId"],
        name=document["name"],
        size=document["size"],
        path=document["path"],
    )
    return candidateDocumentCollection.insert_one(data.model_dump())

def getCandidateScoreById(id):
    return candidateCollection.find_one({"_id":ObjectId(id)},{"score": 1,"name":1})

def updateCandidateStatus(approved,id):
    return candidateCollection.update_one(
        {"_id": ObjectId(id)},
        {"$set": {"status": 2 if approved else 3}}
    )

