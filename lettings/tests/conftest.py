import pytest

from lettings.models import Letting, Address


@pytest.fixture
def create_address() -> Address:
    """create and return address"""
    address = Address.objects.create(
        number=15,
        street="street_test",
        city="city_test",
        state="state_test",
        zip_code=45,
        country_iso_code=143,
    )
    return address


@pytest.fixture
def create_letting(create_address) -> Letting:
    """create and return letting"""
    letting = Letting.objects.create(title="title_test", address=create_address)
    return letting
