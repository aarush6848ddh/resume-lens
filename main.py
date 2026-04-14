from rag.pipeline import build_resume_rag
from tools import scrape_job_posting
from langchain.schema import Document

RESUME = "FALL.txt"
JOB_URL = "https://stripe.com/jobs/listing/software-engineer-intern-summer/7210115?gh_src=73vnei"

print("Scraping job posting...")
job_description = scrape_job_posting.invoke({"url": JOB_URL})

print("Building RAG pipeline...")
chain = build_resume_rag(RESUME, extra_docs=[Document(page_content=job_description, metadata={"source": "job_description"})])

questions = [
    "What machine learning skills does this person have?",
    "What skills from the job description does this person already have?",
    "What skills is this person missing for this job?",
    "Which of their projects is most relevant to this role?",
]

for q in questions:
    print(f"\nQ: {q}")
    print(f"A: {chain.invoke(q)}")
