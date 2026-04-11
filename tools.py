from langchain_core.tools import tool
from langchain_community.document_loaders import WebBaseLoader
import json

@tool
def scrape_job_posting(url: str):
    """
    Takes a job posting URL and returns the full job description text extracted from the page.
    Use this when the user provides a URL instead of pasting the job description.
    """

    page = WebBaseLoader(url).load()

    result = ""
    for doc in page:
        result = result + doc.page_content
    
    return result


@tool
def format_scoring_report(analysis: str):
    """
    Takes the structures ResumeAnalysis output and formats the content into a clean
    human readable scoring report on how much the resume matches the job description
    based on common skills found in both and also lists what skills the resume is 
    missing. It also provides suggested fixes.
    """

    report = json.loads(analysis)

    format_report = f"Match score: {report['match_score']} \n Matching Skills : {report['matching_skills']} \n Missing Skills: {report['missing_skills']} \n Suggested Fixes: {report['suggestions']}"

    return format_report







    