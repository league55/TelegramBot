from src.google_outh import get_auth_url

import re

import telegram
from .storage import add_email

pattern = re.compile(".+\@.+\..+")


def react_to_message(bot, json):
    update = telegram.Update.de_json(json, bot)

    text = update.message.text
    chat_id = update.message.chat.id

    if pattern.match(text):
        add_email(chat_id, text)

        url = get_auth_url()
        bot.sendMessage(chat_id=chat_id, text=url)
    else:
        bot.sendMessage(chat_id=chat_id, text="Please enter valid google email address")

