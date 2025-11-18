import pytest
from tests.utils.helpers import get, post

@pytest.fixture
def api_client():
    """Reusable API client fixture."""
    class Client:
        def get(self, endpoint):
            return get(endpoint)

        def post(self, endpoint, data):
            return post(endpoint, data)

    return Client()
