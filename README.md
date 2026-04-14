# resume-lens

A personal learning project built to get hands-on experience with LangChain and agentic AI workflows. The idea was to build something I'd actually use — a tool that compares a resume against a job description and returns a structured analysis while learning core LangChain primitives from scratch.

## What it does

Give it a resume and a job posting URL, and it:

1. Scrapes the job description directly from the URL, no copy-pasting
2. Embeds your resume and the job description into a local vector store
3. Retrieves the most relevant chunks at query time (RAG)
4. Answers questions like:
   - *What machine learning skills does this person have?*
   - *What skills from the job description does this person already have?*
   - *What skills is this person missing for this role?*
   - *Which of their projects is most relevant?*

## Example output

```
Q: What machine learning skills does this person have?
A: This person has experience building machine learning pipelines using PyTorch
   and scikit-learn, implementing transformer components from scratch (self-attention,
   multi-head attention, positional embeddings), and working with RAG and agentic AI systems.

Q: Which of their projects is most relevant to this role?
A: The Software Engineering Intern role at Webster Bank is most relevant — it involved
   writing production code, bug fixes, and adherence to secure coding standards...
```

## Tech stack

- **Python 3.9**
- **LangChain** — chains, prompt templates, output parsers, tools, LCEL
- **langchain-google-genai** — Gemini 2.5 Flash via LangChain
- **Google Gemini 2.5 Flash** — the underlying LLM
- **sentence-transformers** (`all-MiniLM-L6-v2`) — local embeddings, no API key needed
- **Chroma** — local vector store for RAG
- **fitz (PyMuPDF)** — PDF/text extraction
- **Pydantic** — structured output validation
- **beautifulsoup4** — HTML parsing for the job scraper tool

## Project structure

```
resume-lens/
├── loader.py        # Loads resume text (PDF or txt) using fitz
├── prompt.py        # ChatPromptTemplate with placeholders
├── model.py         # Initializes Gemini 2.5 Flash
├── parser.py        # Pydantic model + output parser for structured results
├── chain.py         # LCEL chain: prompt | model | parser
├── tools.py         # Two LangChain tools: job scraper and report formatter
├── main.py          # Entry point — scrapes JD, builds RAG chain, runs queries
├── requirements.txt # Python dependencies
└── rag/
    ├── splitter.py      # RecursiveCharacterTextSplitter (500 tokens, 50 overlap)
    ├── embedder.py      # HuggingFaceEmbeddings with all-MiniLM-L6-v2
    ├── vector_store.py  # Chroma vector store + retriever
    ├── rag_chain.py     # RAG chain: retriever | prompt | model | StrOutputParser
    └── pipeline.py      # build_resume_rag(resume_path, extra_docs) — full entry point
```

## LangChain concepts covered

| Concept | Where |
|---|---|
| Document Loaders | `loader.py` — fitz loads resume into text |
| Prompt Templates | `prompt.py` — `ChatPromptTemplate` with named placeholders |
| Chat Models | `model.py` — `ChatGoogleGenerativeAI` wraps Gemini |
| LCEL chains | `chain.py` — `prompt | model | parser` pipe syntax |
| Output Parsers | `parser.py` — `PydanticOutputParser` returns a typed Python object |
| Pydantic Models | `parser.py` — `ResumeAnalysis` defines the output schema |
| Tools | `tools.py` — `@tool` decorator exposes functions the model can invoke |
| Text Splitting | `rag/splitter.py` — chunks documents for embedding |
| Embeddings | `rag/embedder.py` — sentence-transformers, local 384-dim vectors |
| Vector Stores | `rag/vector_store.py` — Chroma for similarity search |
| Retrievers | `rag/vector_store.py` — `.as_retriever(k=3)` fetches top-K chunks |
| RAG chains | `rag/rag_chain.py` — retrieval-augmented generation pipeline |

## How it works

### RAG pipeline (current)

```
resume + job description
    ↓
chunk with RecursiveCharacterTextSplitter
    ↓
embed with all-MiniLM-L6-v2 → store in Chroma
    ↓
query → retrieve top-3 relevant chunks
    ↓
inject chunks into prompt → Gemini answers
```

### Original scoring pipeline (chain.py)

```
scrape_job_posting → run_analysis chain → format_scoring_report
```

1. **`tools.py` / `scrape_job_posting`** fetches the job posting URL using `WebBaseLoader`
2. **`chain.py` / `run_analysis`** runs the LCEL chain — loads the resume, formats the prompt, calls Gemini, parses into a `ResumeAnalysis` Pydantic object
3. **`tools.py` / `format_scoring_report`** formats the structured analysis into a human-readable report

## Setup

```bash
pip install -r requirements.txt
```

Create a `.env` file:
```
GOOGLE_API_KEY=your_key_here
```

Run:
```bash
python3 main.py
```
