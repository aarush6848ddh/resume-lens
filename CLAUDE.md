# resume-lens

A LangChain-based resume analyzer that compares a resume PDF against a job description and returns a structured analysis.

## Project Goal
Given a resume (PDF) and job description (plain text), return:
- Match score out of 100
- Matching skills
- Missing skills
- 2-3 tailoring suggestions

## Stack
- Python 3.11
- LangChain
- Google Gemini 2.5 Flash via `langchain-google-genai`
- PDF loading via `langchain-community` + `pypdf`
- Output parsing via LangChain output parsers
- API key stored in `.env` as `GOOGLE_API_KEY`

## Learning Goals
- LangChain chains
- Prompt templates
- PDF loading and parsing
- Structured output with output parsers

## Dev Setup
```bash
source venv/bin/activate
pip install -r requirements.txt
```
