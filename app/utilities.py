from pathlib import Path

UPLOAD_DIR = Path("app/resources/files")
MAX_FILE_SIZE = 5
VALID_DOCUMENT_TYPES = [
    "application/pdf",
    "image/jpeg",
    "image/png"
]
MIN_AMOUNT = 20000
MAX_AMOUNT = 80000
SCORE_UP_RULE = 900
SCORE_DOWN_RULE = 500
MIN_AGE = 20
MAX_AGE = 60
REQUESTED_AMOUNT = 40000
MIN_INCOME_MALE_UP_REQUESTED = 25000
MIN_INCOME_FEMALE_UP_REQUESTED = 20000
MIN_INCOME_MALE_DOWN_REQUESTED = 15000
MIN_INCOME_FEMALE_DOWN_REQUESTED = 10000
YEARS_EXPERIENCE = 5
def parseToMb(size):
    return size / (1024 * 1024)

def amountValue(amount):
    return {"approved": amount >= MIN_AMOUNT and amount <= MAX_AMOUNT,
            "reason": None if amount >= MIN_AMOUNT and amount <= MAX_AMOUNT
            else f"The requested amount must be between {MIN_AMOUNT} and {MAX_AMOUNT}"

    }
    
def scoreRule(score):
    return {"approved": score >= SCORE_DOWN_RULE and score <= SCORE_UP_RULE,
            "reason": None if score >= SCORE_DOWN_RULE and score <= SCORE_UP_RULE else f"The score must be between {SCORE_DOWN_RULE} and {SCORE_UP_RULE}"

    }
    
def ageRule(age):
    return{"approved": age >= MIN_AGE and age <= MAX_AGE,
           "reason": None if age >= MIN_AGE and age <= MAX_AGE else f"The age must be between {MIN_AGE} and {MAX_AGE}"
    } 

def experienceRule(years):
    return {"approved": years >= YEARS_EXPERIENCE,
            "reason": None if years >= YEARS_EXPERIENCE 
            else f"The years of experience must be more than {YEARS_EXPERIENCE}"
    }

def incomeGenderRule(income,amount,gender):
    if amount > REQUESTED_AMOUNT:
        match gender:
            case "Masculino":
                return {"approved": income >= MIN_INCOME_MALE_UP_REQUESTED,
                        "reason": None if income >= MIN_INCOME_MALE_UP_REQUESTED
                        else f"The income must be greather than {MIN_INCOME_MALE_UP_REQUESTED}"
                }
            case "Femenino":
                return {"approved": income >= MIN_INCOME_FEMALE_UP_REQUESTED,
                        "reason": None if income >= MIN_INCOME_FEMALE_UP_REQUESTED
                        else f"The income must be greather than {MIN_INCOME_FEMALE_UP_REQUESTED}"
                }
    else:
        match gender:
            case "Masculino":
                return {"approved": income >= MIN_INCOME_MALE_DOWN_REQUESTED,
                        "reason": None if income >= MIN_INCOME_MALE_DOWN_REQUESTED
                        else f"The income must be greather than {MIN_INCOME_MALE_DOWN_REQUESTED}"
                }
            case "Femenino":
                return {"approved": income >= MIN_INCOME_FEMALE_DOWN_REQUESTED,
                        "reason": None if income >= MIN_INCOME_FEMALE_DOWN_REQUESTED
                        else f"The income must be greather than {MIN_INCOME_FEMALE_DOWN_REQUESTED}"
                }
        

