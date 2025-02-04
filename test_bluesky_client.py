import unittest
from unittest.mock import patch
from datetime import date
from bluesky_client import BlueskyClient
from collections import Counter


class TestBlueskyClient(unittest.TestCase):
    def setUp(self):
        self.username = "test_user"
        self.app_password = "test_password"

    @patch("requests.post")
    def test_authenticate(self, mock_post):
        mock_post.return_value.json.return_value = {"accessJwt": "test_jwt_token"}

        client = BlueskyClient(self.username, self.app_password)

        mock_post.assert_called_once_with(
            "https://bsky.social/xrpc/com.atproto.server.createSession",
            json={"identifier": self.username, "password": self.app_password},
        )

        self.assertEqual(client.access_jwt, "test_jwt_token")

    @patch("requests.get")
    @patch("requests.post")
    def test_get_post_counts(self, mock_post, mock_get):
        mock_post.return_value.json.return_value = {"accessJwt": "test_jwt_token"}

        mock_get.return_value.json.return_value = {
            "feed": [
                {"post": {"record": {"createdAt": "2024-03-20T10:00:00Z"}}},
                {"post": {"record": {"createdAt": "2024-03-20T15:00:00Z"}}},
                {"post": {"record": {"createdAt": "2024-03-21T10:00:00Z"}}},
            ]
        }

        client = BlueskyClient(self.username, self.app_password)
        result = client.get_post_counts()

        mock_get.assert_called_once_with(
            "https://bsky.social/xrpc/app.bsky.feed.getAuthorFeed",
            headers={"Authorization": "Bearer test_jwt_token"},
            params={"actor": self.username, "limit": 100},
        )

        expected_counts = Counter({date(2024, 3, 20): 2, date(2024, 3, 21): 1})
        self.assertEqual(result, expected_counts)


if __name__ == "__main__":
    unittest.main()
