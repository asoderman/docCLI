import webbrowser

import click

from docCLI.core import create_url_creator, get_file_id, download_file

NEW = 2

@click.command()
@click.argument('filename', required=False)
@click.option('-d', '--download', is_flag=True, help='Download the sheet to the current dir.')
@click.option('--ext', required=False, help='Specify the extension to download the sheet as. '
    'Defaults to .csv')
def open_sheets(filename=None, no_open=False, download=False, ext=None):
    '''Entry point for the sheets command

    This function is called whenever the sheets command is used. This is intended to be
    used with spreadsheets.

    Parameters
    ----------
    filename : str
        The filename (not including a file extension) as it appears in Google drive.
    no_open : bool
        Flag to suppress opening browser window after uploading a file.
    download : bool
        Flag to download the file to the current working directory instead of opening it
    ext : str
        The file extension to export the document from Google drive as.

    '''

    file_id = None

    if filename:
        file_id = get_file_id(filename)
        if download:
            if ext:
                if not ext.startswith('.'):
                    ext = '.' + ext
                ext = ext.lower()
            else:
                ext = '.csv'
            download_file(filename, file_id, ext)
            return

    url = create_url(file_id)

    if not no_open:
        webbrowser.open(url, NEW)

def create_url(file_id=None):
    f = create_url_creator('sheets')
    return f(file_id)

if __name__ == '__main__':
    open_sheets()
