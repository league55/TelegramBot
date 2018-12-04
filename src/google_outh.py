import logging
import os

import httplib2
import google_auth_oauthlib.flow
from googleapiclient import errors
from googleapiclient.discovery import build

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
    flow = get_oauth_flow(None)
    flow.redirect_uri = 'https://telegramdrivebot.herokuapp.com/oauth'

    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true')

    return authorization_url


def get_oauth_flow(state):
    flow = google_auth_oauthlib.flow.Flow.from_client_config(
        CLIENT_CONFIG,
        scopes=[
            'https://www.googleapis.com/auth/drive',
            "https://www.googleapis.com/auth/userinfo.email",
            "https://www.googleapis.com/auth/plus.me"
        ],
        state=state)
    return flow


def get_user_info(credentials):
    user_info_service = build(
    serviceName='oauth2', version='v2',
    http=credentials.authorize(httplib2.Http()))

    user_info = None
    try:
        user_info = user_info_service.userinfo().get().execute()
    except errors.HttpError as e:
        logging.error('An error occurred: %s', e)
    if user_info and user_info.get('id'):
        return user_info
    else:
        raise Exception()
