#!/usr/bin/env python
import os

import telegram
from flask import Flask, request

from src.dispatcher import react_to_message

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

TOKEN = os.environ['BOT_TOKEN']

bot = telegram.Bot(token=TOKEN)

store = {}

@app.route('/oauth/<auth_code>', methods=['GET'])
def auth(auth_code):
    if request.method == "GET":
        # retrieve the message in JSON and then transform it to Telegram object
        print(auth_code)

    return 'ok'

@app.route('/hook', methods=['POST'])
def webhook_handler():
    if request.method == "POST":
        # retrieve the message in JSON and then transform it to Telegram object
        print(request.get_json())

        react_to_message(bot, request.get_json(force=True))

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
    return 'All works'
