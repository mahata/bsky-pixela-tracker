import unittest
from datetime import datetime
from unittest.mock import patch
from pixela_client import PixelaClient


class TestPixelaClient(unittest.TestCase):
    def setUp(self):
        self.client = PixelaClient(
            username="test_user", graph_id="test_graph", user_token="test_token"
        )

    @patch("requests.post")
    def test_post_value(self, mock_post):
        mock_post.return_value.text = '{"message":"Success","isSuccess":true}'

        test_date = datetime(2024, 3, 20)
        test_quantity = 5

        result = self.client.post_value(test_date, test_quantity)

        mock_post.assert_called_once_with(
            self.client.base_url,
            headers={"X-USER-TOKEN": "test_token"},
            json={"date": "20240320", "quantity": "5"},
        )

        self.assertEqual(result, '{"message":"Success","isSuccess":true}')


if __name__ == "__main__":
    unittest.main()
