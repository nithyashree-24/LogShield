🛡️ LogShield

A lightweight Python security log analyzer for detecting suspicious authentication activity.

🛡️ Overview

LogShield analyzes authentication logs and identifies repeated failed login attempts that may indicate suspicious activity.

The tool processes log entries, extracts relevant information, and highlights IP addresses associated with multiple failed login attempts.

✨ Features

- 🔐 Failed login attempt detection
- 🌐 IP address extraction
- 📊 Failed attempt counting
- ⚠️ Suspicious activity identification
- 📄 Simple text-based log analysis
- ⚙️ Configurable monitoring settings
- 🧩 Lightweight and easy to extend

🧰 Technologies Used

- Python
- Regular Expressions ("re")
- File Handling
- String Processing
- JSON Configuration
- Data Structures

⚙️ Configuration

LogShield supports configurable monitoring settings through the "config.json" file.

The configuration file allows users to customize:

- Failed login attempt threshold
- Log file location
- Alert status

Example:

{
    "failed_attempt_threshold": 3,
    "log_file": "sample_logs.txt",
    "alert_enabled": true
}

⚙️ Configuration Options

Setting| Description
"failed_attempt_threshold"| Number of failed attempts required before an IP is flagged
"log_file"| Authentication log file to analyze
"alert_enabled"| Enables or disables suspicious activity alerts

🔍 Monitoring Process

LogShield follows a simple analysis workflow:

1. Reads the authentication log file.
2. Loads monitoring settings from "config.json".
3. Identifies successful and failed login attempts.
4. Extracts IP addresses from log entries.
5. Counts failed attempts for each IP address.
6. Compares failed attempts against the configured threshold.
7. Flags IP addresses with repeated failed attempts.
8. Displays the analysis results.

📄 Event Logging

The analyzer processes authentication events and identifies relevant security activity from the log file.

Each analyzed event may contain:

- Timestamp
- Login status
- Source IP address
- Failed attempt count
- Suspicious activity status

🚀 How to Run

📥 Clone Repository

git clone https://github.com/nithyashree-24/LogShield.git
cd LogShield

▶️ Run the Analyzer

python log_analyzer.py

📄 Analyze the Sample Log

Make sure "sample_logs.txt" and "config.json" are present in the project folder before running the analyzer.

The analyzer reads the configured log file and applies the threshold specified in "config.json".

🎯 Project Objective

The objective of LogShield is to demonstrate a basic security log analysis technique using Python.The project focuses on detecting repeated authentication failures and identifying potentially suspicious source IP addresses through configurable monitoring rules.

🔮 Future Enhancements

- 🔹 Real-Time Log Monitoring
  
  Monitor authentication logs continuously and detect suspicious activity as it occurs.

- 🔹 IP Reputation Checking
  
  Integrate external threat-intelligence sources to check suspicious IP addresses.

- 🔹 Automated Alerting
  
  Generate security alerts when repeated failed login attempts are detected.

- 🔹 Advanced Detection Rules
  
  Detect brute-force patterns, unusual login times, and repeated authentication failures.

- 🔹 Security Dashboard
  
  Build a graphical dashboard for visualizing login activity, suspicious IPs, and security events.

⚠️ Security Note

This project is intended for educational and defensive security purposes.

The detected activity is based on predefined log patterns and should not be treated as proof of malicious behaviour.


