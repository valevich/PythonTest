#!/usr/bin/env python

from __future__ import print_function
from gdrive_updatefunction import *
from googleapiclient import errors
from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

def get_authenticated(SCOPES, credential_file='credentials.json',
                  token_file='token.json', service_name='drive',
                  api_version='v3'):
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage(token_file)
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(credential_file, SCOPES)
        creds = tools.run_flow(flow, store)
    service = build(service_name, api_version, http=creds.authorize(Http()))
    return service


def retrieve_all_files(service):
    """Retrieve a list of File resources.

    Args:
        service: Drive API service instance.
    Returns:
        List of File resources.
    """

    result = []
    page_token = None
    while True:
        try:
            param = {}
            if page_token:
                param['pageToken'] = page_token
            files = service.files().list(**param).execute()

            result.extend(files['files'])
            page_token = files.get('nextPageToken')
            if not page_token:
                break
        except errors.HttpError as error:
            print('An error occurred: %s' % error)
            break

    return result


def insert_file(service, name, description, parent_id, mime_type, filename):
    """Insert new file.

    Args:
        service: Drive API service instance.
        name: Name of the file to insert, including the extension.
        description: Description of the file to insert.
        parent_id: Parent folder's ID.
        mime_type: MIME type of the file to insert.
        filename: Filename of the file to insert.
    Returns:
        Inserted file metadata if successful, None otherwise.
    """
    media_body = MediaFileUpload(filename, mimetype=mime_type, resumable=True)
    body = {
        'name': name,
        'description': description,
        'mimeType': mime_type
    }
    # Set the parent folder.
    if parent_id:
        body['parents'] = [{'id': parent_id}]

    try:
        file = service.files().create(
            body=body,
            media_body=media_body).execute()

        # Uncomment the following line to print the File ID
        #print ('File ID: %s' % file['id'])

        return file
    except errors.HttpError as error:
        print('An error occurred: %s' % error)
        return None


# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/drive'

def main():
    service = get_authenticated(SCOPES)
    service.about().get(fields = "user, storageQuota").execute()

    # Call the Drive v3 API
    results = retrieve_all_files(service)

    target_file_descr = 'Description of hello.txt'
    target_file = 'hello2.txt'
    target_file_name = target_file
    target_file_id = [file['id'] for file in results if file['name'] == target_file_name]

    if len(target_file_id) == 0:
        print('No file called %s found in root. Create it:' % target_file_name)
        file_uploaded = insert_file(service, target_file_name, target_file_descr, None,
                                'text/x-script.phyton', target_file_name)
    else:
        print('File called %s found. Update it:' % target_file_name)
        file_uploaded = update_file(service, target_file_id[0], target_file_name, target_file_descr,
                                'text/x-script.phyton', target_file_name)

    print(str(file_uploaded))


if __name__ == '__main__':
    main()