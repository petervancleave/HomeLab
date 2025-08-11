import pandas as pd
import re

# Define log file path
auth_log = "/var/log/auth.log"

# Extract SSH login attempts
def parse_ssh_log(file_path):
    data = []
    with open(file_path, "r") as file:
        for line in file:
            if "sshd" in line and ("Accepted" in line or "Failed" in line):
                match = re.search(r'(\w{3} \d{1,2} \d{2}:\d{2}:\d{2}) .* (Accepted|Failed) password for (\w+) from ([\d.]+)', line)
                if match:
                    timestamp, status, user, ip = match.groups()
                    data.append([timestamp, status, user, ip])

    df = pd.DataFrame(data, columns=["Timestamp", "Status", "User", "IP"])
    return df

# Parse logs and save to CSV
df = parse_ssh_log(auth_log)
df.to_csv("ssh_logs.csv", index=False)
print(df.head())
