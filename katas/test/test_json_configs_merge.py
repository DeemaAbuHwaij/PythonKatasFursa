import unittest
from unittest.mock import mock_open, patch
import builtins
import json
from katas.json_config_merge import json_configs_merge
# Assume json_configs_merge is defined above or imported

class TestJsonConfigsMerge(unittest.TestCase):

    def setUp(self):
        # Sample mock file contents
        self.default_json = json.dumps({
            "user": {
                "name": "John",
                "age": 30
            },
            "settings": {
                "theme": "light",
                "language": "english"
            }
        })

        self.local_json = json.dumps({
            "user": {
                "age": 31,
                "email": "john@example.com"
            },
            "settings": {
                "language": "spanish",
                "timezone": "UTC+1"
            }
        })

        self.expected_merged = {
            "user": {
                "name": "John",
                "age": 31,
                "email": "john@example.com"
            },
            "settings": {
                "theme": "light",
                "language": "spanish",
                "timezone": "UTC+1"
            }
        }

    @patch("builtins.open")
    def test_merge_two_json_files(self, mock_open_builtin):
        # Setup mock open to return different files depending on call order
        mock_open_builtin.side_effect = [
            mock_open(read_data=self.default_json).return_value,
            mock_open(read_data=self.local_json).return_value
        ]

        result = json_configs_merge("default.json", "local.json")
        self.assertEqual(result, self.expected_merged)

    @patch("builtins.open")
    def test_merge_empty(self, mock_open_builtin):
        mock_open_builtin.return_value = mock_open(read_data="{}").return_value

        result = json_configs_merge("empty.json", "empty.json")
        self.assertEqual(result, {})

    @patch("builtins.open")
    def test_merge_overwrite_entire_key(self, mock_open_builtin):
        mock_open_builtin.side_effect = [
            mock_open(read_data='{"key": {"nested": 1}}').return_value,
            mock_open(read_data='{"key": 2}').return_value
        ]

        result = json_configs_merge("a.json", "b.json")
        self.assertEqual(result, {"key": 2})

if __name__ == '__main__':
    unittest.main()
