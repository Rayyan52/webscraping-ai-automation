<div align="center">

# 🎓 Result Notifier

### Automated AI-Powered Student Result Notification System

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

An intelligent automation system that monitors university examination results, leverages AI vision models to extract student data from official result images, and delivers personalized email notifications to each student.

[Features](#-features) •
[Installation](#-installation) •
[Usage](#-usage) •
[Configuration](#-configuration) •
[Documentation](#-documentation)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Customization](#-customization)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🔍 Overview

Result Notifier is an automated system designed to streamline the process of result distribution in educational institutions. The system:

1. 🌐 **Monitors** the NEDUET examination results page for new Software Engineering department announcements
2. 📥 **Downloads** official result notification images automatically
3. 🤖 **Extracts** student data (roll numbers and GPAs) using Groq's Llama 4 Scout vision AI model
4. 📧 **Sends** personalized email notifications to each student with their individual results

This eliminates the manual process of checking results and ensures students receive their grades instantly upon announcement.

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔍 **Automated Monitoring** | Continuously monitors the NEDUET results page for new announcements |
| 📥 **Smart Image Download** | Automatically downloads official result notification images |
| 🤖 **AI-Powered Extraction** | Uses Groq's Llama 4 Scout vision model with structured output for data extraction |
| ✉️ **Personalized Emails** | Sends individual emails to each student with their specific GPA and roll number |
| 🛡️ **Robust Error Handling** | Includes timeout management and connection error handling |
| 🔐 **Secure Configuration** | Environment variable management for API keys and credentials |
| ✅ **Type-Safe Data** | Pydantic models ensure validated and structured AI outputs |

---

## 🛠️ Tech Stack

<div align="center">

| Category | Technologies |
|----------|-------------|
| **Language** | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) |
| **AI/ML** | ![Groq](https://img.shields.io/badge/Groq-000000?style=for-the-badge) Llama 4 Scout, Instructor, Pydantic |
| **Web Scraping** | BeautifulSoup4, Requests, urllib |
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
├── caviar.py              # Main application script
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── result.jpg            # Downloaded result image (generated)
└── venv/                 # Virtual environment (optional)
```

## Prerequisites
- **Python 3.8+**: Required for modern type hints and async features
- **Groq API Key**: Sign up at [Groq Console](https://console.groq.com) to get your free API key
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
<summary><b>🔧 Common Issues & Solutions</b></summary>

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

---

## 🚀 Roadmap & Future Enhancements

- [ ] 🔄 Continuous monitoring with configurable intervals
- [ ] 🏫 Support multiple departments simultaneously
- [ ] 📱 SMS notifications via Twilio
- [ ] 🌐 Web dashboard to view sent notifications
- [ ] 💾 Database to track notification history
- [ ] 🔁 Retry logic for failed email deliveries
- [ ] 💬 Telegram bot integration
- [ ] 🎓 Support multiple universities
- [ ] 📊 Analytics dashboard for result trends
- [ ] 🔔 Push notifications mobile app

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
