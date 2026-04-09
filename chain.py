from loader import load_pdf
from prompt import build_prompt
from model import get_model
from parser import get_parser

def run_analysis(resume_path, job_description):
    # Load the resume text from the PDF
    resume_text = load_pdf(resume_path)
    
    # Build the prompt for the language model
    prompt = build_prompt()
    
    # Get the language model
    model = get_model()
    
    # Get the output parser
    parser = get_parser()
    
    chain = prompt | model | parser

    # Run the chain with the resume and job description
    return chain.invoke({
        "resume": resume_text,
        "job_description": job_description,
        "format_instructions": parser.get_format_instructions()
    })