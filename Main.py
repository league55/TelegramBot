import requests
import datetime
from time import sleep

TOKEN = "555204475:AAG1RrFFPbC0IiWOUglWKnfZtgvbLWspB5s"
url = "https://api.telegram.org/bot" + TOKEN + "/"


class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, timeout=30, offset=None):
        params = {'timeout': timeout, 'offset': offset}
        response = requests.get(self.api_url + "getUpdates", params)
        return response.json()['result']

    def get_last_update(self):
        get_results = self.get_updates(self)
        if len(get_results) > 0:
            last_update = get_results[-1]
        else:
            last_update = get_results[len(get_results)]

        return last_update

    def send_message(self, chat, text):
        params = {'chat_id': chat, 'text': text}
        response = requests.post(self.api_url + 'sendMessage', data=params)
        return response


greet_bot = BotHandler(TOKEN)
greetings = ('hello', 'hi', 'greetings', 'sup')
now = datetime.datetime.now()


def main():
    new_offset = None
    today = now.day
    hour = now.hour
    while True:
        greet_bot.get_updates(offset=new_offset)
        last_update = greet_bot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
            greet_bot.send_message(last_chat_id, 'Good Morning  {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
            greet_bot.send_message(last_chat_id, 'Good Afternoon {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
            greet_bot.send_message(last_chat_id, 'Good Evening  {}'.format(last_chat_name))
            today += 1

        new_offset = last_update_id + 1

        if __name__ == '__main__':
            try:
                main()
            except KeyboardInterrupt:
                exit()
