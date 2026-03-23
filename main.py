import argparse
import requests
import feedparser
from datetime import datetime, timedelta, timezone
from email_notifier import send_email_notification


ARXIV_API = "http://export.arxiv.org/api/query"

def fetch_recent_hepex(days=3, max_results=100):
    params = {
        "search_query": "cat:hep-ex",
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending"
    }

    response = requests.get(ARXIV_API, params=params)
    feed = feedparser.parse(response.text)

    cutoff = datetime.now(timezone.utc) - timedelta(days=days)

    papers = []
    for entry in feed.entries:
        published = datetime.strptime(entry.published, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)

        if published >= cutoff:
            papers.append({
                "title": entry.title,
                "authors": [a.name for a in entry.authors],
                "link": entry.link,
                "published": entry.published,
                "summary": entry.summary[:300]  # 可截断
            })

    return papers


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch recent hep-ex papers from arXiv")
    parser.add_argument("--days", type=int, default=3, help="Number of days to search back (default: 3)")
    parser.add_argument("--max-results", type=int, default=100, help="Maximum number of results (default: 100)")
    parser.add_argument("--email", action="store_true", help="Send email notification")
    args = parser.parse_args()

    papers = fetch_recent_hepex(days=args.days, max_results=args.max_results)

    print("=" * 80)
    print(f"📚 Recent hep-ex Papers (Last {args.days} Days) - {len(papers)} papers found")
    print("=" * 80)
    print()

    for i, p in enumerate(papers, 1):
        # 格式化日期
        pub_date = p['published'].replace("T", " ").replace("Z", "")
        
        print(f"[{i}] {p['title']}")
        print(f"    📅 Published: {pub_date}")
        print(f"    👤 Authors: {', '.join(p['authors'])}")
        print(f"    📝 Abstract: {p['summary']}...")
        print(f"    🔗 Link: {p['link']}")
        print("-" * 80)
        print()

    # 发送邮件通知
    if args.email:
        send_email_notification(papers, days=args.days)
