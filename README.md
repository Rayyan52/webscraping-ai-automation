# NEDUET Result Notifier 🎓

An automated Python-based system that monitors the NEDUET examination results page, extracts student results using AI vision models, and sends personalized email notifications to students. This project combines web scraping, computer vision, and automated email delivery to provide instant result notifications.

## Features
- **Automated Web Scraping**: Continuously monitors the NEDUET results page for Software Engineering department announcements
- **Intelligent Image Download**: Downloads official result notification images when new results are posted
- **AI-Powered Data Extraction**: Leverages Groq's Llama 4 Scout vision model with structured output to extract roll numbers and GPAs from result images
- **Personalized Email Notifications**: Sends individual emails to each student with their specific GPA and roll number
- **Error Handling**: Robust timeout handling and connection management for reliable operation
- **Environment Variable Security**: Keeps sensitive credentials secure using `.env` file

## Tech Stack

### Core Technologies
- **Python 3.8+**: Main programming language providing the foundation for all components

### Web Scraping & HTTP
- **requests**: HTTP library for making web requests to fetch the NEDUET results page and download images
- **BeautifulSoup4 (bs4)**: HTML parser that navigates and searches the DOM to locate result announcements in specific table structures
- **urllib.parse**: URL manipulation for constructing absolute URLs from relative paths on the NEDUET website

### AI & Machine Learning
- **Groq**: Cloud-based AI inference API providing access to high-performance language models
  - Model used: `meta-llama/llama-4-scout-17b-16e-instruct` - A vision-capable model optimized for image understanding
- **Instructor**: Python library that adds structured output capabilities to language models
  - Converts raw AI responses into validated Python objects
  - Ensures type safety and data validation using Pydantic models
  - Handles image input processing for vision models
- **Pydantic**: Data validation library using Python type hints
  - Defines `Student` and `ResultSheet` models with field descriptions
  - Provides automatic validation and serialization
  - Ensures extracted data matches expected format (roll numbers as strings, GPAs as floats)

### Email & Communication
- **smtplib**: Python's built-in SMTP protocol client for sending emails
  - Configured for Gmail's SMTP server (smtp.gmail.com:465)
  - Uses SSL/TLS encryption for secure email transmission
- **email.mime.text**: Creates properly formatted email messages with headers and body content

### Configuration & Security
- **python-dotenv**: Loads environment variables from `.env` file
  - Secures API keys (Groq API)
  - Keeps credentials out of source code
  - Facilitates different configurations for development/production

### Data Structures
- **typing.List**: Type hints for better code documentation and IDE support
- **Field (from Pydantic)**: Adds metadata and descriptions to model fields for AI understanding

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

## Customization

### Changing the Department
To monitor results for a different department, modify the scraping logic in `download_result_image()` (around line 82):
```python
if cols[0].get_text(strip=True) == "Your Department Name":
```

### Changing the AI Model
You can switch to different Groq models by modifying line 154:
```python
model="meta-llama/llama-4-scout-17b-16e-instruct",  # Current model
# Alternative models:
# model="llama-3.2-90b-vision-preview",
# model="llama-3.2-11b-vision-preview",
```

### Customizing Email Content
Edit the email body in the `send_result_emails()` function (around lines 121-131):
```python
body = f"""
Your custom message here
GPA: {student.gpa}
Student ID: {student.roll_no}
"""
```

### Adding More Data Fields
To extract additional information (e.g., course grades), update the Pydantic models:
```python
class Student(BaseModel):
    roll_no: str
    gpa: float
    semester: str = Field(description="Semester name")
    # Add more fields as needed
```

## Troubleshooting

### Common Issues

**1. "Module not found" errors**
```bash
pip install -r requirements.txt
```

**2. "Authentication failed" when sending emails**
- Ensure 2FA is enabled on your Google account
- Use an App Password, not your regular password
- Check that SENDER_EMAIL and APP_PASSWORD are correct

**3. "API key not found"**
- Verify `.env` file exists in the project root
- Check that the key name is exactly `GROQ_API`
- Ensure `.env` is in the same directory as `caviar.py`

**4. No emails sent**
- Check if student roll numbers in results match those in `ROLL_EMAIL_MAP`
- Verify internet connection
- Check spam/junk folders

**5. AI extraction errors**
- Ensure the result image is clear and readable
- Verify the Groq API key is valid and has available credits
- Check the prompt matches the actual result format

## Future Enhancements
- [ ] Add continuous monitoring with configurable intervals
- [ ] Support multiple departments simultaneously
- [ ] Add SMS notifications via Twilio
- [ ] Create a web dashboard to view sent notifications
- [ ] Add database to track notification history
- [ ] Implement retry logic for failed email deliveries
- [ ] Add Telegram bot integration
- [ ] Support multiple universities

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## Security Considerations
- **Never commit `.env` files**: Add `.env` to your `.gitignore`
- **Use App Passwords**: Never use your main Gmail password
- **Protect student data**: Ensure you have consent to store and use email addresses
- **API key security**: Keep your Groq API key private
- **Rate limiting**: Be mindful of API usage limits

## Performance Notes
- **Groq inference**: Typically completes in 1-3 seconds
- **Email sending**: ~1 second per email via Gmail SMTP
- **Image download**: Depends on image size and connection speed
- **Total execution time**: Usually under 30 seconds for 20 students

## API Costs
- **Groq API**: Free tier includes generous limits
  - Model used is optimized for cost-efficiency
  - One image analysis per result check
- **Gmail SMTP**: Free (500 emails/day limit)

## Disclaimer
- This tool is for **educational and personal notification purposes only**
- Ensure you have **permission to use students' email addresses**
- The project is **not affiliated with NEDUET**
- Use responsibly and comply with your institution's policies
- Respect privacy and data protection regulations

## Acknowledgments
- Built with [Groq](https://groq.com) for fast AI inference
- Uses [Instructor](https://github.com/jxnl/instructor) for structured outputs
- Inspired by the need for instant result notifications

## License
MIT License - feel free to use and modify for your own projects

## Author
Created for NEDUET Software Engineering students
