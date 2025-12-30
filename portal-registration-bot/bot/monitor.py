from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utils.email import send_email

driver = webdriver.Chrome()
driver.get("https://pl.neduet.edu.pk/?degtype=2")

print("👉 Login manually (captcha + password), then press ENTER")
input()

print("✅ Logged in. Monitoring registration links...")

notified = set()

while True:
    driver.refresh()
    time.sleep(3)  # allow page to load

    links = driver.find_elements(
        By.XPATH,
        "//a[contains(., 'Phase') and contains(., 'Registration')]"
    )

    if links:
        for link in links:
            phase_text = link.text.strip()
            phase_url = link.get_attribute("href")

            if phase_text not in notified:
                send_email(
                    "🚨 Registration Open",
                    f"{phase_text}\n\n{phase_url}"
                )
                print(f"📧 Email sent for: {phase_text}")
                notified.add(phase_text)
    else:
        print("❌ No registration open yet")

    time.sleep(20)  # refresh every 20 seconds
