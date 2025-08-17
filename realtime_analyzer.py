import time
import smtplib
import csv
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

LOG_FILE = "auth_sample.log"   # replace with your real log file
ALERTS_FILE = "alerts.csv"

# Email setup
SENDER_EMAIL = "manasilohar8533@gmail.com"
SENDER_PASSWORD = "cvsp azkr pwzj fqos"   # App password
RECEIVER_EMAIL = "manasilohar8533@gmail.com"

def send_email_alert(ip, line):
    try:
        subject = "🚨 Security Alert: Suspicious Activity Detected"
        body = f"Suspicious activity detected!\n\nIP: {ip}\nLog: {line}"

        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())

        print(f"[📧] Email alert sent for IP {ip}")
    except Exception as e:
        print(f"[❌] Failed to send email: {e}")

def log_alert(ip, line):
    with open(ALERTS_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), ip, line])
    print(f"[!] Suspicious entry logged for IP {ip}")

class LogHandler(FileSystemEventHandler):
    def __init__(self):
        self.position = 0   # remember file position

    def on_modified(self, event):
        if event.src_path.endswith(LOG_FILE):
            with open(LOG_FILE, 'r') as f:
                f.seek(self.position)   # go to last read position
                new_lines = f.readlines()
                self.position = f.tell()  # update position

            for line in new_lines:
                line = line.strip()
                if "Failed login attempt" in line or "Failed password" in line:
                    parts = line.split()
                    if "from" in parts:
                        ip = parts[parts.index("from") + 1]
                    else:
                        ip = "Unknown"

                    send_email_alert(ip, line)
                    log_alert(ip, line)

if __name__ == "__main__":
    print("[*] Real-time log monitoring started. Press Ctrl+C to stop.")
    event_handler = LogHandler()
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
