import feedparser

def fetch_entries(feed_url: str) -> list[dict]:
    feed = feedparser.parse(feed_url)
    return [
        {"title": e.title, "link": e.link, "id": e.get("id", e.link)}
        for e in feed.entries
    ]

if __name__ == "__main__":
    # 例：Hacker News RSS
    entries = fetch_entries("https://hnrss.org/frontpage")
    for entry in entries[:5]:
        print(entry["title"])