# Configuring Google account authentication

### To generate the necessary credentials for interacting with Google APIs, including Google Drive API, you'll need to set up a project in the Google Cloud Console and create credentials for OAuth 2.0 client IDs.

### Here are the steps to generate the credentials:

- Go to the Google Cloud Console: Visit the Google Cloud Console and sign in with your Google account.

- Create a new project:

  - Click on the project dropdown menu at the top of the page.
  - Click on "New Project".
  - Enter a project name and click "Create".



- Enable the Google Drive API:

  - In the left-hand menu, navigate to "APIs & Services" > "Library".
  - Search for "Google Drive API".
  - Click on "Google Drive API" in the search results.
  - Click "Enable".


- Create OAuth 2.0 credentials:

  - In the left-hand menu, navigate to "APIs & Services" > "Credentials".
  - Click on "Create credentials" and select "OAuth client ID".
  - Choose the application type (for this script, you can choose "Desktop app").
  - Enter a name for the OAuth client ID.
  - Click "Create".
  - Download the credentials:

### After creating the OAuth client ID, you'll be prompted to download the credentials as a JSON file. This file contains your client ID and client secret, which you'll need for authentication.

Get your access and refresh tokens:

You'll need to obtain an access token and a refresh token to authenticate your requests. You can use the OAuth 2.0 authorization flow to get these tokens programmatically. Libraries like google-auth and google-auth-oauthlib provide utilities to handle OAuth authentication and token management. You can refer to the official documentation and examples provided by Google for details on how to implement this flow.
Once you have obtained your client ID, client secret, access token, and refresh token, you can use them in your Python script to authenticate with the Google Drive API and interact with Google Drive. Make sure to keep your credentials secure and never expose them publicly.


![Upload File!](/Uploaded_File.png "Uploaded File")
