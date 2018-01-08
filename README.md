# docCLI
A command line interface for Google Docs/Drive/Sheets.

[![Documentation Status](https://readthedocs.org/projects/doccli/badge/?version=latest)](http://doccli.readthedocs.io/en/latest/?badge=latest) [![Build Status](https://travis-ci.org/asoderman/docCLI.svg?branch=travis)](https://travis-ci.org/asoderman/docCLI)


## What can it do?
- Open Google Docs/Drive/Sheets in your browser.
- Open a Google Docs/Drive/Sheets file in your browser.
- Download Google Docs/Drive/Sheets files to your current directory.
- Upload a file to Google Docs/Drive/Sheets.
- Open a local copy of a Google Docs file in your favorite command line editor.

## How do I get it?

Download this repo and run the setup.py with python3.6

## Usage:

All scripts contain a help option. Use ```[SCRIPT] --help``` to access it. The
base commands are ```docs``` ```drive``` and ```sheets```.

### Docs:
- ```docs``` to open the Google Docs page.
- ```docs [FILENAME] ``` to open (in your web browser) a Google Docs file that is in your drive.
- ```docs [FILENAME] -d``` to download the Document from your Google Drive.
- ```docs [FILENAME] -e [EDITOR]``` downloads then opens the local copy in the editor provided.
Defaults to the EDITOR env variable and if that is not found it defaults to vim.

### Drive:
- ```drive``` to open your Google Drive page.
- ```drive [FILENAME]``` to open a file in your Google Drive.
- ```drive [FILENAME] -d``` to download the file specified to your current directory.
- ```drive -u [FILENAME]``` to upload a file from your directory to Google Drive.

### Sheets:
- ```sheets``` to open the Google Sheets page.
- ```sheets [FILENAME]``` to open a spreadsheet in your web browser.
- ```sheets [FILENAME] -d --ext [EXTENSION]``` to download the spreadsheet. --ext
specifies the extension defaults to .csv

## TODO:
- python2.7 compatibility
- Improve developer documentation with more details
- Increase unit test coverage
- Implement updating of files after editing locally
- Callback to handle a file from drive after its been downloaded. e.g. playing a .mp3 after it has been
downloaded

## Developer Documentation:
[readthedocs](http://doccli.readthedocs.io/)

If you want to generate the documentation yourself install sphinx and run
```make html``` in the docs directory.
