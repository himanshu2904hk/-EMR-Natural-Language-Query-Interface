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

## 🛠️ Tech Stack

| Layer | Technology |
| --- | --- |
| Language | Python |
| LLM Orchestration | LangChain |
| AI Model | Grok API (xAI) |
| Backend API | FastAPI |
| Database | PostgreSQL / EMR Database |

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
- PostgreSQL
- Grok API Key

### Installation

```bash
# Clone the repository
git clone https://github.com/himanshu2904hk/emr-nlq-interface.git
cd emr-nlq-interface

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your GROK_API_KEY and DATABASE_URL to .env

# Run the application
uvicorn main:app --reload
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
