import json
import os
import requests
from datetime import datetime
from collections import Counter
from dotenv import load_dotenv

# API Settings
load_dotenv()
USERNAME = os.getenv("BSKY_USERNAME")
PASSWORD = os.getenv("BSKY_APP_PASSWORD")
AUTH_URL = "https://bsky.social/xrpc/com.atproto.server.createSession"
FEED_URL = "https://bsky.social/xrpc/app.bsky.feed.getAuthorFeed"

# Authentication
auth_payload = {"identifier": USERNAME, "password": PASSWORD}
auth_response = requests.post(AUTH_URL, json=auth_payload)
auth_data = auth_response.json()
access_jwt = auth_data["accessJwt"]

# Fetch Posts
headers = {"Authorization": f"Bearer {access_jwt}"}
params = {"actor": USERNAME, "limit": 100}
feed_response = requests.get(FEED_URL, headers=headers, params=params)
feed_data = feed_response.json()

# Count Posts by Date
post_dates = [datetime.fromisoformat(post["post"]["record"]["createdAt"]).date() for post in feed_data["feed"]]
post_count = Counter(post_dates)

# Display Results
for date, count in sorted(post_count.items())[1:]:
    print(f"{date}: {count} posts")
