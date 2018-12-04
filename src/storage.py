chat_email = {}

def add_email(chat_id, email):
    chat_email[chat_id] = email

def get_email_for_chat(chat_id):
    return chat_email[chat_email]

def get_chat_for_email(cur_email):
    for chat, email in chat_email:
        print(email)
        if email == cur_email:
            return chat