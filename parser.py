from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

class ResumeAnalysis(BaseModel):
    match_score: int = Field(..., description="A score from 0 to 100 indicating how well the resume matches the job description.")
    matching_skills: list[str] = Field(..., description="A list of matching skills between the resume and job description.")
    missing_skills: list[str] = Field(..., description="A list of missing skills that are in the job description but not in the resume.")
    suggestions: list[str] = Field(..., description="Specific suggestions for improving the resume.") 

def get_parser():
    return PydanticOutputParser(pydantic_object=ResumeAnalysis)