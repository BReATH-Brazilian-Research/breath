import httplib2

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from oauth2client.service_account import ServiceAccountCredentials

scopes = ["https://www.googleapis.com/auth/userinfo.email", "openid"]

flow = InstalledAppFlow.from_client_secrets_file("client_secret_pc.json", scopes)
credendials = flow.run_local_server(port=0)
with open('token.json', 'w') as token:
    token.write(credendials.to_json())
print("\n\n")



service = build("oauth2", "v2", credentials=credendials)

userinfo = service.userinfo().get().execute()

print(userinfo)