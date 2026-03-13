import json
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("backend/logs/transactions.json")

LOG_FILE.parent.mkdir(parents=True, exist_ok=True)


def log_event(event):

    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "event": event
    }

    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append(entry)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

    print("LOG:", entry)


def get_logs():

    try:
        with open(LOG_FILE) as f:
            return json.load(f)
    except:
        return []