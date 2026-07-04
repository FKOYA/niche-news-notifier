from fetcher import fetch_entries

def test_fetch_entries_returns_list():
    # 実際のネットワークに依存しないよう、後でmock化するのが望ましい発展課題
    entries = fetch_entries("https://hnrss.org/frontpage")
    assert isinstance(entries, list)