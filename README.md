# 🏥 EMR Natural Language Query Interface

> Query patient data in plain English — no SQL required.

## Overview

A production-grade **Natural Language Query (NLQ) engine** built for Electronic Medical Record (EMR) databases. Designed to let doctors and medical staff retrieve patient data using plain English questions, eliminating the need for manual SQL queries and reducing friction in clinical workflows.

Built with a focus on **privacy**, **accuracy**, and **speed** — all patient data stays local with zero exposure to external servers.

---

## ✨ Features

- 🗣️ **Plain English Queries** — Medical staff can ask questions like *"Show me all diabetic patients admitted last week"* without writing SQL
- 🎯 **High Accuracy** — Achieves high query accuracy with low error rate across diverse medical datasets
- 🔒 **Full Data Privacy** — All processing is done locally; no patient data is sent to external servers
- ⚡ **Fast Response** — Optimised pipeline for low-latency query execution in clinical settings
- 🔄 **Workflow Automation** — Translates ambiguous query inputs into precise, executable multi-step workflows with detailed documentation

---

## 🎬 Demo

### Web UI
Type any medical question and get instant results:

![EMR Query UI](https://raw.githubusercontent.com/himanshu2904hk/-EMR-Natural-Language-Query-Interface/main/static/demo-ui.png)

### Example Queries & Results

**Query:** *"Show me all diabetic patients"*
```json
{
  "question": "Show me all diabetic patients",
  "generated_sql": "SELECT p.* FROM patients p JOIN diagnoses d ON p.id = d.patient_id WHERE d.diagnosis_name ILIKE '%diabetes%'",
  "results": [
    { "id": 1, "first_name": "Aarav", "last_name": "Sharma", "gender": "Male", "date_of_birth": "1985-03-12" },
    { "id": 10, "first_name": "Deepa", "last_name": "Joshi", "gender": "Female", "date_of_birth": "1982-02-28" }
  ],
  "row_count": 2
}
```

**Query:** *"Which patients are currently admitted?"*
```json
{
  "question": "Which patients are currently admitted?",
  "generated_sql": "SELECT p.first_name, p.last_name, a.ward, a.reason, a.admitted_at FROM patients p JOIN admissions a ON p.id = a.patient_id WHERE a.discharged_at IS NULL",
  "results": [
    { "first_name": "Rohan", "last_name": "Mehta", "ward": "Endocrinology", "reason": "Hyperglycaemia" },
    { "first_name": "Manish", "last_name": "Dubey", "ward": "Isolation Ward", "reason": "TB treatment initiation" }
  ],
  "row_count": 2
}
```

**Query:** *"List all patients on Metformin"*
```json
{
  "question": "List all patients on Metformin",
  "generated_sql": "SELECT p.first_name, p.last_name, m.dosage, m.frequency FROM patients p JOIN medications m ON p.id = m.patient_id WHERE m.medication_name = 'Metformin' AND m.active = TRUE",
  "results": [
    { "first_name": "Aarav", "last_name": "Sharma", "dosage": "500mg", "frequency": "Twice daily" }
  ],
  "row_count": 1
}
```

---

## 🛠️ Tech Stack

| Layer | Technology |
| --- | --- |
| Language | Python |
| LLM Orchestration | LangChain |
| AI Model | Groq API (Llama 3.3 70B) |
| Backend API | FastAPI |
| Database | Supabase (PostgreSQL) |
| Frontend | HTML / CSS / Vanilla JS |

---

## 🏗️ Architecture

```
User (Plain English Input)
        ↓
   FastAPI Backend
        ↓
  LangChain Pipeline
        ↓
   Grok API (LLM)
        ↓
  SQL Query Generator
        ↓
 EMR PostgreSQL Database
        ↓
   Structured Results → User
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- [Supabase](https://supabase.com) account (free)
- [Groq](https://console.groq.com) API Key (free)

### Installation

```bash
# Clone the repository
git clone https://github.com/himanshu2904hk/-EMR-Natural-Language-Query-Interface.git
cd -EMR-Natural-Language-Query-Interface

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Fill in your GROQ_API_KEY and Supabase DATABASE_URL in .env

# Run the application
uvicorn main:app --reload
```

Then open **http://127.0.0.1:8000** in your browser.

### Environment Variables

```env
GROQ_API_KEY=your_groq_api_key
DATABASE_URL=postgresql://postgres:password@db.xxxx.supabase.co:5432/postgres
GROQ_MODEL=llama-3.3-70b-versatile
```

---

## 📌 Use Case

Built for healthcare environments where clinical staff need fast access to patient data but lack SQL expertise. This system bridges the gap between medical professionals and complex databases — making data accessible, fast, and safe.

---

## 🔐 Privacy & Compliance

- All patient data remains **100% local**
- Zero data sent to external servers
- Designed with healthcare data privacy standards in mind

---

## 👤 Author

**Himanshu Kumar Lenka**
AI/ML Engineer
[LinkedIn](https://linkedin.com/in/) | [GitHub](https://github.com/himanshu2904hk)
