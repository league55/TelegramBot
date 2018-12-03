import os

import google_auth_oauthlib.flow

CLIENT_CONFIG = {
    "web": {
        "client_id": os.environ['client_id'],
        "project_id": "trim-mile-122420",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://www.googleapis.com/oauth2/v3/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_secret": os.environ['client_secret'],
        "redirect_uris": [
            "https://telegramdrivebot.herokuapp.com/oauth"
        ],
        "javascript_origins": [
            "https://telegram.org",
            "https://t.me",
            "https://web.telegram.org"
        ]
    }
}

def get_auth_url():
    flow = google_auth_oauthlib.flow.Flow.from_client_config(
        CLIENT_CONFIG,
        scopes=['https://www.googleapis.com/auth/drive'])
    flow.redirect_uri = 'https://telegramdrivebot.herokuapp.com/oauth'

    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true')

    return authorization_url
