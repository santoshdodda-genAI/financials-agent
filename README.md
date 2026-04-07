# 🚀 Financial Insights Agent

A production-ready **GenAI-powered financial analysis API** built using FastAPI, Google ADK, and Gemini (Vertex AI), deployed on Cloud Run.

---

## 🌐 Live API

**Base URL:**

```
https://financials-agent-289062580192.us-central1.run.app
```

---

## 📌 Endpoints

### 🔍 Health Check

```
GET /health
```

**Response:**

```json
{"status": "ok"}
```

---

### 📊 Analyze Financial Text

```
POST /analyze
```

**Request Body:**

```json
{
  "text": "ITC reports strong growth in FMCG segment"
}
```

**Response:**

```
Sentiment: Bullish
Summary: ITC has reported significant growth within its FMCG segment. This indicates positive momentum and a strong outlook for the business.
```

---

## 🧠 Architecture

```
Client → Cloud Run → FastAPI → Google ADK → Gemini (Vertex AI)
```

---

## ⚙️ Tech Stack

* **Backend:** FastAPI
* **AI Framework:** Google ADK
* **LLM:** Gemini (via Vertex AI)
* **Deployment:** Cloud Run
* **Containerization:** Docker

---

## 📁 Project Structure

```
financials-agent/
│
├── main.py              # FastAPI entry point
├── agent.py             # ADK agent + runner logic
├── config.py            # Environment configuration
├── requirements.txt     # Python dependencies
├── Dockerfile           # Container setup
└── .env                 # Environment variables (not committed)
```

---

## 🐳 Running Locally

### 1. Clone the repo

```
git clone https://github.com/santoshdodda-genAI/financials-agent.git
cd financials-agent
```

### 2. Create virtual environment

```
python3.12 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the server

```
uvicorn main:app --host 0.0.0.0 --port 8080
```

---

## ☁️ Deployment (Cloud Run)

### Build container

```
gcloud builds submit --tag gcr.io/project-financial-agent/financials-agent
```

### Deploy

```
gcloud run deploy financials-agent \
--image gcr.io/project-financial-agent/financials-agent \
--platform managed \
--region us-central1 \
--allow-unauthenticated \
--set-env-vars GOOGLE_GENAI_USE_VERTEXAI=1,GOOGLE_CLOUD_PROJECT=project-financial-agent,GOOGLE_CLOUD_LOCATION=us-central1,MODEL=gemini-2.5-flash
```

---

## 🔐 Environment Variables

Create a `.env` file (do NOT commit):

```
GOOGLE_GENAI_USE_VERTEXAI=1
GOOGLE_CLOUD_PROJECT=project-financial-agent
GOOGLE_CLOUD_LOCATION=us-central1
MODEL=gemini-2.5-flash
```

---

## ✅ Features

* Sentiment classification (Bullish / Bearish / Neutral)
* 2-line financial summary generation
* Stateless API using ADK Runner
* Production deployment with Cloud Run
* Scalable and serverless architecture

---

## 🏁 Future Improvements

* Add authentication (secure API)
* Add logging & monitoring
* UI dashboard (Streamlit / React)
* Multi-agent workflows
* Database integration for history

---

## 👤 Author

**Santosh Dodda**

---

## 💡 Summary

This project demonstrates how to build and deploy a **production-grade GenAI microservice**, integrating FastAPI, Google ADK, and Vertex AI with scalable infrastructure using Cloud Run.
