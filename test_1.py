import requests
import pytest
from jsonschema import validate


def test_status_code_200(base_url_dogs):
    res = requests.get(base_url_dogs + "/api/breeds/list/all")
    assert res.status_code == 200


def test_api_json_schema(base_url_dogs):
    res = requests.get(base_url_dogs + "/api/breeds/image/random")

    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "string"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }

    validate(instance=res.json(), schema=schema)


def test_status_code_404(base_url_dogs):
    res = requests.get(base_url_dogs + "/qwerty")
    assert res.status_code == 404


@pytest.mark.parametrize("breed_name, image_url", [
    ('hound-afghan', 'n02088094_1003.jpg'),
    ('hound-basset', 'n02088238_10005.jpg')
])
def test_four(breed_name, image_url):
    res = requests.get('https://images.dog.ceo/breeds/' + breed_name + '/' + image_url)
    assert res.status_code == 200


@pytest.mark.parametrize("url, status", [
    ('https://dog.ceo/api/breeds/image/random', 200),
    ('https://dog.ceo/api/breeds/image/qwerty', 404)
])
def test_five(url, status):
    res = requests.get(url)
    assert res.status_code == status
