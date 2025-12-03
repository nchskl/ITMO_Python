from unittest.mock import Mock, MagicMock

from currencies import logger_using, get_currencies
import unittest
import json
from unittest.mock import patch, MagicMock


class currencies_test(unittest.TestCase):
    def test_currencies(self):
        self.assertEqual(get_currencies(["USD", "EUR"]), {'USD': 77.9556, 'EUR': 90.5903})

    def test_non_exist_currency(self):
        with self.assertRaisesRegex(KeyError, "Валюта отсутствует"):
            get_currencies(["qwerty", "fff"])

    def test_connect_error(self):
        with self.assertRaisesRegex(ConnectionError, "API недоступен"):
            get_currencies(["qwerty", "fff"], url = "https://z")

    @patch('currencies.requests.get')
    def test_key_value_error(self, mock_get):
        fake_response = MagicMock()
        fake_response.status_code = 200
        fake_response.json.return_value = {
            "WrongKey": {"USD": {"Value": 100.0}}
        }
        mock_get.return_value = fake_response

        with self.assertRaises(KeyError):
            get_currencies(['USD', 'EUR'])

    @patch("currencies.requests.get")
    def test_json_error(self, mock_get):
        mock_js = MagicMock()
        mock_js.json.side_effect = json.JSONDecodeError("bad jd", 'x', 0)
        mock_get.return_value = mock_js

        with self.assertRaises(ValueError):
            get_currencies(['USD', 'EUR'])




if __name__ == '__main__':
    unittest.main()