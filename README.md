# resume-lens

A personal learning project built to get hands-on experience with LangChain and agentic AI workflows. The idea was to build something I'd actually use — a tool that compares a resume PDF against a job description and returns a structured analysis — while learning the core LangChain primitives from scratch.

## What it does

Give it a resume PDF and a job description, and it returns:

- **Match score** — a 0–100 rating of how well your resume fits the role
- **Matching skills** — skills you have that the job is looking for
- **Missing skills** — skills the job wants that aren't on your resume
- **Tailoring suggestions** — specific, actionable ways to improve your resume for this role

## Example output

```
Match Score: 88
Matching Skills: ['Python', 'Machine Learning', 'Cloud Computing', 'Data Science', 'AWS']
Missing Skills: ['GCP', 'Experience with truly large datasets']
Suggestions for Improvement: [
  "Quantify your dataset scale...",
  "Address GCP experience if applicable...",
  ...
]
```

## Tech stack

- **Python 3.11**
- **LangChain** — chains, prompt templates, output parsers
- **langchain-google-genai** — Gemini integration via LangChain
- **Google Gemini 2.0 Flash** — the underlying language model
- **pypdf** — PDF text extraction
- **Pydantic** — structured output validation

## Project structure

```
resume-lens/
├── loader.py        # Loads and extracts text from a resume PDF
├── prompt.py        # Defines the ChatPromptTemplate with placeholders
├── model.py         # Initializes the Gemini chat model
├── parser.py        # Pydantic model + output parser for structured results
├── chain.py         # Assembles the LCEL chain and runs the analysis
├── main.py          # Entry point
└── requirements.txt # Python dependencies
```

## LangChain concepts covered

| Concept | Where |
|---|---|
| Document Loaders | `loader.py` — `PyPDFLoader` reads the PDF into `Document` objects |
| Prompt Templates | `prompt.py` — `ChatPromptTemplate` with named placeholders |
| Chat Models | `model.py` — `ChatGoogleGenerativeAI` wraps the Gemini API |
| LCEL chains | `chain.py` — `prompt | model | parser` pipe syntax |
| Output Parsers | `parser.py` — `PydanticOutputParser` returns a typed Python object |
| Pydantic Models | `parser.py` — `ResumeAnalysis` defines the output schema |

## How it works

The core is a three-step LangChain chain built with LCEL (LangChain Expression Language):

```
prompt | model | parser
```

1. **`loader.py`** extracts all text from the resume PDF using `PyPDFLoader`
2. **`prompt.py`** formats the resume text, job description, and output format instructions into a structured chat prompt
3. **`model.py`** sends the prompt to Gemini and gets a response
4. **`parser.py`** parses Gemini's response into a typed `ResumeAnalysis` Python object using Pydantic

The `|` pipe operator connects each step — the output of one becomes the input of the next, with no glue code required.
