# 🔍 Real-Time Log Analyzer with Email Alerts

This project is a **Python-based real-time log monitoring tool** that detects suspicious login attempts (like failed SSH logins) from system logs and triggers **email alerts.**  
It also logs the suspicious activity in a CSV file for auditing.

# ✨ Features
- 📡 **Real-time monitoring** of system authentication logs
- 📧 **Email alerts** for suspicious activity
- 📝 Logs alerts into a CSV file ('alerts.csv')
- ⚡ Used watchdog because it allows script to automatically detect changes in log files in real time without needing to manually refresh or repeatedly read the file.

# Setup Instructions
1. Install dependencies:

pip install watchdog

2. Update the script with your email details:

SENDER_EMAIL = "your-email@gmail.com"
SENDER_PASSWORD = "your-app-password"   # Use Gmail App Password
RECEIVER_EMAIL = "your-email@gmail.com"

3. Run the analyzer:

python realtime_analyzer.py

# 🔍 Terminal Output
<img width="731" height="322" alt="terminal op" src="https://github.com/user-attachments/assets/25b8040d-149d-4c4a-89ae-66d87cd24535" />

