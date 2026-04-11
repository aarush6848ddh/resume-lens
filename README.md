# resume-lens

A personal learning project built to get hands-on experience with LangChain and agentic AI workflows. The idea was to build something I'd actually use, a tool that compares a resume PDF against a job description and returns a structured analysis while learning the core LangChain primitives from scratch.

## What it does

Give it a resume PDF and a job posting URL, and it:

1. Scrapes the job description directly from the URL, no copy-pasting
2. Compares your resume against the job description using Gemini
3. Returns a formatted scoring report with:

- **Match score** - a 0–100 rating of how well your resume fits the role
- **Matching skills** - skills you have that the job is looking for
- **Missing skills** - skills the job wants that aren't on your resume
- **Tailoring suggestions** - specific, actionable ways to improve your resume for this role

## Example output

```
Match score: 92
Matching Skills : ['Python', 'Java', 'React', 'Docker', 'PostgreSQL', 'CI/CD', ...]
Missing Skills: ['Ruby', 'Scala', 'Go']
Suggested Fixes: [
  "Quantify impact in your internship with specific metrics...",
  "Explicitly mention code reviews and pull requests...",
  "Add a summary section highlighting learning agility...",
  ...
]
```

## Tech stack

- **Python 3.9**
- **LangChain** - chains, prompt templates, output parsers, tools
- **langchain-google-genai** - Gemini integration via LangChain
- **Google Gemini 2.5 Flash** - the underlying language model
- **pypdf** - PDF text extraction
- **Pydantic** - structured output validation
- **beautifulsoup4** - HTML parsing for the job scraper tool

## Project structure

```
resume-lens/
├── loader.py        # Loads and extracts text from a resume PDF
├── prompt.py        # Defines the ChatPromptTemplate with placeholders
├── model.py         # Initializes the Gemini chat model
├── parser.py        # Pydantic model + output parser for structured results
├── chain.py         # Assembles the LCEL chain and runs the analysis
├── tools.py         # Two LangChain tools: job scraper and report formatter
├── main.py          # Entry point - wires tools and chain together
└── requirements.txt # Python dependencies
```

## LangChain concepts covered

| Concept | Where |
|---|---|
| Document Loaders | `loader.py` - `PyPDFLoader` reads the PDF into `Document` objects |
| Prompt Templates | `prompt.py` - `ChatPromptTemplate` with named placeholders |
| Chat Models | `model.py` - `ChatGoogleGenerativeAI` wraps the Gemini API |
| LCEL chains | `chain.py` - `prompt | model | parser` pipe syntax |
| Output Parsers | `parser.py` - `PydanticOutputParser` returns a typed Python object |
| Pydantic Models | `parser.py` - `ResumeAnalysis` defines the output schema |
| Tools | `tools.py` - `@tool` decorator exposes functions the model can invoke |

## How it works

The full pipeline has two stages: tools and a chain.

```
scrape_job_posting → run_analysis chain → format_scoring_report
```

1. **`tools.py` / `scrape_job_posting`** fetches the job posting URL and extracts the page text using `WebBaseLoader`
2. **`chain.py` / `run_analysis`** runs the LCEL chain - loads the resume PDF, formats the prompt, calls Gemini, and parses the response into a `ResumeAnalysis` Pydantic object
3. **`tools.py` / `format_scoring_report`** takes the structured analysis, serialized as a JSON string, and formats it into a clean human-readable report

### Why tools?

A LangChain chain is a fixed pipeline, it always runs the same steps in the same order. A tool is a callable function exposed to the model so it can decide when to invoke it. This is the foundation of agentic systems like LangGraph, where agents choose which tools to call at runtime based on tool descriptions.
