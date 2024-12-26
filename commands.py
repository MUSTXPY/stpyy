
import time
from mustpy.client import MustpyClient

class MustpyBot:
    def __init__(self, token):
        self.client = MustpyClient(token)
        self.last_update_id = None

    def listen(self):
        while True:
            updates = self.client.get_updates()
            if updates['result']:
                for update in updates['result']:
                    update_id = update['update_id']
                    if update_id != self.last_update_id:
                        self.last_update_id = update_id
                        chat_id = update['message']['chat']['id']
                        text = update['message']['text']

                        # Example of handling a command
                        if text.lower() == "/start":
                            self.client.send_message(chat_id, "Hello, I'm your bot!")
                        else:
                            self.client.send_message(chat_id, "I received your message.")
            time.sleep(1)
