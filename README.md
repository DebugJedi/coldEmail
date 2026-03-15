# Cold Email Generator

> **AI-powered cold email writer — paste a job URL, upload your resume, get a tailored cold email in seconds.**  
> LangChain · Llama 3.1 70B · Groq · Streamlit · PyPDF2

---

## What This Is

Cold emailing hiring managers is one of the most effective job search strategies — and one of the most time-consuming to do well. This app automates it entirely.

Paste any job posting URL, upload your resume PDF, and the app scrapes the job description, extracts structured role requirements, cross-references your experience, and generates a personalized cold email using **Llama 3.1 70B via Groq's inference API**.

---

## How It Works

```
User pastes job URL + uploads resume PDF
              │
              ▼
┌─────────────────────────┐
│  WebBaseLoader          │  Scrapes full job posting page
│  (LangChain)            │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  LLM extraction chain   │  Llama 3.1 70B via Groq
│  (PromptTemplate +      │  Extracts: role · experience
│   JsonOutputParser)     │  skills · description → JSON
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  PyPDF2                 │  Extracts full text from
│  resume_extract.py      │  uploaded resume PDF
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  Email generation chain │  Llama 3.1 70B via Groq
│  (PromptTemplate)       │  Combines job JSON + resume text
│                         │  → Personalized cold email draft
└────────┬────────────────┘
         │
         ▼
    Streamlit UI displays generated email
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| LLM | Llama 3.1 70B Versatile |
| Inference | Groq API (`langchain-groq`) |
| Orchestration | LangChain (`PromptTemplate`, `JsonOutputParser`) |
| Web scraping | LangChain `WebBaseLoader` |
| PDF parsing | PyPDF2 |
| UI | Streamlit + streamlit-shadcn-ui |
| Secrets management | Streamlit Secrets |

---

## Features

- **Job URL scraping** — paste any job posting URL, the app fetches and parses the full page
- **Structured job extraction** — LLM extracts `role`, `experience`, `skills`, and `description` as clean JSON
- **Resume PDF upload** — drag and drop your resume, text is extracted and passed to the email chain
- **Personalized email generation** — combines your experience with the specific job requirements
- **One-click generation** — single button press runs the full pipeline end to end

---

## Quick Start

### Prerequisites
- Python 3.11+
- [Groq API key](https://console.groq.com) — free tier available

### Installation

```bash
# Clone the repo
git clone https://github.com/DebugJedi/coldEmail.git
cd coldEmail

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Configure secrets

Create `.streamlit/secrets.toml`:

```toml
groq_api_key = "your_groq_api_key"
post_url     = "https://example.com/jobs/your-default-job"
myurl        = "https://your-portfolio-or-linkedin-url"
resume       = "path/to/your/resume.pdf"
ignore       = "words to exclude from email"
comp_ignore  = "company names to exclude"
```

### Run the app

```bash
streamlit run streamlit_email_app.py
# → http://localhost:8501
```

---

## Usage

1. Open the app at `http://localhost:8501`
2. Upload your resume PDF using the file uploader
3. Paste the job posting URL into the text input
4. Click **Submit**
5. Wait ~10 seconds for the full pipeline to run
6. Copy the generated cold email

---

## Project Structure

```
coldEmail/
├── streamlit_email_app.py  ←  Streamlit UI · file upload · job URL input
├── emailGenerator.py       ←  E_generator class · orchestrates full pipeline
├── jobPosting.py           ←  Scrapes job URL · extracts structured JSON via LLM
├── resume_extract.py       ←  PyPDF2 resume text extraction
├── myData.py               ←  Loads personal portfolio/profile data
├── assets/
│   └── style.css           ←  Custom Streamlit styling
├── app/
│   └── resources/photos/   ←  App header image
├── .streamlit/
│   └── secrets.toml        ←  API keys and config (gitignored)
└── requirements.txt
```

---

## Pipeline Design

### Job extraction
`jobPosting.py` uses `WebBaseLoader` to scrape the full job page, then passes it through a LangChain prompt chain instructing Llama 3.1 to return only valid JSON with four keys: `role`, `experience`, `skills`, `description`. `JsonOutputParser` parses the response into a Python dict.

### Resume extraction
`resume_extract.py` uses `PyPDF2` to iterate all pages and concatenate extracted text — handles multi-page resumes cleanly.

### Email generation
`emailGenerator.py` combines the structured job JSON and resume text into a single prompt. The LLM is instructed to write a professional cold email targeting the hiring manager for that specific role, grounded in the candidate's actual experience.

### Privacy controls
Configurable `ignore` and `comp_ignore` fields in secrets allow you to exclude specific names or company references from the generated email — useful when applying from a current employer context.

---

## Roadmap

- [x] Job URL scraping and structured extraction
- [x] Resume PDF upload and text extraction
- [x] LLM-powered personalized email generation
- [x] Privacy controls (name/company exclusions)
- [ ] ChromaDB integration for portfolio/experience vector store
- [ ] Multiple email tone options (formal / casual / aggressive)
- [ ] Export to clipboard / download as `.txt`
- [ ] Support for LinkedIn job URLs
- [ ] Streamlit Cloud deployment

---

## Author

Built and maintained by **Priyank Rao** — Data Scientist / ML Engineer  
[Portfolio](https://priyankrao.co) · [GitHub](https://github.com/DebugJedi)

---

## License

MIT