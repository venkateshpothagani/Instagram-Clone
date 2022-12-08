from datetime import datetime
import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient
from instagramcloneapi.models import User
from instagramcloneapi.tests.factories import UserFactory, ProfileFactory

register(UserFactory)
register(ProfileFactory)


@pytest.fixture
def api_client():
    return APIClient

# @pytest.fixture
# def new_user_factory(db):
#     def create_user(phoneNumber: str = "7984561230", email: str = "venkatesh@email.com",
#                     password: str = "venkatesh", created: datetime = datetime.now()):

#         user = User.objects.create(phoneNumber=phoneNumber, email=email,
#                                    password=password, created=created)

#         return user

#     return create_user


# @pytest.fixture
# def new_user_01(db, new_user_factory):
#     return new_user_factory(email="venkateshpothagani@gmail.com")


# @pytest.fixture
# def new_user_02(db, new_user_factory):
#     return new_user_factory(email="venkateshpothagani@outlook.com")
