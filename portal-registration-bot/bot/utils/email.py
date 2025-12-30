import smtplib
from email.mime.text import MIMEText

SENDER_EMAIL = "syed.rayyan52@gmail.com"
APP_PASSWORD = "-"
RECEIVER_EMAIL = "syed.rayyan0452@gmail.com"

def send_email(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)
