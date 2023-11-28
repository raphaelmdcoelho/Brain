import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def get_drive_service():
    creds = service_account.Credentials.from_service_account_file(
        'service_account.json', 
        scopes=['https://www.googleapis.com/auth/drive']
    )
    return build('drive', 'v3', credentials=creds)

def upload_file(filename, filepath, mimetype):
    service = get_drive_service()
    file_metadata = {'name': filename}
    media = MediaFileUpload(filepath, mimetype=mimetype)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"File ID: {file.get('id')}")

upload_file('markdown_files.zip', 'markdown_files.zip', 'application/zip')