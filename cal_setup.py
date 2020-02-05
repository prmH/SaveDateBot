import config
import pickle
import os.path

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar']


def get_calendar_service():
    credentials = None

    if os.path.exists(config.token_pickle):
        with open(config.token_pickle, 'rb') as token:
            credentials = pickle.load(token)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(config.client_secret_calendar, SCOPES)
            credentials = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(config.token_pickle, 'wb') as token:
            pickle.dump(credentials, token)

    service = build('calendar', 'v3', credentials=credentials)
    return service
