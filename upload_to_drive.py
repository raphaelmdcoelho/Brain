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

def find_file(service, filename, folder_id):
    results = service.files().list(
        q=f"name='{filename}' and '{folder_id}' in parents",
        spaces='drive',
        fields='files(id, name)').execute()
    items = results.get('files', [])
    return items[0]['id'] if items else None

def upload_or_update_file(filename, filepath, mimetype, folder_id):
    service = get_drive_service()
    file_metadata = {'name': filename}
    media = MediaFileUpload(filepath, mimetype=mimetype)
    
    file_id = find_file(service, filename, folder_id)
    
    if file_id:
        # Update existing file
        service.files().update(
            fileId=file_id,
            body=file_metadata,
            media_body=media,
            addParents=[folder_id],  # Include this if you're moving to a new folder
            # removeParents=[current_parent_id]  # Use if removing from a current folder
        ).execute()
        print(f"Updated File ID: {file_id}")
    else:
        # Upload new file
        file_metadata['parents'] = [folder_id]  # Set parent folder for new file
        file = service.files().create(
            body=file_metadata, 
            media_body=media, 
            fields='id').execute()
        print(f"Uploaded New File ID: {file.get('id')}")

folder_id = '1dQiC-8K0yjKZMuQ97Q87JfUsgg1lBGpI'  # Replace with your actual folder ID
upload_or_update_file('markdown_files.zip', 'markdown_files.zip', 'application/zip', folder_id)

