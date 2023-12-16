import pytest
import requests

@pytest.fixture(scope="class")
def fixture_ramdom(request):
    response = requests.request(method="GET", url="https://api.chucknorris.io/jokes/random")
    request.cls.response = response
#    yield response # закоментував, оскільки з класом працює і без нього


@pytest.fixture(scope="class")
def fixture_query(request):
    response = requests.request(method="GET", url="https://api.chucknorris.io/jokes/search?query=fishing")
    status_code = response.status_code
    request.cls.response = response
    request.cls.status_code = status_code
#    yield response # закоментував, оскільки з класом працює і без нього
