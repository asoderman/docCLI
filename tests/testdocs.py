import unittest
from unittest.mock import Mock, patch

from click.testing import CliRunner
from nose.tools import assert_equal, assert_true, assert_in

from docCLI.docs import open_docs

class TestDocs:

	@classmethod
	def setup_class(cls):
		cls.runner = CliRunner()

	@classmethod
	def teardown_class(cls):
		cls.runner =  None

	@patch('docCLI.docs.webbrowser.open')
	def test_open_docs_no_arg(self, op):
		'''
		Ensures the script runs properly when nothing is passed to it.
		'''
		result = self.runner.invoke(open_docs, [])
		assert_equal(result.exit_code, 0)
		assert_true(op.called)

	@patch('docCLI.docs.webbrowser.open')
	def test_open_docs_filename(self, op):
		'''
		Ensures a url is created and opened when a filename is passed to
		the script.
		'''
		with patch('docCLI.docs.get_file_id') as get:
			with patch('docCLI.docs.create_url_creator') as creator:
				creator.return_value = lambda x: 'google.com/doc/{}5'.format(x)
				get.return_value = '1234' # Test file id
			
				result = self.runner.invoke(open_docs, ['testfile'])

				get.assert_called_with('testfile')
				op.assert_called_with('google.com/doc/12345', 2)

	def test_open_docs_download(self):
		'''
		Ensures download function is called 
		when the script is called with the download flag.
		'''
		with patch('docCLI.docs.get_file_id') as get:
			with patch('docCLI.docs.download_file') as download:
				get.return_value = '1234'

				self.runner.invoke(open_docs, ['testfile', '-d'])

				download.assert_called_with('testfile', '1234', '.docx', callback=None)

	def test_open_docs_edit(self):
		'''
		Ensures the editor is opened if requested.
		'''
		def mock_handler():
			pass
		with patch('docCLI.docs.get_file_id') as get:
			with patch('docCLI.docs.download_file') as download:
				with patch('docCLI.docs.create_handler') as creator:
					
					get.return_value = '1234'
					creator.return_value = mock_handler

					self.runner.invoke(open_docs, ['testfile', '-e'])

					creator.assert_called_with(None)
					download.assert_called_with('testfile', '1234', '.txt', 
						callback=creator.return_value)

