from pydantic import BaseModel


class JobInput(BaseModel):
    text: str

class MatchInput(BaseModel):
    job_description: str
    resumes: list[str]