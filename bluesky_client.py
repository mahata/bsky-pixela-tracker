import requests
from datetime import datetime
from collections import Counter


class BlueskyClient:
    def __init__(self, username, app_password):
        self.username = username
        self.app_password = app_password
        self.auth_url = "https://bsky.social/xrpc/com.atproto.server.createSession"
        self.feed_url = "https://bsky.social/xrpc/app.bsky.feed.getAuthorFeed"
        self.access_jwt = self._authenticate()

    def _authenticate(self):
        auth_payload = {"identifier": self.username, "password": self.app_password}
        auth_response = requests.post(self.auth_url, json=auth_payload)
        auth_data = auth_response.json()
        return auth_data["accessJwt"]

    def get_post_counts(self):
        headers = {"Authorization": f"Bearer {self.access_jwt}"}
        params = {"actor": self.username, "limit": 100}
        feed_response = requests.get(self.feed_url, headers=headers, params=params)
        feed_data = feed_response.json()

        post_dates = [
            datetime.fromisoformat(post["post"]["record"]["createdAt"]).date()
            for post in feed_data["feed"]
        ]
        return Counter(post_dates)
