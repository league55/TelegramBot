#!/usr/bin/env python
import os

import telegram
from flask import Flask, request, url_for
from oauth2client.file import Storage

from src.dispatcher import react_to_message
from src.google_outh import get_oauth_flow, get_user_info
from src.storage import get_chat_for_email


app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

TOKEN = os.environ['BOT_TOKEN']

bot = telegram.Bot(token=TOKEN)

store = {}

@app.route('/oauth', methods=['GET'])
def oauth2callback():
    state = request.args.get("state")
    flow = get_oauth_flow(state)

    flow.redirect_uri = url_for('oauth2callback', _external=True)

    authorization_response = request.url
    flow.fetch_token(authorization_response=authorization_response)
    credentials = flow.credentials

    print(credentials)
    usr_info = get_user_info(credentials)
    print(usr_info)
    email = usr_info.get("email")
    chat_id = get_chat_for_email(email)

    if chat_id:
        storage = Storage('stores/' + email)
        storage.put(credentials)
        bot.sendMessage(chat_id=chat_id, text="Granted access to Goodle Drive success. Now send me some docs")

    return 'ok'

@app.route('/hook', methods=['POST'])
def webhook_handler():
    if request.method == "POST":
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
