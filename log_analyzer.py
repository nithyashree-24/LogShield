import re
from collections import Counter
from datetime import datetime
LOG_FILE = "sample_logs.txt"
FAILED_LOGIN_PATTERN = re.compile(
    r"(?P<timestamp>\S+\s+\S+).*Failed login.*IP=(?P<ip>\d+\.\d+\.\d+\.\d+)",
    re.IGNORECASE
)
def analyze_logs():
    failed_attempts = []
    ip_counter = Counter()
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            for line in file:
                match = FAILED_LOGIN_PATTERN.search(line)
                if match:
                    timestamp = match.group("timestamp")
                    ip_address = match.group("ip")
                    failed_attempts.append(timestamp)
                    ip_counter[ip_address] += 1
    except FileNotFoundError:
        print(f"\n[ERROR] {LOG_FILE} not found.")
        print("Create the sample_logs.txt file before running the analyzer.")
        return
    print("\n" + "=" * 55)
    print("              LOGSHIELD - SECURITY ANALYZER")
    print("=" * 55)
    print(f"\nTotal failed login attempts : {len(failed_attempts)}")
    print(f"Unique source IPs           : {len(ip_counter)}")
    print("\n--- Suspicious IP Activity ---")
    if not ip_counter:
        print("No failed login activity detected.")
        return
    for ip, count in ip_counter.most_common():
        if count >= 5:
            risk = "HIGH"
        elif count >= 3:
            risk = "MEDIUM"
        else:
            risk = "LOW"
        print(f"IP: {ip:<16} Attempts: {count:<3} Risk: {risk}")
    print("\nAnalysis completed.")
    print("=" * 55)
if __name__ == "__main__":
    analyze_logs()
