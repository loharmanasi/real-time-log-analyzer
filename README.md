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

- pip install watchdog

2. Update the script with your email details:

  SENDER_EMAIL = "your-email@gmail.com"
  SENDER_PASSWORD = "your-app-password"   # Use Gmail App Password
  RECEIVER_EMAIL = "your-email@gmail.com"

3. Run the analyzer:

  python realtime_analyzer.py

# 🔍 Terminal Output
![terminal op](https://github.com/user-attachments/assets/37359039-efa1-4f5e-b128-35d1d68b217b)

# 📧 Email Alert Example
<img width="847" height="257" alt="Untitled design (1)" src="https://github.com/user-attachments/assets/6a10596b-1c7e-4d8c-a3a5-fb8faeca7c5d" />
<img width="920" height="254" alt="Untitled design (2)" src="https://github.com/user-attachments/assets/a2b7ad29-8aaa-4499-934c-e0a2da54cf75" />
<img width="921" height="245" alt="Untitled design (3)" src="https://github.com/user-attachments/assets/c435b8d9-6445-40a7-96d1-1ea4fda03e1d" />
<img width="920" height="249" alt="Untitled design (4)" src="https://github.com/user-attachments/assets/aa524fa5-7044-43b8-89a3-618f5273c8fe" />

