import requests
import pytest
from jsonschema import validate


def test_status_code_200(base_url_brewery):
    res = requests.get(base_url_brewery + "/v1/breweries/meta?by_type=micro")
    assert res.status_code == 200


def test_api_json_schema(base_url_brewery):
    res = requests.get(base_url_brewery + "/v1/breweries/meta?by_type=micro")

    schema = {
        "type": "object",
        "properties": {
            "total": {"type": "string"},
            "page": {"type": "string"},
            "per_page": {"type": "string"}
        },
        "required": ["total", "page", "per_page"]
    }

    validate(instance=res.json(), schema=schema)


def test_status_code_404(base_url_brewery):
    res = requests.get(base_url_brewery + "/qwerty")
    assert res.status_code == 404


@pytest.mark.parametrize("brewery_id", [
    '5128df48-79fc-4f0f-8b52-d06be54d0cec',
    '9c5a66c8-cc13-416f-a5d9-0a769c87d318'
])
def test_four(base_url_brewery, brewery_id):
    res = requests.get(base_url_brewery + '/v1/breweries/' + brewery_id)
    assert res.status_code == 200


@pytest.mark.parametrize("brewery_id_1, brewery_id_2", [
    ('5128df48-79fc-4f0f-8b52-d06be54d0cec', '9c5a66c8-cc13-416f-a5d9-0a769c87d318')
])
def test_five(base_url_brewery, brewery_id_1, brewery_id_2):
    res = requests.get(base_url_brewery + '/v1/breweries?by_ids=' + brewery_id_1 + ',' + brewery_id_2)
    assert res.status_code == 200
