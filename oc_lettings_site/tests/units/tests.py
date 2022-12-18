import pytest


@pytest.mark.django_db
def test_index_should_return_200(client):
    response = client.get("")
    response_data = response.content.decode()

    assert response.status_code == 200
    assert "Welcome to Holiday Homes" in response_data
