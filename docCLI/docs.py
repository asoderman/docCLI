import webbrowser

import click

from docCLI.core import upload_file, create_url_creator, get_file_id, download_file, create_handler

NEW = 2

@click.command()
@click.argument('filename', required=False)
@click.option('-u', '--upload', help='Use this to upload a file to your drive.')
@click.option('-n', '--no-open', is_flag=True, help='Use this to cancel opening the webbrowser '
              'after uploading your file.')
@click.option('-d', '--download', is_flag=True, help='Download the file instead of opening it '
              'in browser')
@click.option('-e', '--edit', is_flag=True, help='Download the document in a txt format and open '
              'with your editor. Specify an editor after this flag or set an env var for EDITOR. '
              'If neither is supplied defaults to vim')
@click.argument('editor', required=False)
@click.option('--ext', help='Specify the file extension for downloading.')
def open_docs(filename=None, upload=None, no_open=False, download=False, edit=False,
              editor=None, ext=None):
    '''Entry point for the docs command

    This function is called whenever the docs command is used.

    Parameters
    ----------
    filename : str
        The filename (not including a file extension) as it appears in Google drive.
    upload : str
        The name of the local file (including extension) to be uploaded.
    no_open : bool
        Flag to suppress opening browser window after uploading a file.
    download : bool
        Flag to download the file to the current working directory instead of opening it
    edit : bool
        Flag to download the file and open the local copy for editing with a command line text
        editor. Downloads the document in .txt format unless specified.
    editor : str
        The editor to open the downloaded file with.
    ext : str
        The file extension to export the document from Google drive as.

    '''
    file_id = None

    if upload:
        file_id = upload_file(upload)

    elif filename:

        file_id = get_file_id(filename)

        if not file_id:
            print('Could not locate: {}'.format(filename))
            return
        elif download or edit:
            if edit:
                callback = create_handler(editor)
                if not ext:
                    ext = '.txt'
            else:
                callback = None
                if not ext:
                    ext = '.docx'

            download_file(filename, file_id, ext, callback=callback)

            return

    create_url = create_url_creator('docs')
    url = create_url(file_id)

    if not no_open:
        webbrowser.open(url, NEW)

if __name__ == '__main__':
    open_docs()
