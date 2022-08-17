from unittest import mock

import pytest

from main import _validate, _read_database

params1 = {
    "data": {
        "attributes": {
            "list": [
                {
                    "power": "12",
                    "date": "2019-01-22"
                },
                {
                    "value": "8",
                    "date": "2019-02-22"
                }
            ]
        }
    }
}

params2 = """{
    "data": {
        "attributes": {
            "list": [
                {
                    "power": "6",
                    "date": "2019-01-22"
                }
            ]
        }
    }
}"""

params3 = {
    "data": {
        "attributes": {
            "list": [
                {
                    "power": "12",
                    "date": "2019-01-22"
                },
                {
                    "value": "-8",
                    "date": "2019-02-22"
                }
            ]
        }
    }
}

datacsv = """date_from, value_up_to_10_kwp, value_up_to_30_kwp, value_up_to_40_kwp
2019-01-01, 0.5062, 0.4962, 0.4862
2019-02-01, 0.4810, 0.4710, 0.4610
"""


class TestValidate:
    def test_validate_ok(self):
        result = _validate(params1)
        assert result["data"]["attributes"]["list"][0]["power"] == "12"

    def test_validate_str_conv_ok(self):
        result = _validate(params2)
        assert type(result) == dict

    def test_validate_invalid_value(self):
        with pytest.raises(ValueError) as ve:
            _validate(params3)

        assert "Malformed query" in str(ve)


class TestDatabaseReader:
    def test_read_database_ok(self):
        mocked_open_function = mock.mock_open(read_data=datacsv)
        with mock.patch("builtins.open", mocked_open_function):
            data = _read_database()
            assert len(data) == 2
            assert data[0]["value_up_to_10_kwp"] < 1.0
