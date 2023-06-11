import pytest


@pytest.fixture(scope="session")
def base_url_dogs():
    return "https://dog.ceo"


@pytest.fixture(scope="session")
def base_url_brewery():
    return "https://api.openbrewerydb.org"


@pytest.fixture(scope="session")
def base_url_typicode():
    return "https://jsonplaceholder.typicode.com"


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="This is request url"
    )

    parser.addoption(
        "--status_code",
        default=200,
        help="This is status code"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status(request):
    return request.config.getoption("--status_code")

