import requests


def test_url_status(base_url, status):
    res = requests.get(base_url)
    assert res.status_code == int(status)
