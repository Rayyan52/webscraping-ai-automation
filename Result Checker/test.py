import os
import time
import smtplib
import requests
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from dotenv import load_dotenv
from urllib.parse import urljoin

from groq import Groq
import instructor
from pydantic import BaseModel, Field
from typing import List

# ---------------- ENV ----------------
load_dotenv()

BASE_URL = "https://www.neduet.edu.pk"
URL = "https://www.neduet.edu.pk/examination_results"

SENDER_EMAIL = "-"
APP_PASSWORD = "-"

# ---------------- ROLL → EMAIL MAP ----------------
ROLL_EMAIL_MAP = {
    "SE-22051": "-",
    "SE-22052": "-"
}
# ---------------- GROQ + INSTRUCTOR ----------------
client = Groq(api_key=os.getenv("GROQ_API"))
client = instructor.from_groq(client)

# ---------------- PYDANTIC MODELS ----------------
class Student(BaseModel):
    roll_no: str = Field(description="Seat number e.g. SE-23051")
    gpa: float = Field(description="GPA mentioned in brackets")


class ResultSheet(BaseModel):
    students: List[Student]

# ---------------- PROMPT ----------------
PROMPT = """
You are given an image of an official university examination result notification.

TASK:
- Read ONLY the table titled:
  'Candidates who obtained passing grade in all courses of the semester : Seat Number (GPA)'
- Extract each seat number and its GPA.

RULES:
- Ignore all other sections.
- Preserve roll number formatting exactly.
- GPA must be a float.
- Skip unclear or missing values.
"""

# ---------------- DOWNLOAD IMAGE (ONLY AFTER VIEW) ----------------
def download_result_image():
    response = requests.get(URL, timeout=15)
    soup = BeautifulSoup(response.text, "html.parser")

    for row in soup.find_all("tr"):
        cols = row.find_all("td")
        if not cols:
            continue

        # 🔒 COLUMN LOGIC — UNCHANGED
        if cols[0].get_text(strip=True) == "Software Engg.":
            third_entry = cols[4].get_text(strip=True)

            if third_entry.lower() != "view":
                return None

            # Get the SAME View link
            link = cols[4].find("a")
            if not link:
                return None

            

            img_url = urljoin(BASE_URL, link["href"])
            img_data = requests.get(img_url, timeout=15).content

            with open("result.jpg", "wb") as f:
                f.write(img_data)

            print("✅ Result image downloaded")
            return "result.jpg"

    return None

# ---------------- EMAIL FUNCTION ----------------
def send_result_emails(result_sheet):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, APP_PASSWORD)

        for student in result_sheet.students:
            recipient = ROLL_EMAIL_MAP.get(student.roll_no)
            if not recipient:
                continue

            body = f"""
Hello {student.roll_no},

Your semester result has been announced.

GPA: {student.gpa}
Student ID: {student.roll_no}

You ARE COOKED! HEHE

Official link:
{URL}
"""

            msg = MIMEText(body)
            msg["Subject"] = "🎓 Semester Result Announced"
            msg["From"] = SENDER_EMAIL
            msg["To"] = recipient

            server.send_message(msg)
            print(f"📧 Email sent to {student.roll_no} → {recipient}")

# ---------------- MAIN LOOP ----------------
while True:
    image_path = download_result_image()

    if image_path:
        image = instructor.Image.from_path(image_path)

        result = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {
                    "role": "user",
                    "content": [PROMPT, image],
                }
            ],
            response_model=ResultSheet,
            strict=True,
            temperature=0.0,
        )

        print(result.model_dump_json(indent=2))
        send_result_emails(result)
        break

    print("⏳ Results not announced yet...")
    break