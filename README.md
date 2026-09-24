# 🛡️ LogShield

A lightweight Python security log analyzer for detecting suspicious authentication activity.

## 🛡️ Overview

LogShield analyzes authentication logs and identifies repeated failed login attempts that may indicate suspicious activity.

The tool processes log entries, extracts relevant information, counts failed login attempts, and highlights IP addresses associated with repeated authentication failures.

## ✨ Features

- 🔐 Failed login attempt detection
- 🌐 IP address extraction
- 📊 Failed attempt counting
- ⚠️ Suspicious activity identification
- 🎯 Risk level classification
- 🚨 Configurable alerting
- ⚙️ JSON-based configuration
- 📄 Simple text-based log analysis
- 🧩 Lightweight and easy to extend

## 🧰 Technologies Used

- Python
- Regular Expressions (`re`)
- JSON (`json`)
- File Handling
- String Processing
- Collections (`Counter`)
- Date and Time Handling (`datetime`)

## 📦 Requirements

- Python 3.x
- No external Python packages required
- Uses only Python standard library modules

## 📁 Project Structure

```text
LogShield/
│
├── log_analyzer.py
├── config.json
├── sample_logs.txt
└── README.md
```

### 📄 File Description

| File | Description |
|---|---|
| `log_analyzer.py` | Main Python security log analyzer |
| `config.json` | Configurable monitoring settings |
| `sample_logs.txt` | Sample authentication log data |
| `README.md` | Project documentation |

## ⚙️ Configuration

LogShield supports configurable monitoring settings through the `config.json` file.

The configuration file allows users to customize:

- Failed login attempt threshold
- Log file location
- Alert status

Example:

```json
{
    "failed_attempt_threshold": 3,
    "log_file": "sample_logs.txt",
    "alert_enabled": true
}
```

### ⚙️ Configuration Options

| Setting | Description |
|---|---|
| `failed_attempt_threshold` | Number of failed attempts required before an IP is flagged |
| `log_file` | Authentication log file to analyze |
| `alert_enabled` | Enables or disables suspicious activity alerts |

## 🔍 Monitoring Process

LogShield follows a simple analysis workflow:

1. Reads the authentication log file.
2. Loads monitoring settings from `config.json`.
3. Identifies successful and failed login attempts.
4. Extracts IP addresses from log entries.
5. Counts failed attempts for each IP address.
6. Compares failed attempts against the configured threshold.
7. Assigns a risk level based on failed attempts.
8. Flags IP addresses with repeated failed attempts.
9. Generates security alerts when alerting is enabled.
10. Displays the analysis results.

## 📄 Event Logging

The analyzer processes authentication events and identifies relevant security activity from the log file.

Each analyzed event may contain:

- Timestamp
- Login status
- Source IP address
- Failed attempt count
- Risk level
- Suspicious activity status

## 📊 Risk Classification

LogShield assigns a basic risk level based on the number of failed login attempts.

| Condition | Risk Level |
|---|---|
| Failed attempts below threshold | No Alert |
| Failed attempts reach threshold | MEDIUM |
| Failed attempts exceed threshold significantly | HIGH |

The risk classification is intended for basic security monitoring and demonstration purposes.

## 📊 Sample Output

```text
IP Address : 192.168.1.10
Attempts   : 5
Risk Level : HIGH
Alert      : Repeated failed login activity detected.

IP Address : 10.0.0.15
Attempts   : 3
Risk Level : MEDIUM
Alert      : Repeated failed login activity detected.

Analysis completed successfully.
```

## 🚀 How to Run

### 📥 Clone Repository

```bash
git clone https://github.com/nithyashree-24/LogShield.git
cd LogShield
```

### ▶️ Run the Analyzer

```bash
python log_analyzer.py
```

### 📄 Analyze the Sample Log

Make sure the following files are present in the project folder:

```text
config.json
sample_logs.txt
log_analyzer.py
requirements.txt
```

The analyzer reads the configured log file and applies the threshold specified in `config.json`.

## 🧪 Testing

LogShield was tested using sample authentication logs containing:

- Successful login attempts
- Repeated failed login attempts
- Multiple source IP addresses
- Different failed-attempt counts

The analyzer successfully identified repeated failed login activity and generated corresponding risk levels and alerts.

## 🎯 Project Objective

The objective of LogShield is to demonstrate a basic security log analysis technique using Python.

The project focuses on detecting repeated authentication failures, identifying potentially suspicious source IP addresses, and generating basic security alerts through configurable monitoring rules.

## 🔮 Future Enhancements

- 🔹 **Real-Time Log Monitoring**

  Monitor authentication logs continuously and detect suspicious activity as it occurs.

- 🔹 **IP Reputation Checking**

  Integrate external threat-intelligence sources to check suspicious IP addresses.

- 🔹 **Automated Alerting**

  Generate security alerts through email, notifications, or security monitoring platforms.

- 🔹 **Advanced Detection Rules**

  Detect brute-force patterns, unusual login times, repeated authentication failures, and abnormal login behaviour.

- 🔹 **Security Dashboard**

  Build a graphical dashboard for visualizing login activity, suspicious IPs, risk levels, and security events.

- 🔹 **Log Export**

  Export analysis results into CSV or JSON formats for further investigation.

## ⚠️ Security Note

This project is intended for educational and defensive security purposes.

The detected activity is based on predefined log patterns and should not be treated as proof of malicious behaviour.

