import webbrowser

import click

from docCLI.core import create_url_creator, get_file_id, upload_file, download_file

NEW = 2

@click.command()
@click.argument('filename', required=False)
@click.option('-u', '--upload', )
@click.option('-n', '--no-open', is_flag=True, help='Upload the file without opening.')
@click.option('-d', '--download', is_flag=True, help='Download the file to the cwd')
def open_drive(filename=None, upload=None, no_open=False, download=False):
    '''Entry point for the drive command

    This function is called whenever the drive command is used. This is intended to be used
    with files that are not docs/sheets (e.g. .mp3, .iso etc).

    Parameters
    ----------
    filename : str
        The filename (including a file extension) as it appears in Google drive.
    upload : str
        The name of the local file (including extension) to be uploaded.
    no_open : bool
        Flag to suppress opening browser window after uploading a file.
    download : bool
        Flag to download the file to the current working directory instead of opening it

    '''

    file_id = None
    create_url = create_url_creator('drive')

    if upload:
        file_id = upload_file(upload)
    elif filename:
        file_id = get_file_id(filename)
        if download:
            name = filename.split('.')[0]
            ext = '.' + filename.split('.')[1]
            download_file(name, file_id, ext)
            return

    if not no_open:
        webbrowser.open(create_url(filename), NEW)

if __name__ == '__main__':
    open_drive()
