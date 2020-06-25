# File: gdrive_updatefunction.py
from googleapiclient import errors
from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

def update_file(service, file_id, new_name, new_description, new_mime_type,
            new_filename):

#"""Update an existing file's metadata and content.
#
#Args:
#    service: Drive API service instance.
#    file_id: ID of the file to update.
#    new_name: New name for the file.
#    new_description: New description for the file.
#    new_mime_type: New MIME type for the file.
#    new_filename: Filename of the new content to upload.
#    new_revision: Whether or not to create a new revision for this file.
#Returns:
#    Updated file metadata if successful, None otherwise.
#"""
    
    try:
        # First retrieve the file from the API.
        file = service.files().get(fileId=file_id).execute()

#        # File's new metadata.
        del file['id']      
#        file['name'] = new_name
#        file['description'] = new_description
#        file['mimeType'] = new_mime_type
#        file['trashed'] = True

        # File's new content.
        media_body = MediaFileUpload(
            new_filename, mimetype=new_mime_type, resumable=True)

        # Send the request to the API.
        updated_file = service.files().update(
            fileId=file_id,
            body=file,
            media_body=media_body).execute()
        return updated_file
    except errors.HttpError as error:
        print('An error occurred: %s' % error)
        return None