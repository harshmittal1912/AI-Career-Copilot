import json
import os
import re

from dotenv import load_dotenv
from google import genai
from google.genai.types import GenerateContentConfig

load_dotenv()

PROMPT = """
You are an expert ATS (Applicant Tracking System) and resume coach.

Analyze the resume against the job description.

Return ONLY valid JSON.

{{
    "ats_score": 0,
    "score_reason": "",
    "matched_keywords": [],
    "missing_keywords": [],
    "weak_bullets": [],
    "improved_bullets": [],
    "top_feedback": []
}}

Rules:
- ats_score must be between 0 and 100.
- matched_keywords: max 15
- missing_keywords: max 15
- weak_bullets: 2-4 bullets
- improved_bullets: same count as weak_bullets
- top_feedback: exactly 3 items.

Resume:

{resume}

Job Description:

{jd}
"""


def _client():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY not found. Add it to backend/.env"
        )

    return genai.Client(api_key=api_key)


def _extract_json(text: str):
    text = text.strip()

    m = re.search(r"```json(.*?)```", text, re.DOTALL)

    if m:
        text = m.group(1).strip()

    return json.loads(text)


def analyze_resume(resume_text: str, job_description: str):

    if not job_description.strip():
        raise ValueError("Job description cannot be empty.")

    prompt = PROMPT.format(
        resume=resume_text[:12000],
        jd=job_description[:8000],
    )

    client = _client()

    print("========== GEMINI REQUEST ==========")

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
        config=GenerateContentConfig(
            temperature=0.2,
            response_mime_type="application/json",
        ),
    )

    print("========== GEMINI RESPONSE ==========")
    print(response.text)
    print("====================================")

    if not response.text:
        raise RuntimeError("Gemini returned an empty response.")

    data = _extract_json(response.text)

    required = [
        "ats_score",
        "score_reason",
        "matched_keywords",
        "missing_keywords",
        "weak_bullets",
        "improved_bullets",
        "top_feedback",
    ]

    for key in required:
        if key not in data:
            raise RuntimeError(f"Missing key: {key}")

    data["ats_score"] = max(
        0,
        min(100, int(data["ats_score"]))
    )

    return data