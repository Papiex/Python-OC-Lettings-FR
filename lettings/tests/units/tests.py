from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_index_should_return_200(client):
    response = client.get(reverse("lettings:index"))
    response_data = response.content.decode()

    assert response.status_code == 200
    assert "Lettings" in response_data
    assert "Profiles" in response_data
    assert "Home" in response_data


@pytest.mark.django_db
def test_letting_should_return_200(client, create_letting):
    letting_object = create_letting
    letting = reverse("lettings:letting", kwargs={"letting_id": letting_object.id})
    response = client.get(letting)
    response_data = response.content.decode()

    assert response.status_code == 200
    assert "title_test" in response_data
    assert "street_test" in response_data
    assert "city_test" in response_data
    assert "state_test" in response_data
    assert "45" in response_data
    assert "143" in response_data
