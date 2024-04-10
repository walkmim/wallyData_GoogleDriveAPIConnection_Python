# FIRSTLY YOU NEEED TO INSTALL THESE PYTHON LIBS

# python3 -m pip install --upgrade pip
# python3 -m pip install google-auth
# python3 -m pip install google-api-python-client
# python3 -m pip install google_auth_oauthlib

# https://developers.google.com/identity?hl=pt-br

import os
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Configure your own credentials
client_id = ""
client_secret = ""
filepath = f"C:\Temp\lucianoBrabo.txt"

# Define the scope for Google Drive API
SCOPES = ['https://www.googleapis.com/auth/drive']

#########################################################################################################################

# Define the scope for Google Drive API
SCOPES = ['https://www.googleapis.com/auth/drive']

def generate_tokens(client_id, client_secret):
    """
    Generate access token and refresh token using OAuth 2.0 authorization flow.

    Args:
        client_id (str): OAuth 2.0 client ID.
        client_secret (str): OAuth 2.0 client secret.

    Returns:
        tuple: Tuple containing access token and refresh token.
    """
    flow = InstalledAppFlow.from_client_config(
        client_config={
            "web": {
                "client_id": client_id,
                "client_secret": client_secret,
                "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob"],
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://accounts.google.com/o/oauth2/token",
            }
        },
        scopes=SCOPES
    )
    flow.run_local_server(port=0)

    return flow.credentials.token, flow.credentials.refresh_token



#########################################################################################################################

def authenticate_with_token(token):
    """
    Authenticate user with API token.

    Args:
        token (dict): Token dictionary containing access token, refresh token, etc.

    Returns:
        google.oauth2.credentials.Credentials: Authenticated credentials object.
    """
    creds = Credentials.from_authorized_user_info(token)
    if not creds.valid:
        if creds.expired and creds.refresh_token:
            creds.refresh(Request())
    return creds

def upload_file_to_drive(file_path, token):
    """
    Upload a file to Google Drive.

    Args:
        file_path (str): Path to the file to be uploaded.
        token (dict): Token dictionary containing access token, refresh token, etc.
    """
    creds = authenticate_with_token(token)
    service = build('drive', 'v3', credentials=creds)
    file_name = os.path.basename(file_path)
    file_metadata = {'name': file_name}
    media = MediaFileUpload(file_path, resumable=True)
    file = service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    print('File ID: %s' % file.get('id'))

if __name__ == "__main__":
  
    access_token, refresh_token = generate_tokens(client_id, client_secret)
    print("Access Token:", access_token)
    print("Refresh Token:", refresh_token)
    
    # Replace 'TOKEN' with your token dictionary
    token = {
        "token": access_token,
        "refresh_token": refresh_token,
        "token_uri": "https://oauth2.googleapis.com/token",
        "client_id": client_id,
        "client_secret": client_secret,
        "scopes": SCOPES
    }
    
    upload_file_to_drive(filepath, token)
