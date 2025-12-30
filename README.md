<div align="center">



### AI-Powered Result Notifier & Portal Registration Monitor

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green.svg)](https://www.selenium.dev/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A comprehensive automation toolkit for NEDUET students featuring two powerful bots:
1. **Result Notifier** - AI-powered result extraction and email delivery
2. **Portal Registration Monitor** - Automated registration availability checker

[Features](#-features) •
[Installation](#-installation) •
[Usage](#-usage) •
[Configuration](#-configuration) •
[Documentation](#-documentation)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Quick Start](#-quick-start)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
  - [Result Notifier Bot](#result-notifier-bot)
  - [Portal Registration Monitor](#portal-registration-monitor)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Customization](#-customization)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🔍 Overview

This repository contains two powerful automation tools designed to streamline NEDUET student processes:

### 📊 Quick Comparison

| Feature | Result Notifier | Portal Registration Monitor |
|---------|----------------|---------------------------|
| **Purpose** | Exam results notification | Course registration alerts |
| **Technology** | AI Vision (Groq) + Web Scraping | Selenium Browser Automation |
| **User Interaction** | Fully automated | Manual login required |
| **Frequency** | Checks once (configurable) | Continuous monitoring (20s) |
| **Notifications** | Individual student emails | Bulk/multi-recipient alerts |
| **Setup Complexity** | Medium (API key needed) | Easy (just configure emails) |

---

### 🎯 Result Notifier Bot
An intelligent system that monitors the NEDUET examination results page, downloads result images, uses AI vision models to extract student data, and sends personalized email notifications.

**Workflow:**
1. 🌐 **Monitors** the NEDUET examination results page for new Software Engineering department announcements
2. 📥 **Downloads** official result notification images automatically
3. 🤖 **Extracts** student data (roll numbers and GPAs) using Groq's Llama 4 Scout vision AI model
4. 📧 **Sends** personalized email notifications to each student with their individual results

### 🔔 Portal Registration Monitor
An automated browser-based monitor that continuously checks the NEDUET student portal for course registration availability and instantly alerts students when registration opens.

**Workflow:**
1. 🌐 **Logs into** the NEDUET student portal (pl.neduet.edu.pk)
2. 🔄 **Monitors** registration links for phase-based course registration
3. 🔍 **Detects** when "Registration is not open yet" message disappears
4. 📧 **Alerts** students immediately via email when registration becomes available

Both tools eliminate manual checking and ensure students never miss critical deadlines!

---

## ⚡ Quick Start

### For Result Notifier (AI-powered exam results):

```bash
# 1. Install dependencies
pip install requests beautifulsoup4 python-dotenv groq instructor pydantic

# 2. Create .env file with your Groq API key
echo "GROQ_API=your_api_key_here" > .env

# 3. Configure email in caviar.py (lines 20-21)
# SENDER_EMAIL and APP_PASSWORD

# 4. Run
python caviar.py
```

### For Portal Registration Monitor (course registration alerts):

```bash
# 1. Install Selenium
pip install selenium

# 2. Configure email in portal-registration-bot/bot/utils/email_bunch.py
# Add recipient emails to the list

# 3. Run (browser will open)
cd portal-registration-bot/bot
python Register.py

# 4. Login manually when prompted, then press Enter
# The script will monitor and alert you!
```

---

## ✨ Features

### 🎓 Result Notifier Bot

| Feature | Description |
|---------|-------------|
| 🔍 **Automated Monitoring** | Continuously monitors the NEDUET results page for new announcements |
| 📥 **Smart Image Download** | Automatically downloads official result notification images |
| 🤖 **AI-Powered Extraction** | Uses Groq's Llama 4 Scout vision model with structured output for data extraction |
| ✉️ **Personalized Emails** | Sends individual emails to each student with their specific GPA and roll number |
| 🛡️ **Robust Error Handling** | Includes timeout management and connection error handling |
| 🔐 **Secure Configuration** | Environment variable management for API keys and credentials |
| ✅ **Type-Safe Data** | Pydantic models ensure validated and structured AI outputs |

### 🔔 Portal Registration Monitor

| Feature | Description |
|---------|-------------|
| 🌐 **Browser Automation** | Uses Selenium WebDriver for reliable portal interaction |
| 🔐 **Manual Login Support** | Handles CAPTCHA and secure login requirements |
| 🔄 **Continuous Monitoring** | Auto-refreshes portal page every 20 seconds |
| 🎯 **Phase Detection** | Identifies all registration phases automatically |
| 📧 **Instant Alerts** | Sends immediate email notifications when registration opens |
| 💾 **State Persistence** | Prevents duplicate notifications using state file |
| 👥 **Multi-Recipient** | Supports sending alerts to multiple students simultaneously |
| ⚡ **Auto-Close** | Browser closes automatically after successful notification |

---

## 🛠️ Tech Stack

<div align="center">

| Category | Technologies |
|----------|-------------|
| **Language** | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) |
| **AI/ML** | ![Groq](https://img.shields.io/badge/Groq-000000?style=for-the-badge) Llama 4 Scout, Instructor, Pydantic |
| **Web Scraping** | BeautifulSoup4, Requests, urllib |
| **Browser Automation** | ![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white) WebDriver |
| **Email** | SMTP (Gmail), email.mime |
| **Configuration** | python-dotenv |

</div>

### Core Technologies

#### 🐍 Python 3.8+
Foundation language providing modern type hints and async capabilities

#### 🌐 Web Scraping & HTTP
- **requests** - HTTP library for web requests and image downloads
- **BeautifulSoup4** - HTML parsing and DOM navigation
- **urllib.parse** - URL manipulation and construction

#### 🤖 Browser Automation
- **Selenium WebDriver** - Browser automation for portal interaction
  - Chrome WebDriver for reliable page rendering
  - Element detection and interaction
  - Dynamic page monitoring and refresh
  - XPath-based element selection

#### 🤖 AI & Machine Learning
- **Groq API** - High-performance cloud-based AI inference
  - Model: `meta-llama/llama-4-scout-17b-16e-instruct`
  - Optimized for vision and image understanding
- **Instructor** - Structured LLM outputs with validation
  - Converts AI responses to typed Python objects
  - Handles image input processing
- **Pydantic** - Data validation using Python type hints
  - Defines `Student` and `ResultSheet` models
  - Automatic validation and serialization

#### 📧 Email & Communication
- **smtplib** - SMTP protocol client (Gmail SMTP: smtp.gmail.com:465)
- **SSL/TLS encryption** - Secure email transmission
- **email.mime.text** - Properly formatted email messages

#### ⚙️ Configuration & Security
- **python-dotenv** - Environment variable management
- Secure API key and credential storage

---

## How It Works

### 1. Web Scraping Phase
The script sends an HTTP GET request to `https://www.neduet.edu.pk/examination_results` and parses the HTML response. It searches for table rows (`<tr>`) where:
- The first column matches "Software Engg."
- The third column contains a "View" link to the result image

### 2. Image Download Phase
When a valid result link is found:
- Constructs the absolute URL using `urljoin()`
- Downloads the image binary data
- Saves it locally as `result.jpg`

### 3. AI Vision Extraction Phase
The downloaded image is processed using:
- **Instructor** wraps the Groq client to enable structured outputs
- The image is loaded and sent to the **Llama 4 Scout** vision model along with a detailed prompt
- The prompt instructs the model to:
  - Focus only on the passing grades table
  - Extract seat numbers and GPAs with exact formatting
  - Ignore all other sections of the result notification
- The model returns a `ResultSheet` object containing a list of `Student` objects
- Each `Student` has validated `roll_no` (string) and `gpa` (float) fields

### 4. Email Notification Phase
For each student in the extracted results:
- Looks up their email address in `ROLL_EMAIL_MAP`
- Creates a personalized email with their GPA and roll number
- Sends via Gmail SMTP server using SSL encryption
- Logs successful email deliveries

## Project Structure
```
resultss/
├── 📄 README.md                    # Project documentation
├── 📄 requirements.txt             # Python dependencies
├── 🐍 caviar.py                   # Result notifier main script
├── 🖼️ result.jpg                  # Downloaded result image (auto-generated)
├── 🔐 .env                         # Environment variables (create this)
├── 📁 venv/                        # Virtual environment (optional)
├── 📁 Result Checker/              # Legacy/alternative scripts
│   ├── caviar.py
│   └── test.py
├── 📁 portal-registration-bot/     # Portal registration monitoring system
│   ├── bot/
│   │   ├── 🐍 Register.py         # Main registration monitor (single-recipient)
│   │   ├── 🐍 monitor.py          # Alternative monitor (continuous)
│   │   ├── 📄 email_sent.txt      # State file to track sent notifications
│   │   └── utils/
│   │       ├── email.py           # Single recipient email utility
│   │       └── email_bunch.py     # Multi-recipient email utility
│   └── data/                       # Data storage (if needed)
└── 📁 troubleshoot/                # Debugging and testing scripts
    ├── LLM.py
    └── resssult_checker.py
```

## Prerequisites
- **Python 3.8+**: Required for modern type hints and async features
- **Groq API Key**: Sign up at [Groq Console](https://console.groq.com) to get your free API key (for Result Notifier)
- **Chrome Browser**: Required for Portal Registration Monitor
- **ChromeDriver**: Selenium WebDriver for Chrome (auto-install available)
- **Gmail Account**: With App Password enabled for SMTP access
  - Enable 2-Factor Authentication on your Google account
  - Generate an App Password: Google Account → Security → 2-Step Verification → App passwords
- **Internet Connection**: For accessing NEDUET website and Groq API

## Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd resultss
```

2. **Create a virtual environment (recommended)**
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

**Required packages:**
- `requests` - HTTP requests for web scraping
- `beautifulsoup4` - HTML parsing
- `python-dotenv` - Environment variable management
- `groq` - Groq AI API client
- `instructor` - Structured LLM outputs
- `pydantic` - Data validation
- `selenium` - Browser automation (for Portal Registration Monitor)
- `webdriver-manager` - Automatic ChromeDriver management (optional)

## Configuration

### 1. Environment Variables
Create a `.env` file in the project root directory:
```env
GROQ_API=your_groq_api_key_here
```

### 2. Email Credentials
Edit `caviar.py` and update the following lines (around lines 20-21):
```python
SENDER_EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_16_character_app_password"
```

### 3. Student Email Mapping
Update the `ROLL_EMAIL_MAP` dictionary in `caviar.py` (around lines 24-45) with your students' information:
```python
ROLL_EMAIL_MAP = {
    "SE-23051": "student1@example.com",
    "SE-23052": "student2@example.com",
    # Add more students as needed
}
```

## Usage

---

## 🎓 Result Notifier Bot

### Running the Script
```bash
python caviar.py
```

### Expected Output
```
✅ Result image downloaded
{
  "students": [
    {
      "roll_no": "SE-23051",
      "gpa": 3.45
    },
    {
      "roll_no": "SE-23052",
      "gpa": 3.78
    }
  ]
}
📧 Email sent to SE-23051 → student1@example.com
📧 Email sent to SE-23052 → student2@example.com
```

If results are not yet announced:
```
⏳ Results not announced yet...
```

## Email Template
Each student receives an email with:
```
Subject: 🎓 Semester Result Announced

Hello SE-XXXXX,

Your semester result has been announced.

GPA: X.XX
Student ID: SE-XXXXX

You ARE COOKED! HEHE

Official link:
https://www.neduet.edu.pk/examination_results
```

---

## 🔔 Portal Registration Monitor

The Portal Registration Monitor automates the tedious process of checking the NEDUET student portal for course registration availability. Two scripts are available:

### 📋 Available Scripts

#### 1. `Register.py` - One-Time Alert (Recommended)
**Best for:** Single notification when registration opens

**Features:**
- ✅ Monitors registration page continuously
- ✅ Sends email to multiple recipients when registration opens
- ✅ Prevents duplicate notifications using state file
- ✅ Auto-closes browser after sending notification

#### 2. `monitor.py` - Continuous Monitoring
**Best for:** Tracking multiple registration phases

**Features:**
- ✅ Continuously monitors all registration phases
- ✅ Sends separate alerts for each phase
- ✅ Tracks which phases have been notified
- ✅ Runs indefinitely until manually stopped

---

### 🚀 Setup & Configuration

#### Step 1: Install Selenium

```bash
pip install selenium
```

#### Step 2: Install Chrome WebDriver

**Option A: Automatic (Recommended)**
```bash
pip install webdriver-manager
```

**Option B: Manual**
1. Check your Chrome version: `chrome://settings/help`
2. Download matching ChromeDriver: [https://chromedriver.chromium.org/](https://chromedriver.chromium.org/)
3. Add to PATH or place in project directory

#### Step 3: Configure Email Settings

**For Single Recipient (utils/email.py):**
```python
SENDER_EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_16_character_app_password"
RECEIVER_EMAIL = "recipient@gmail.com"
```

**For Multiple Recipients (utils/email_bunch.py):**
```python
SENDER_EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_16_character_app_password"

recipients = [
    "student1@gmail.com",
    "student2@gmail.com",
    "student3@gmail.com",
    # Add more students
]
```

---

### 🎯 Usage

#### Running Register.py (One-Time Alert)

```bash
cd portal-registration-bot/bot
python Register.py
```

**Expected Workflow:**
```
👉 Login manually (captcha + password), then press ENTER
[User logs in through browser]

✅ Logged in. Searching for registration links...
👉 Clicking: Phase 1 Registration

❌ Registration is not open yet
❌ Registration is not open yet
❌ Registration is not open yet
✅ Registration is now open!

📧 Email sent to all recipients!
✅ Browser closed. Script finished.
```

#### Running monitor.py (Continuous Monitoring)

```bash
cd portal-registration-bot/bot
python monitor.py
```

**Expected Workflow:**
```
👉 Login manually (captcha + password), then press ENTER
[User logs in through browser]

✅ Logged in. Monitoring registration links...

❌ No registration open yet
❌ No registration open yet
🚨 Phase 1 Registration detected!
📧 Email sent for: Phase 1 Registration
🚨 Phase 2 Registration detected!
📧 Email sent for: Phase 2 Registration
[Continues monitoring...]
```

---

### 📧 Email Notification Format

When registration opens, students receive:

```
Subject: 🚨 Registration Open

Phase 1 Registration

https://pl.neduet.edu.pk/?degtype=2

🚨 Registration is now open!
You can check it now: [URL]
Who wants chinese language :p
```

---

### 🔧 How It Works

#### Register.py Workflow

1. **Browser Launch** 🌐
   - Opens Chrome browser with Selenium
   - Navigates to NEDUET portal login page

2. **Manual Login** 🔐
   - User manually solves CAPTCHA
   - User enters credentials
   - Script waits for user confirmation (Enter key)

3. **Link Detection** 🔍
   - Searches for registration phase links using XPath
   - Clicks on the first available registration link

4. **Continuous Monitoring** 🔄
   - Refreshes page every 20 seconds
   - Checks for "Registration is not open yet" message
   - When message disappears → registration is open!

5. **Notification** 📧
   - Sends email to all recipients in `email_bunch.py`
   - Saves state to `email_sent.txt` to prevent duplicates
   - Closes browser automatically

#### monitor.py Workflow

1. **Browser Launch & Login** 🌐🔐
   - Same as Register.py

2. **Multi-Phase Detection** 🔍
   - Detects ALL registration phase links on the page
   - Tracks each phase separately

3. **Continuous Monitoring** 🔄
   - Refreshes every 20 seconds
   - Checks which phases are available

4. **Per-Phase Notifications** 📧
   - Sends individual email for each new phase detected
   - Tracks notified phases to avoid duplicates
   - Continues running indefinitely

---

### ⚙️ Customization

#### Change Check Interval

```python
# In Register.py or monitor.py
time.sleep(20)  # Change to desired seconds (e.g., 30, 60)
```

#### Modify Email Message

```python
# In Register.py
send_email(
    "🚨 Registration Open",
    f"🚨 Registration is now open!\n\nCustom message here\n\n{driver.current_url}"
)
```

#### Change Target Portal

```python
# Modify the URL in both scripts
driver.get("https://pl.neduet.edu.pk/?degtype=2")  # Change degtype parameter
```

---

### 🛑 Stopping the Monitor

**For monitor.py (continuous):**
- Press `Ctrl + C` in terminal
- Or close the terminal window

**For Register.py:**
- Automatically stops after sending notification
- Can also press `Ctrl + C` to stop early

---

### 📝 State File (email_sent.txt)

The `email_sent.txt` file prevents duplicate notifications:

```
1  # Notification has been sent
```

**To reset (allow re-notification):**
```bash
# Delete the file
rm email_sent.txt

# Or manually edit to:
0
```

---

## Key Features Explained

### Structured AI Output
The script uses **Instructor** with **Pydantic** models to ensure the AI returns perfectly structured data:
- Type safety: GPAs are always floats, roll numbers are always strings
- Automatic validation: Invalid data is rejected
- Field descriptions guide the AI to extract correct information

### Error Handling
- **Timeout protection**: All HTTP requests have 15-second timeouts
- **Missing data handling**: Students not in the email map are skipped
- **Connection security**: Uses SSL/TLS for email transmission

### Monitoring Loop
The current implementation checks once and exits. To make it continuously monitor:
```python
# Replace the last line `break` with:
import time
time.sleep(300)  # Check every 5 minutes
```

## 🎨 Customization

### 🏫 Changing the Department

To monitor results for a different department, modify the scraping logic:

```python
# In download_result_image() function
if cols[0].get_text(strip=True) == "Your Department Name":
```

### 🤖 Changing the AI Model

Switch to different Groq models:

```python
model="meta-llama/llama-4-scout-17b-16e-instruct",  # Current model

# Alternative models:
# model="llama-3.2-90b-vision-preview",
# model="llama-3.2-11b-vision-preview",
```

### ✉️ Customizing Email Content

Edit the email body in the `send_result_emails()` function:

```python
body = f"""
Your custom message here
GPA: {student.gpa}
Student ID: {student.roll_no}
"""
```

### 📊 Adding More Data Fields

To extract additional information (e.g., course grades), update the Pydantic models:

```python
class Student(BaseModel):
    roll_no: str = Field(description="Student roll number")
    gpa: float = Field(description="Grade point average")
    semester: str = Field(description="Semester name")
    courses: List[str] = Field(description="List of courses")
    # Add more fields as needed
```

---

## ❗ Troubleshooting

<details>
<summary><b>🔧 Result Notifier Issues</b></summary>

### 1. "Module not found" errors

**Solution:**
```bash
pip install -r requirements.txt
```

### 2. "Authentication failed" when sending emails

**Checklist:**
- ✅ 2FA is enabled on your Google account
- ✅ Using App Password, not regular password
- ✅ SENDER_EMAIL and APP_PASSWORD are correct
- ✅ No extra spaces in credentials

### 3. "API key not found"

**Checklist:**
- ✅ `.env` file exists in the project root
- ✅ Key name is exactly `GROQ_API`
- ✅ `.env` is in the same directory as `caviar.py`
- ✅ No quotes around the API key value

### 4. No emails sent

**Debug steps:**
- 🔍 Verify student roll numbers in results match `ROLL_EMAIL_MAP`
- 🔍 Check internet connection
- 🔍 Look in spam/junk folders
- 🔍 Verify Gmail SMTP is enabled

### 5. AI extraction errors

**Solutions:**
- 🖼️ Ensure the result image is clear and readable
- 🔑 Verify the Groq API key is valid
- 💳 Check Groq API has available credits
- 📝 Ensure prompt matches the actual result format

</details>

<details>
<summary><b>🌐 Portal Registration Monitor Issues</b></summary>

### 1. "ChromeDriver not found" error

**Solution A - Automatic:**
```bash
pip install webdriver-manager
```

Then update script to use:
```python
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
```

**Solution B - Manual:**
1. Download ChromeDriver: [https://chromedriver.chromium.org/](https://chromedriver.chromium.org/)
2. Match your Chrome version
3. Add to PATH or project folder

### 2. "Element not found" errors

**Cause:** Page not fully loaded or NEDUET changed their HTML structure

**Solutions:**
```python
# Increase wait time
time.sleep(5)  # Instead of 3

# Or use explicit waits
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "...")))
```

### 3. Browser opens but nothing happens

**Checklist:**
- ✅ You logged in manually
- ✅ You pressed Enter after logging in
- ✅ Check for CAPTCHA that needs solving
- ✅ Ensure you're on the correct portal page

### 4. Multiple notification emails

**Cause:** State file not working

**Solution:**
```bash
# Check if email_sent.txt exists
ls portal-registration-bot/bot/

# Verify it contains "1"
cat email_sent.txt

# If not, create it:
echo "0" > email_sent.txt
```

### 5. Script stops unexpectedly

**Causes & Solutions:**
- 🔌 **Network issue** → Check internet connection
- 🌐 **Portal is down** → Wait and retry
- 🔒 **Session expired** → Script will show login prompt again
- ⚠️ **XPath changed** → NEDUET updated their website (update XPath)

### 6. "Registration not open" message not detected

**Solution:** Update the XPath to match current portal structure:
```python
msg_elem = driver.find_element(
    By.XPATH,
    "//*[contains(text(), 'Registration is not open yet')]"
)
```

Try alternative detection methods:
```python
# Check if registration button is enabled
button = driver.find_element(By.ID, "register-button")
if button.is_enabled():
    # Registration is open
```

</details>

---

## 🚀 Roadmap & Future Enhancements

### Result Notifier
- [ ] 🔄 Continuous monitoring with configurable intervals
- [ ] 🏫 Support multiple departments simultaneously
- [ ] 📊 Analytics dashboard for result trends
- [ ] 💾 Database to track notification history
- [ ] 🎓 Support multiple universities
- [ ] 🔁 Retry logic for failed email deliveries

### Portal Registration Monitor
- [ ] 🤖 Headless browser mode (no GUI)
- [ ] 🔐 Automatic CAPTCHA solving
- [ ] 🔄 Auto-restart on session timeout
- [ ] 📊 Registration statistics tracking
- [ ] 🔔 Multi-channel alerts (Discord, Telegram, SMS)
- [ ] ⏰ Custom check intervals per phase

### Both Systems
- [ ] 📱 SMS notifications via Twilio
- [ ] 🌐 Web dashboard to view sent notifications
- [ ] 💬 Telegram bot integration
- [ ] 📧 Enhanced email templates with HTML
- [ ] 🔐 Better credential management (keyring)
- [ ] 🐳 Docker containerization

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🔀 Open a Pull Request

### Contribution Guidelines

- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

---

## 🔒 Security Considerations

| Area | Best Practice |
|------|---------------|
| 🔐 Environment Files | Never commit `.env` files - add to `.gitignore` |
| 📧 Email Security | Use App Passwords, never your main Gmail password |
| 👥 Student Data | Ensure consent to store and use email addresses |
| 🔑 API Keys | Keep your Groq API key private and secure |
| ⚡ Rate Limiting | Be mindful of API usage limits |
| 🛡️ Data Privacy | Comply with GDPR/local data protection regulations |

---

## ⚡ Performance Metrics

| Operation | Typical Duration |
|-----------|------------------|
| 🤖 Groq AI Inference | 1-3 seconds |
| 📧 Email Sending | ~1 second per email |
| 📥 Image Download | Varies by size/connection |
| 🏁 Total Execution | <30 seconds for 20 students |

---

## 💰 API Costs

### Groq API
- ✅ **Free tier** with generous limits
- ✅ Model optimized for cost-efficiency
- ✅ One image analysis per result check

### Gmail SMTP
- ✅ **Completely free**
- ⚠️ Limit: 500 emails/day

---

## ⚠️ Disclaimer

> **Important Legal Notice**

- This tool is for **educational and personal notification purposes only**
- Ensure you have **explicit permission** to use students' email addresses
- The project is **not affiliated with or endorsed by NEDUET**
- Use responsibly and comply with your institution's policies
- Respect all privacy and data protection regulations (GDPR, COPPA, etc.)
- The authors are not responsible for misuse of this software

---

## 🙏 Acknowledgments

This project was made possible by:

- [Groq](https://groq.com) - Lightning-fast AI inference
- [Instructor](https://github.com/jxnl/instructor) - Structured LLM outputs
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation
- The open-source community

**Inspired by:** The need for instant, automated result notifications for students

---

## 📄 License

```
MIT License

Copyright (c) 2024 Result Notifier Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 👨‍💻 Author & Contact

**Created for:** NEDUET Software Engineering Students

**Maintainer:** Your Name

**Links:**
- 🐙 GitHub: [@yourusername](https://github.com/yourusername)
- 📧 Email: your.email@example.com
- 💼 LinkedIn: [Your Name](https://linkedin.com/in/yourprofile)

---

<div align="center">

### ⭐ If this project helped you, please consider giving it a star!

**Made with for students by students**

[Report Bug](https://github.com/yourusername/result-notifier/issues) • [Request Feature](https://github.com/yourusername/result-notifier/issues) • [Documentation](https://github.com/yourusername/result-notifier/wiki)

</div>
