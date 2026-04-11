from chain import run_analysis
from tools import scrape_job_posting, format_scoring_report
import json

job_description = scrape_job_posting.invoke({"url": "https://stripe.com/jobs/listing/software-engineer-intern-summer/7210115?gh_src=73vnei"})

result = run_analysis("FALL.pdf", job_description)

report = json.dumps(result.dict())

print(format_scoring_report.invoke({"analysis": report}))