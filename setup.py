from setuptools import setup, find_packages

setup(
	name='docCLI',
	version='0.0.1',
	install_requires=[
		'Click',
		'google-api-python-client'
		],
	packages=find_packages(),
	entry_points='''
	[console_scripts]
	docs=docCLI.docs:open_docs
	drive=docCLI.drive:open_drive
	sheets=docCLI.sheets:open_sheets
	'''
	)