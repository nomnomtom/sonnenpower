import pytest

from main import validate

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


class TestValidate:
    def test_validate_ok(self):
        result = validate(params1)
        assert result["data"]["attributes"]["list"][0]["power"] == "12"

    def test_validate_str_conv_ok(self):
        result = validate(params2)
        assert type(result) == dict

    def test_validate_invalid_value(self):
        with pytest.raises(ValueError) as ve:
            validate(params3)

        assert "Malformed query" in str(ve)
