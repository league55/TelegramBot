#!/usr/bin/env python
import os

import telegram
from flask import request, url_for

from src import app
from src.dispatcher import react_to_message
from src.google_outh import get_oauth_flow, get_user_info, get_oauth_flow_2
from src.storage import get_user_by_field, set_user_credentials

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

    flow2 = get_oauth_flow_2()
    credentials = flow2.step2_exchange(request.args["code"])

    print(credentials)
    usr_info = get_user_info(credentials)
    print(usr_info)
    email = usr_info.get("email")
    chat_id = get_user_by_field("email", email)

    if chat_id:
        set_user_credentials(email, credentials.to_json())
        bot.sendMessage(chat_id=chat_id, text="Granted access to Goodle Drive success. Now send me some docs")

    return 'ok'

@app.route('/hook', methods=['POST'])
def webhook_handler():
    if request.method == "POST":
        print(request.get_json())

        react_to_message(bot, request.get_json(force=True))

    return 'ok'


@app.route('/test', methods=['GET', 'POST'])
def test():
    email = request.args.get("email")
    if email:
        return get_user_by_field("email", email)


@app.route('/')
def index():
    return 'All works'
