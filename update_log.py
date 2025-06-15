from datetime import datetime

# Write current timestamp to a file
with open("daily_log.txt", "a") as f:
    f.write(f"Run at {datetime.utcnow().isoformat()}Z\n")
