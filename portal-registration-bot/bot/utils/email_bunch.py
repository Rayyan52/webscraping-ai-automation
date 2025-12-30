import smtplib
from email.mime.text import MIMEText

SENDER_EMAIL = "sender@gmail.com"
APP_PASSWORD = "your app passcode"

# List of recipients
recipients = [
    "user1@gmail.com",
    "user2@gmail.com",
]

def send_email(subject, body):
    for recipient in recipients:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = SENDER_EMAIL
        msg["To"] = recipient

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.send_message(msg)
        print(f"📧 Email sent to {recipient}")
