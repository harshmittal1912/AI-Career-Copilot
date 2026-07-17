# AI Resume Analyzer & ATS Score Checker

A web app that uses **Google Gemini 3.5 Flash** to analyze a student's resume against a job description, calculate an **ATS compatibility score**, identify **skill gaps**, and generate **improved bullet points**.

## Architecture

                    +----------------+
                    | React (Vite)   |
                    +-------+--------+
                            |
                     HTTP REST API
                            |
                            v
                    +----------------+
                    | FastAPI Backend|
                    +-------+--------+
                            |
          +-----------------+-----------------+
          |                                   |
          v                                   v
    pdfplumber                      Google Gemini 3.5 Flash
 (Resume Extraction)                 AI Resume Analysis


## Tech Stack

| Layer | Stack |
|-------|-------|
| Frontend | React, Vite, Tailwind CSS |
| Backend | FastAPI, pdfplumber |
| AI | Google Gemini 3.5 Flash (google-genai SDK) |
| Language | Python, JavaScript |

## Features
- Upload PDF resumes
- ATS compatibility scoring
- AI-powered resume analysis
- Skill gap identification
- Matched and missing keyword detection
- Resume improvement suggestions
- Weak bullet point identification
- Improved bullet point generation
- REST API using FastAPI
- Responsive React frontend

## Recent Improvements

- Migrated from deprecated `google-generativeai` SDK to the latest `google-genai` SDK.
- Updated Gemini integration to support Gemini 3.5 Flash.
- Improved JSON parsing and prompt handling.
- Enhanced backend stability and error handling.


## Quick Start (Local)

### 1. Install Python
Download from https://www.python.org/downloads/ (check “Add to PATH”), then restart the terminal.

### 2. Get a Gemini API key

1. Go to [Google AI Studio](https://aistudio.google.com/apikey)
2. Create an API key

### 3. Backend

```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
copy .env.example .env
# Edit .env and set GEMINI_API_KEY=your_key

uvicorn main:app --reload --port 8000
```

Health check: http://localhost:8000/health

### 4. Frontend

```bash
cd frontend
npm install
copy .env.example .env
# VITE_API_URL=http://localhost:8000 (default)

npm run dev
```

Open http://localhost:5173

## API

### `GET /health`

```json
{ "status": "ok", "service": "resume-analyzer" }
```

### `POST /analyze`

| Field             | Type   | Description        |
| ----------------- | ------ | ------------------ |
| `file`            | PDF    | Resume file        |
| `job_description` | string | Full JD text       |

**Response:**

```json
{
  "success": true,
  "data": {
    "ats_score": 72,
    "score_reason": "...",
    "matched_keywords": [],
    "missing_keywords": [],
    "weak_bullets": [],
    "improved_bullets": [],
    "top_feedback": []
  }
}
```


### Future Updates

Whenever you make changes:

```bash
git add .
git commit -m "Describe your changes"
git push
```

## Deploy (Free Tier)

### Backend — [Render.com](https://render.com)

1. Push this repo to GitHub
2. New **Web Service** → connect repo
3. **Root directory:** `backend`
4. **Build command:** `pip install -r requirements.txt`
5. **Start command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. **Environment:** `GEMINI_API_KEY`, `ALLOWED_ORIGINS=https://your-app.vercel.app`

### Frontend — [Vercel](https://vercel.com)

1. Import repo → set **Root Directory** to `frontend`
2. **Environment variable:** `VITE_API_URL=https://your-backend.onrender.com`
3. Deploy

## Live Demo

**Try the application here:**

https://ai-resume-analyzer-frontend-plum.vercel.app/

⚠️ Free Render services spin down after 15 mins of inactivity. First request after sleep takes ~30 seconds. Add a note on your site: "First analysis may take 30s to wake up." Upgrade to paid ($7/mo) when you start earning.

---

## Testing Tips

- Use text-based PDFs (not scanned images)
- Paste full JDs from Naukri/LinkedIn for best keyword matching
- Try 5 different resume + JD pairs and screenshot strong results for your portfolio

## Project Structure

```
backend/
│
├── main.py
├── ai_service.py
├── pdf_extractor.py
├── requirements.txt
├── .env.example
│
frontend/
│
├── src/
├── public/
├── package.json
│
README.md
```

## Environment Variables

### Backend (`backend/.env`)

Create a `.env` file inside the `backend` directory and add the following:

```env
GEMINI_API_KEY=your_gemini_api_key
ALLOWED_ORIGINS=http://localhost:5173
```

### Frontend (`frontend/.env`)

Create a `.env` file inside the `frontend` directory and add the following:

```env
VITE_API_URL=http://localhost:8000
```

> **Production Deployment**
>
> Update these values after deployment:
>
> - `ALLOWED_ORIGINS=https://your-frontend.vercel.app`
> - `VITE_API_URL=https://your-backend.onrender.com`

## Resume Analysis Includes

- ATS Score (0–100)
- Skill Match Analysis
- Missing Skills
- Resume Strengths
- Resume Weaknesses
- AI Feedback
- Resume Bullet Improvements


## Future Enhancements

- Resume PDF report generation
- AI Cover Letter Generator
- AI Interview Question Generator
- Resume Version History
- Authentication
- User Dashboard

## License

MIT — use freely for learning and portfolio projects.
