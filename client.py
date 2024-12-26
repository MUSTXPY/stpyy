
import requests

class MustpyClient:
    def __init__(self, token):
        self.token = token
        self.base_url = f"https://api.example.com/{self.token}/"

    def send_message(self, chat_id, text):
        url = f"{self.base_url}sendMessage"
        payload = {"chat_id": chat_id, "text": text}
        response = requests.post(url, data=payload)
        return response.json()

    def get_updates(self):
        url = f"{self.base_url}getUpdates"
        response = requests.get(url)
        return response.json()
