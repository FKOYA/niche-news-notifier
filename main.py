import json
import os
from pathlib import Path
from fetcher import fetch_entries
from notifier import send_email

SEEN_FILE = Path("seen_articles.json")
FEED_URL = "https://hnrss.org/frontpage"

def load_seen() -> set:
    if SEEN_FILE.exists():
        return set(json.loads(SEEN_FILE.read_text()))
    return set()

def save_seen(seen: set):
    SEEN_FILE.write_text(json.dumps(list(seen)))

def main():
    seen = load_seen()
    entries = fetch_entries(FEED_URL)
    new_entries = [e for e in entries if e["id"] not in seen]

    if new_entries:
        body = "\n".join(f"- {e['title']}\n  {e['link']}" for e in new_entries)
        send_email(f"新着記事 {len(new_entries)}件", body)
        seen.update(e["id"] for e in new_entries)
        save_seen(seen)

if __name__ == "__main__":
    main()