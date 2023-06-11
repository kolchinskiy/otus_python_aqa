import requests
import pytest
from jsonschema import validate


def test_status_code_200(base_url_typicode):
    res = requests.get(base_url_typicode + "/posts/1")
    assert res.status_code == 200


def test_api_json_schema(base_url_typicode):
    res = requests.get(base_url_typicode + "/posts/1")

    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "title": {"type": "string"},
            "body": {"type": "string"},
            "userId": {"type": "number"}
        },
        "required": ["id", "title", "body", "userId"]
    }

    validate(instance=res.json(), schema=schema)


def test_status_code_404(base_url_typicode):
    res = requests.get(base_url_typicode + "/posts/qwerty")
    assert res.status_code == 404


@pytest.mark.parametrize('userId',
                         [1, 2, 3, 4, 5])
def test_four(base_url_typicode, userId):
    assert requests.get(base_url_typicode + "/posts", params={'userId': userId}).json() != []


@pytest.mark.parametrize('word',
                         ['albums', 'todos', 'posts'])
def test_five(base_url_typicode, word):
    assert requests.get(base_url_typicode + "/users/1/" + word) != []
