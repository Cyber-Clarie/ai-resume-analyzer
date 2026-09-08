# 🤖 AI Resume Analyzer

> A FastAPI-powered **resume parser and job description matcher** that extracts text from PDF resumes and identifies relevant skills through keyword analysis.

## ✨ Features

- 📄 Upload and validate PDF resumes
- 🔎 Extract readable text with **PyPDF**
- 🎯 Compare resumes against a job description
- 📊 Calculate a keyword match score
- ✅ Show matched keywords and missing keywords
- 🛡️ Return clear errors for invalid or unreadable files
- 📚 Explore and test the API through built-in Swagger documentation

## 🛠️ Tech Stack

- **Python**
- **FastAPI**
- **Uvicorn**
- **PyPDF**
- **REST API**

## 🚀 Getting Started

### 1. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install fastapi uvicorn python-multipart pypdf
```

### 3. Run the application

```bash
uvicorn main:app --reload
```

Open the interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

## 📌 API Endpoint

### `POST /analyze-resume`

Send:

- A **PDF resume**
- A **job description**

The API returns the filename, resume preview, match score, matched keywords, and missing keywords.

## ⚙️ How It Works

1. The API validates that the uploaded resume is a PDF.
2. PyPDF extracts text from each page.
3. The application identifies meaningful keywords in the resume and job description.
4. It compares both keyword sets and returns a match score with practical insights.

## 🔮 Future Improvements

- 🧠 AI-powered semantic matching
- 🖥️ Web interface for non-technical users
- 📈 Resume improvement suggestions
- ☁️ Cloud deployment

## 👤 Author

Built by [Cyber-Clarie](https://github.com/Cyber-Clarie)
