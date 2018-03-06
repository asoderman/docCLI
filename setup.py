from setuptools import setup, find_packages

setup(
	name='docCLI',
	author='Alex Soderman',
	author_email='asoderman.as@gmail.com',
	url='https://github.com/asoderman/docCLI',
	description='A command line interface for Google Docs suite',
	version='0.0.4',
	install_requires=[
		'Click',
		'google-api-python-client'
		],
	packages=find_packages(),
	package_data={'': ['docCLI/credentials/client_secret.json']},
	include_package_data=True,
	entry_points='''
	[console_scripts]
	docs=docCLI.docs:open_docs
	drive=docCLI.drive:open_drive
	sheets=docCLI.sheets:open_sheets
	'''
	)
