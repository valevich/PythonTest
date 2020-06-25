#!/usr/bin/env python

from __future__ import print_function
import os

from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
    
SCOPES = 'https://www.googleapis.com/auth/drive.file'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets(
            'credentials.json', scope=SCOPES)
    creds = tools.run_flow(flow, store, flags) \
            if flags else tools.run(flow, store)

#DRIVE = build('drive', 'V3', http=creds.authorize(Http()))
DRIVE = build('drive', 'v3', credentials=creds)

FILES = (
    ('hello.txt', None),
# =========  Convert to Google Docs Logic  =============
#    ('hello.txt', 'application/vnd.google-apps.document'),
)

for filename, mimeType in FILES:
    metadata = {'name': filename}
    if mimeType:
        metadata['mimeType'] = mimeType
    res = DRIVE.files().create(body=metadata, media_body=filename).execute()
    if res:
        print('Uploaded "%s" (%s)' % (filename, res['mimeType']))

# =========  Download Logic  =============
#if res:
#    MIMETYPE = 'application/pdf'
#    data = DRIVE.files().export(fileId=res['id'], mimeType=MIMETYPE).execute()
#    if data:
#        fn = '%s.pdf' % os.path.splitext(filename)[0]
#        with open(fn, 'wb') as fh:
#            fh.write(data)
#        print('Downloaded "%s" (%s)' % (fn, MIMETYPE))

