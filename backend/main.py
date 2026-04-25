from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class JobInput(BaseModel):
    text: str


bias_terms = {
    "Age Bias": ["young"],
    "Gender Bias": ["salesman", "waitress", "barman"],
    "Nationality Bias": ["native italian", "italian only"],
    "Appearance Bias": ["good looking"]
}


def rewrite_text(text):
    replacements = {
        "young": "motivated",
        "salesman": "sales professional",
        "waitress": "service professional",
        "barman": "bar professional",
        "native italian": "fluent Italian",
        "italian only": "Italian language skills preferred",
        "good looking": "professional"
    }

    new_text = text.lower()

    for old, new in replacements.items():
        new_text = new_text.replace(old, new)

    return new_text.capitalize()


def analyze_bias(text):
    lower = text.lower()
    issues = []

    for category, words in bias_terms.items():
        for word in words:
            if word in lower:
                issues.append({
                    "category": category,
                    "term": word
                })

    score = max(100 - len(issues)*20, 0)

    return {
        "score": score,
        "issues": issues,
        "rewrite": rewrite_text(text)
    }


@app.get("/")
def home():
    return {"message": "TalentOS AI Running"}

@app.post("/fairness")
def fairness(data: JobInput):
    return analyze_bias(data.text)