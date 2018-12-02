#!/usr/bin/env python

import telegram
from flask import Flask, request

from secret.config import TOKEN

if __name__ == "__main__":
    app = Flask(__name__)
    app.run()

global bot
bot = telegram.Bot(token=TOKEN)

def echo(update):
    chat_id = update.message.chat.id
    text = update.message.text.encode('utf-8')

    bot.sendMessage(chat_id=chat_id, text=text)


def command_to_action(update):
    return echo



@app.route('/hook', methods=['POST'])
def webhook_handler():
    if request.method == "POST":
        # retrieve the message in JSON and then transform it to Telegram object
        update = telegram.Update.de_json(request.get_json(force=True))

        action = command_to_action(update)
        action(update)

    return 'ok'


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('telegramdrivebot.herokuapp.com/hook')
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route('/')
def index():
    return '.'