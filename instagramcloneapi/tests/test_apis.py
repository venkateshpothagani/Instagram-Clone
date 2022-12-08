from rest_framework.test import APIClient
import pytest

from instagramcloneapi.models import User, Profile
from django_mock_queries.mocks import MockSet
client = APIClient()


pytestmark = pytest.mark.django_db


class TestUserEndpoints:
    pytestmark = pytest.mark.django_db

    @pytest.mark.django_db
    def test_create_user_api(user_factory, api_client, django_db_keepdb):

        data = {
            "phoneNumber": "7984563210",
            "email": "venkatesh@gmail.com",
            "password": "123423"
        }

        response = api_client().post(path='/api/register', data=data)

        status_code = response.status_code
        response_data = response.data["data"]

        assert status_code == 201 and \
            response_data['phoneNumber'] == "7984563210" and \
            response_data['email'] == "venkatesh@gmail.com" and \
            len(response_data['posts']) == 0

    @pytest.mark.django_db
    def test_login_user_api(user_factory, api_client, db):
        data = {
            "phoneNumber": "7984563210",
            "email": "venkatesh@gmail.com",
            "password": "123423"
        }

        response = api_client().post(path='/api/register', data=data)

        assert response.status_code == 201

        data = {
            "phoneNumber": "7984563210",
            "password": "123423"
        }

        response = api_client().post(path='/api/login', data=data)

        assert response.status_code == 200
