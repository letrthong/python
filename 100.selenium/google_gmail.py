#
# google-auth-oauthlib https://pypi.org/project/google-auth-oauthlib/
# google-api-python-client https://pypi.org/project/google-api-python-client/
#
# https://developers.google.com/gmail/api/quickstart/python
# https://github.com/googleworkspace/python-samples/blob/master/gmail/quickstart/quickstart.py
#  https://developers.google.com/workspace/guides/create-credentials

from __future__ import print_function

import base64
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


# https://www.base64decode.org/
def decode_base64(text_b64encode):
    try:
        base64_bytes = bytes(text_b64encode, 'utf-8')
        d = base64.b64decode(base64_bytes)
        text = d.decode('utf-8')
        return text
    except:
        return text_b64encode


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    '''
    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            #print(label['name'])
    '''

    result = service.users().messages().list(maxResults=5, userId='me').execute()
    messages = result.get('messages')
    for msg in messages:
        txt = service.users().messages().get(userId='me', id=msg['id']).execute()
        try:
            payload = txt['payload']
            headers = payload['headers']
            # print("Message: ", headers)
            # print("payload: ", payload)
            for item in headers:
                if item['name'] == 'Subject':
                    subject = item['value']
                if item['name'] == 'From':
                    sender = item['value']

            print("Subject: ", subject)
            print("From: ", sender)
            # process body
            parts = payload.get('parts')[0]
            data = parts['body']['data']
            # print("data=", data)
            data = data.replace("-", "+").replace("_", "/")
            decoded_data = decode_base64(data)
            print("decoded_data: ", decoded_data)
            print('\n\n')
        except:
            print("An exception occurred")
            pass


if __name__ == '__main__':
    main()
