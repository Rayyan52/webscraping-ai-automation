from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from utils.email_bunch import send_email  # Your email function that handles multiple recipients

STATE_FILE = "email_sent.txt"

# Check if email was already sent
if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r") as f:
        notified = f.read().strip() == "1"
else:
    notified = False

driver = webdriver.Chrome()
driver.get("https://pl.neduet.edu.pk/?degtype=2")

print("👉 Login manually (captcha + password), then press ENTER")
input()

print("✅ Logged in. Searching for registration links...")

# Give the page a moment to load links
time.sleep(2)

# Refetch links safely
try:
    links = driver.find_elements(
        By.XPATH,
        "//a[contains(., 'Phase') and contains(., 'Registration')]"
    )
except Exception as e:
    print(f"❌ Error fetching registration links: {e}")
    driver.quit()
    exit()

if not links:
    print("❌ No registration links found after login.")
    driver.quit()
    exit()

# Click the first registration link safely
try:
    link_text = links[0].text
    link_url = links[0].get_attribute("href")
    print(f"👉 Clicking: {link_text}")
    links[0].click()
except Exception as e:
    print(f"❌ Failed to click registration link: {e}")
    driver.quit()
    exit()

time.sleep(3)  # wait for registration page to load

while True:
    try:
        driver.refresh()
        time.sleep(3)  # allow page to load

        # Look for the "registration not open" message
        try:
            msg_elem = driver.find_element(
                By.XPATH,
                "//*[contains(text(), 'Registration is not open yet')]"
            )
            msg_text = msg_elem.text.strip()
            print(f"❌ {msg_text}")

        except:
            # Message not found -> registration is likely open
            if not notified:
                # Send email to all recipients
                send_email(
                    "🚨 Registration Open",
                    f"🚨 Registration is now open!\n\nYou can check it now: {driver.current_url},  Who wants chinese language :p"
                )
                print("📧 Email sent to all recipients!")

                # Save state to file
                with open(STATE_FILE, "w") as f:
                    f.write("1")
                notified = True

                # Close the browser after sending the email
                driver.quit()
                print("✅ Browser closed. Script finished.")
                break  # exit the loop

        time.sleep(20)  # check every 20 seconds

    except Exception as e:
        print(f"⚠️ Error during monitoring loop: {e}")
        time.sleep(5)
