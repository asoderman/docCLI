import io
import os
from functools import partial
from subprocess import call

from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

from docCLI.google import drive_service
from docCLI.mime import MIMETYPES

NEW = 2

EXPORTABLE = ['.doc', '.docx', '.txt', '.csv', '.tsv', '.xls', '.xlsx', '.pdf']

def upload_file(filename):
    '''
    Uploads a file to Google drive and returns the file id
    '''
    service = drive_service()
    metadata = {filename.split('.')[0] : filename}
    media = MediaFileUpload(filename, mimetype=MIMETYPES['.' + filename.split('.')[1]])
    new_file = service.files().create(body=metadata, media_body=media, fields='id').execute()
    return new_file.get('id')

def download_file(filename, file_id, ext, callback=None):
    '''
    Downloads a document/sheet from google docs
    '''
    print('Beginning download for {}'.format(filename))

    filepath = os.path.join(os.getcwd(), filename + ext)

    if not file_id:
        print('File not found')
        return
    if ext in EXPORTABLE:
        request = drive_service().files().export_media(fileId=file_id, mimeType=MIMETYPES[ext])
    else:
        request = drive_service().files().get_media(fileId=file_id)
    file_handler = io.FileIO(filepath, 'w+')
    downloader = MediaIoBaseDownload(file_handler, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()

        print("Download {}%.".format(int(status.progress() * 100)), end="\r")

    print('Download complete.')
    if callback:
        callback(filepath)

def get_file_id(filename):
    '''
    Searches google drive for a file and returns the file id.
    '''
    service = drive_service()

    files_service = service.files()

    request = files_service.list(pageSize=1000, fields='nextPageToken, files(id, name)')

    while request is not None:
        results = request.execute()
        items = results.get('files', [])
        for f in items:
            if f['name'].lower() == filename.lower():
                file_id = f['id']
                return file_id

        request = files_service.list_next(request, results)

    return None

def create_handler(editor=None):
    '''
    Creates the callback function to open the editor.
    Defaults to vim if no editor is passed and there is not an env var set under EDITOR
    '''
    def handler(filepath, editor):
        if editor:
            call([editor, filepath])
        else:
            editor = os.environ.get('EDITOR', 'vim')
            call([editor, filepath])
    return partial(handler, editor=editor)

def create_url_creator(service):
    '''
    Creates the function that will create a url depending on the service
    '''

    def create_url(file_id, service):
        '''
        Create the URL for the webbrowser to open
        '''

        expanded = {'docs' : 'document', 'sheets' : 'spreadsheets'}

        if service.lower() == 'docs' or service.lower() == 'sheets':
            if file_id:
                url = 'https://docs.google.com/{}/d/{}/edit'.format(expanded[service], file_id)
            else:
                url = 'https://google.com/{}'.format(service)
        elif service.lower() == 'drive':
            if file_id:
                pass
            else:
                url = 'https://drive.google.com/drive/my-drive'

        return url

    return partial(create_url, service=service)
