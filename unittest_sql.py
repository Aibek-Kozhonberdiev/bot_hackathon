import unittest
from unittest.mock import MagicMock
from sql_data import ResultText

class ResultTextTest(unittest.TestCase):
    def setUp(self):
        self.result_text = ResultText('int', "instruction")

    def test_lang_text(self):
        # Mock the database connection and cursor
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [('Instruction value',)]
        mock_connection = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        self.result_text.connection = mock_connection

        # Mock the get_user_language method
        self.result_text.get_user_language = MagicMock(return_value='en')

        # Call the lang_text method
        result = self.result_text.lang_text()

        # Assertions
        self.assertEqual(result, 'Instruction value')
        mock_connection.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once()
        mock_cursor.fetchall.assert_called_once()
        self.result_text.get_user_language.assert_called_once()

    def test_get_user_language(self):
        # Mock the database connection and cursor
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [('en',)]
        mock_connection = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        self.result_text.connection = mock_connection

        # Call the get_user_language method
        result = self.result_text.get_user_language()

        # Assertions
        self.assertEqual(result, 'en')
        mock_connection.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once()
        mock_cursor.fetchall.assert_called_once()

if __name__ == '__main__':
    unittest.main()