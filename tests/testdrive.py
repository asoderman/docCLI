import unittest
from unittest.mock import Mock, patch

from click.testing import CliRunner
from nose.tools import assert_equal, assert_true, assert_in

from docCLI.drive import open_drive

class TestDrive:

	@classmethod
	def setup_class(cls):
		cls.runner = CliRunner()

	@classmethod
	def teardown_class(cls):
		pass

	@patch('docCLI.drive.webbrowser.open')
	def test_open_drive_no_arg(self, op):
		'''
		Ensures the script runs properly when nothing is passed to it
		'''
		result = self.runner.invoke(open_drive, [])
		assert_true(op.called)
		assert_equal(result.exit_code, 0)

	def test_open_drive_download(self):
		with patch('docCLI.drive.get_file_id') as get:
			with patch('docCLI.drive.download_file') as download:
				get.return_value = '1234'

				self.runner.invoke(open_drive, ['testfile.zip', '-d'])
				download.assert_called_with('testfile', '1234', '.zip')
	

