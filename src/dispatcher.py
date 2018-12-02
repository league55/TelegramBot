from src.google_outh import get_auth_url
from run import bot

import re

from storage import add_email

pattern = re.compile(".+\@.+\..+")

def echo(update):
    chat_id = update.message.chat.id
    text = update.message.text

    bot.sendMessage(chat_id=chat_id, text=text)


def command_to_action(update):
    text = update.message.text
    chat_id = update.message.chat.id

    if pattern.match(text):
        add_email(chat_id, text)

        url = get_auth_url()
        bot.sendMessage(chat_id=chat_id, text=url)
    else:
        bot.sendMessage(chat_id=chat_id, text="Please enter valid google email address")

    return echo
