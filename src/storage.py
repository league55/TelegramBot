chat_email = {}
email_token = {}


def add_email(chat_id, email):
    chat_email[chat_id] = email


def add_token_for_email(email, token):
    email_token[email] = token


def get_email_for_chat(chat_id):
    return chat_email[chat_email]


def get_token_for_chat(chat_id):
    email = chat_email[chat_id]
    return email_token[email]