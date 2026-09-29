# 🤖 NexusScout AI

**An autonomous, full-stack Agentic AI application for real-time competitor intelligence.**

NexusScout AI allows users to track competitors by URL. An asynchronous backend agent autonomously navigates to the website, bypasses bot protections, extracts the content, and uses a Large Language Model (LLM) to generate a strategic business analysis. The insights are persisted in a database and rendered dynamically on a modern Next.js dashboard.

![NexusScout Dashboard](https://via.placeholder.com/800x400.png?text=Add+Screenshot+Here)

## 🚀 Features

- **Autonomous Web Scraping:** Uses Playwright to render JavaScript-heavy sites and bypass basic bot detection.
- **AI-Powered Analysis:** Integrates with Groq's LLM API to generate structured Markdown reports (Value Prop, Pricing, Strategy).
- **Full-Stack Architecture:** Next.js frontend, FastAPI backend, and SQLAlchemy ORM.
- **Persistent Storage:** AI insights are saved to a database and survive page refreshes.
- **Resilient Design:** Handles API deprecations, context window limits, and OS-level async bugs gracefully.

## ️ Tech Stack

- **Frontend:** Next.js (React), TypeScript, Tailwind CSS
- **Backend:** Python, FastAPI, Pydantic, Uvicorn
- **AI & Scraping:** Groq API (Llama 3 / Mixtral), Playwright
- **Database:** SQLite (Local), PostgreSQL (Production-ready via SQLAlchemy)

## 📦 Installation & Setup

### Prerequisites
- Python 3.10+
- Node.js 18+
- A Groq API Key (Get one free at console.groq.com)

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt

# Create .env file and add your key
echo "GROQ_API_KEY=your_key_here" > .env
echo "DATABASE_URL=sqlite:///./nexus_scout.db" >> .env

python -m uvicorn main:app --reload