import requests
import pytest
from jsonschema import validate

schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "address": {"type": "string"},
            "zip": {"type": "string"},
            "country": {"type": "string"},
            "employeeCount": {"type": "integer"},
            "industry": {"type": "string"},
            "marketCap": {"type": "integer"},
            "domain": {"type": "string"},
            "logo": {"type": "string"},
            "ceoName": {"type": "string"}
        },
        "required": [
            "id", "name", "address", "zip", "country",
            "employeeCount", "industry", "marketCap",
            "domain", "logo", "ceoName"
        ]
    }
}

@pytest.mark.api
def test_get_companies():
    url = "https://fake-json-api.mock.beeceptor.com/companies"
    response = requests.get(url)
    assert response.status_code == 200
    try:
        validate(instance=response.json(), schema=schema)
    except Exception as e:
        pytest.fail(f"The JSON response doesnt match with the schema: {e}")

    print("Test passed successfully.")