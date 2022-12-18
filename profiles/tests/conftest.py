import pytest

from django.contrib.auth.models import User

from profiles.models import Profile


@pytest.fixture
def create_profile(create_user) -> Profile:
    """create and return profile"""
    profile = Profile.objects.create(
        user=create_user, favorite_city="favorite_city_test"
    )
    return profile


@pytest.fixture
def create_user() -> User:
    """create and return user"""
    user = User.objects.create(username="test_user")
    return user
