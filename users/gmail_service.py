import pickle
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from email.mime.text import MIMEText
import base64

# Load saved OAuth credentials
with open('users/oauth/token.pkl', 'rb') as token_file:
    creds = pickle.load(token_file)

# Refresh token if expired
if creds.expired and creds.refresh_token:
    creds.refresh(Request())

service = build('gmail', 'v1', credentials=creds)

def send_email(to, subject, body, html=False):
    if html:
        message = MIMEText(body, 'html')
    else:
        message = MIMEText(body)
    message['to'] = to
    message['subject'] = subject
    message['from'] = 'PixRevive Team <ezzezze86@gmail.com>' 
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    service.users().messages().send(userId='me', body={'raw': raw}).execute()

