import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import time

URL = "https://www.neduet.edu.pk/examination_results"  # replace this

SENDER_EMAIL = "-"
APP_PASSWORD = "-"  # replace this

RECEIVER_EMAILS = [
    "-",
    "-",
    "-",
    "-",
    "-"
    "-"
    "-"
    "-"
    "-"
    "-"
]

def send_email():
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, APP_PASSWORD)
        
        for recipient in RECEIVER_EMAILS:
            msg = MIMEText("Software Engineering results are now AVAILABLE! check the link https://www.neduet.edu.pk/examination_results")
            msg["Subject"] = "🎉 Result Announced"
            msg["From"] = SENDER_EMAIL
            msg["To"] = recipient  # Only this recipient sees their email

            server.send_message(msg)
            print(f"📧 Email sent to {recipient}!")

def check_results():
    response = requests.get(URL, timeout=15)
    soup = BeautifulSoup(response.text, "html.parser")

    for row in soup.find_all("tr"):
        cols = row.find_all("td")
        if not cols:
            continue

        if cols[0].get_text(strip=True) == "Software Engg.":
            third_entry = cols[3].get_text(strip=True)
            return third_entry.lower() == "view"

    return False

while True:
    if check_results():
        send_email()
        print("🎉 All emails sent! Results announced.")
        break
    else:
        print("⏳ Not announced yet...")
    
    time.sleep(600)  # every 10 minutes
