from chain import run_analysis

job_description = " We are looking for a software engineer with experience in Python, machine learning, and cloud computing. The ideal candidate will have a strong background in data science and be able to work with large datasets. Experience with AWS or GCP is a plus."

result = run_analysis("FALL.pdf", job_description)

print("Match Score:", result.match_score)
print("Matching Skills:", result.matching_skills)
print("Missing Skills:", result.missing_skills)
print("Suggestions for Improvement:", result.suggestions)