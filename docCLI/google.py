import os
import sys
import httplib2

from googleapiclient.discovery import build
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

class NoClientSecretException(Exception):
    pass

SCOPES = 'https://www.googleapis.com/auth/drive'

def get_client_secret():
    try:
        mod = '/'.join(os.path.abspath(__file__).split('/')[0:-1])
        CLIENT_SECRET_FILE = os.path.join(mod,
                                          'credentials/client_secret.json')
        if not os.path.isfile(CLIENT_SECRET_FILE):
            raise NoClientSecretException()
    except NoClientSecretException:
        print('Unable to find client secret. Exiting...')
        sys.exit(1)


APPLICATION_NAME = 'docCLI'

def get_credentials():
    '''Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    '''
    CLIENT_SECRET_FILE = get_client_secret()
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'drive-googleapis.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = tools.run_flow(flow, store)
    return credentials

def drive_service():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = build('drive', 'v3', http=http)
    return service
