from django.urls import reverse
import pytest

from lettings.models import Letting, Address


@pytest.mark.django_db
def test_index_should_return_200(client):
    response = client.get(reverse('lettings:index'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_letting_should_return_200(client):
    address = Address.objects.create(
        number = 15,
        street = 'test',
        city = 'test',
        state = 'test',
        zip_code = 45,
        country_iso_code = 143,
    )
    letting_object = Letting.objects.create(
        title = 'test',
        address = address
    )
    letting = reverse('lettings:letting', kwargs={'letting_id': letting_object.id})
    response = client.get(letting)
    assert response.status_code == 200