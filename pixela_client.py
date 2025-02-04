import requests


class PixelaClient:
    def __init__(self, username, graph_id, user_token):
        self.username = username
        self.graph_id = graph_id
        self.user_token = user_token
        self.base_url = f"https://pixe.la/v1/users/{username}/graphs/{graph_id}"

    def post_value(self, date, quantity):
        headers = {"X-USER-TOKEN": self.user_token}
        payload = {"date": date.strftime("%Y%m%d"), "quantity": str(quantity)}
        response = requests.post(self.base_url, headers=headers, json=payload)
        return response.text
