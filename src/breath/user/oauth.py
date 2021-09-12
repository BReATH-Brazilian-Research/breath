import os
import logging

import streamlit

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow


def google_oauth_login():
    '''
        Get user info using Google API.

        Saves info in streamlit session_state.

        Parameters:
            None
        Returns:
            None
    '''

    logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)

    scopes = ["https://www.googleapis.com/auth/userinfo.email", "openid"]

    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', scopes)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret_pc.json', scopes)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build("oauth2", "v2", credentials=creds)

    userinfo = service.userinfo().get().execute()


    streamlit.session_state.token = creds
    streamlit.session_state.email = userinfo["email"]
    streamlit.session_state.google_login = True