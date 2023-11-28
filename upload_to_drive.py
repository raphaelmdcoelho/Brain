import os
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account
from googleapiclient.discovery import build

def get_drive_service():
    creds = service_account.Credentials.from_service_account_file(
        'service_account.json', 
        scopes=['https://www.googleapis.com/auth/drive']
    )
    return build('drive', 'v3', credentials=creds)

def find_file(service, name, folder_id):
    response = service.files().list(q=f"name='{name}' and '{folder_id}' in parents",
                                    spaces='drive',
                                    fields='files(id, name)').execute()
    for file in response.get('files', []):
        # Assuming first match is the file to update
        return file.get('id')
    return None

def upload_or_update_file(filename, filepath, mimetype, folder_id):
    service = get_drive_service()
    file_id = find_file(service, filename, folder_id)

    file_metadata = {'name': filename, 'parents': [folder_id]}
    media = MediaFileUpload(filepath, mimetype=mimetype)

    if file_id:
        updated_file = service.files().update(fileId=file_id, body=file_metadata, media_body=media).execute()
        print(f"Updated File ID: {updated_file.get('id')}")
    else:
        new_file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print(f"New File ID: {new_file.get('id')}")

folder_id = 'your-folder-id-here'  # Replace with your actual folder ID
upload_or_update_file('markdown_files.zip', 'markdown_files.zip', 'application/zip', folder_id)
