import re
import json
from collections import Counter
from datetime import datetime
CONFIG_FILE = "config.json"
def load_config():
    """Load monitoring settings from config.json."""
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "failed_attempt_threshold": 3,
            "log_file": "sample_logs.txt",
            "alert_enabled": True
        }
def analyze_logs():
    config = load_config()
    log_file = config.get("log_file", "sample_logs.txt")
    threshold = config.get("failed_attempt_threshold", 3)
    alert_enabled = config.get("alert_enabled", True)
    failed_ips = []
    total_events = 0
    pattern = r"Failed login attempt IP=([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)"
    try:
        with open(log_file, "r", encoding="utf-8") as file:
            for line in file:
                total_events += 1
                match = re.search(pattern, line)
                if match:
                    failed_ips.append(match.group(1))
    except FileNotFoundError:
        print(f"\nError: {log_file} was not found.")
        return
    ip_counts = Counter(failed_ips)
    print("\n" + "=" * 50)
    print("              LOGSHIELD")
    print("=" * 50)
    print(f"Log file       : {log_file}")
    print(f"Total events   : {total_events}")
    print(f"Failed logins  : {len(failed_ips)}")
    print(f"Alert threshold: {threshold}")
    print("=" * 50)
    if not ip_counts:
        print("\nNo failed login attempts detected.")
        return
    print("\nSuspicious Activity:")
    for ip, count in ip_counts.items():
        if count >= threshold:
            risk = "HIGH" if count >= threshold + 2 else "MEDIUM"
            print(f"\nIP Address : {ip}")
            print(f"Attempts   : {count}")
            print(f"Risk Level : {risk}")
            if alert_enabled:
                print("Alert      : Repeated failed login activity detected.")
    print("\nAnalysis completed at:",
          datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 50)
if __name__ == "__main__":
    analyze_logs()
