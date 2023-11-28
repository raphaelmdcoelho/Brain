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

def delete_existing_file(service, filename, folder_id):
    # Find the file in the specified folder
    response = service.files().list(q=f"name='{filename}' and '{folder_id}' in parents",
                                    spaces='drive',
                                    fields='files(id, name)').execute()
    for file in response.get('files', []):
        # Delete the file
        service.files().delete(fileId=file.get('id')).execute()

def upload_file(filename, filepath, mimetype, folder_id):
    service = get_drive_service()
    delete_existing_file(service, filename, folder_id)
    
    file_metadata = {'name': filename, 'parents': [folder_id]}
    media = MediaFileUpload(filepath, mimetype=mimetype)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"File ID: {file.get('id')}")

folder_id = '1dQiC-8K0yjKZMuQ97Q87JfUsgg1lBGpI'
upload_file('markdown_files.zip', 'markdown_files.zip', 'application/zip', folder_id)
