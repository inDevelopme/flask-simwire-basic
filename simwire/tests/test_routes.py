import pytest
from .. import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_example_route(client):
    response = client.get('/')  # Update with your actual route
    assert response.status_code == 200