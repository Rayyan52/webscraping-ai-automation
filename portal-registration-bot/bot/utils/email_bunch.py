import smtplib
from email.mime.text import MIMEText

SENDER_EMAIL = "syed.rayyan52@gmail.com"
APP_PASSWORD = "echc ktet avve utlf"

# List of recipients
recipients = [
    "iqbalanas978@gmail.com",
    "enayatrehman8@gmail.com",
    "saadalikhan042@gmail.com",
    "mawwabkhank2006@gmail.com",
    "hiddenmystery621@gmail.com",
    "m.abyaz681@gmail.com",
    "muhammadtalha.mailme@gmail.com",
    "th47555@gmail.com",
    "nabeedjamshedali800@gmail.com",
    "abdulwahabshahid332@gmail.com",
    "danialsaud7@gmail.com",
    "raafiafatima5@gmail.com",
    "atayyaba965@gmail.com",
    "mlaamir2005@gmail.com",
    "maazalimurtaza@gmail.com",
    "rusher12789@gmail.com",
    "syedahmerali13@gmail.com",
    "syedahmerali12789@gmail.com"
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
