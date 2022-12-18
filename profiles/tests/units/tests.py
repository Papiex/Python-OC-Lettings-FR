from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_profile_index_should_return_200(client):
    response = client.get(reverse("profiles:index"))
    response_data = response.content.decode()

    assert response.status_code == 200
    assert "Profiles" in response_data
    assert "Home" in response_data
    assert "Lettings" in response_data


@pytest.mark.django_db
def test_profile_should_return_200(client, create_profile):
    profile_object = create_profile
    profile = reverse("profiles:profile", args=[profile_object.user])
    response = client.get(profile)
    response_data = response.content.decode()

    assert response.status_code == 200
    assert "test_user" in response_data
    assert "favorite_city_test" in response_data
