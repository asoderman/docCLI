import unittest
from unittest.mock import Mock, patch

from click.testing import CliRunner
from nose.tools import assert_equal, assert_true

from docCLI.sheets import open_sheets

class TestSheets:

	@classmethod
	def setup_class(cls):
		cls.runner = CliRunner()

	@classmethod
	def teardown_class(cls):
		pass

	@patch('docCLI.sheets.webbrowser.open')
	def test_open_sheets_no_arg(self, op):
		result = self.runner.invoke(open_sheets, [])
		assert_true(op.called)
		assert_equal(result.exit_code, 0)

