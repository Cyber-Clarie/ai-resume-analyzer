import re
k
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from pypdf import PdfReader

app = FastAPI(title="AI Resume Analyzer API")

STOP_WORDS = {
    "and", "the", "for", "with", "from", "that", "this", "your",
    "you", "are", "our", "will", "have", "has", "but", "not",
    "job", "role", "work", "working", "experience", "skills",
    "years", "year", "team", "company", "candidate", "required",
    "preferred", "ability", "knowledge", "strong"
}


def extract_keywords(text: str) -> set[str]:
    words = re.findall(r"\b[a-zA-Z+#.]{3,}\b", text.lower())
    return {word for word in words if word not in STOP_WORDS}


@app.get("/")
def home():
    return {"message": "AI Resume Analyzer API is running!"}


@app.post("/analyze-resume")
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF resume files are supported.")

    try:
        reader = PdfReader(file.file)
        resume_text = ""
        for page in reader.pages:
            resume_text += page.extract_text() or ""
    except Exception:
        raise HTTPException(status_code=400, detail="The uploaded PDF could not be read.")

    if not resume_text.strip():
        raise HTTPException(status_code=400, detail="No readable text was found in this PDF.")

    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_description)
    matched_keywords = sorted(resume_keywords & job_keywords)
    missing_keywords = sorted(job_keywords - resume_keywords)
    match_score = round((len(matched_keywords) / len(job_keywords)) * 100, 1) if job_keywords else 0

    return {
        "filename": file.filename,
        "match_score": f"{match_score}%",
        "matched_keywords": matched_keywords,
        "missing_keywords": missing_keywords,
        "resume_preview": resume_text[:500]
    }
