from datetime import datetime
import pytest

from instagramcloneapi.models import User, Profile
from instagramcloneapi.tests.factories import UserFactory

# @pytest.mark.skip
# def test_example_01():
#     assert True


# @pytest.mark.database
# @pytest.mark.xfail
# def test_example_02():
#     assert False


# def test_example_03():
#     assert True


# @pytest.fixture(scope="session")
# def fixture_01():
#     print("****************************************fixture_01****************************************")
#     return 1

# @pytest.fixture(scope="session")
# def fixture_02():
#     print("****************************************start fixture_02****************************************")
#     yield 2
#     print("****************************************end fixture_02****************************************")


# def test_sample_fixture_01(fixture_01):
#     assert 1 == fixture_01

# def test_sample_fixture_02(fixture_01):
#     assert 1 == fixture_01

# def test_sample_fixture_03(fixture_02):
#     assert 2 == fixture_02

# **************************************DATABASE*************************************

# @pytest.mark.django_db
# def test_user_create():
#     User.objects.create(phoneNumber="7984561230", email="venkatesh@email.com",
#                         password="venkatesh", created=datetime.now())

#     print(User.objects.all())

#     assert User.objects.count() == 1


# @pytest.mark.django_db
# def test_user_count():
#     assert User.objects.count() == 0


# **************************************DATABASE FIXTURE*************************************
# @pytest.fixture()
# def database_fixture(db):
#     user = User.objects.create(phoneNumber="7984561230", email="venkatesh@email.com",
#                                password="venkatesh", created=datetime.now())

#     return user


# @pytest.mark.django_db
# def test_user_count(database_fixture):
#     assert User.objects.count() == 1


# @pytest.mark.django_db
# def test_user(database_fixture):
#     assert database_fixture.email == "venkatesh@email.com" and database_fixture.phoneNumber == "7984561230"


# **************************************DATABASE FACTORY FIXTURE*************************************


# @pytest.mark.django_db
# def test_new_user_count(new_user_01):
#     assert User.objects.count() == 1


# @pytest.mark.django_db
# def test_new_user_01(new_user_01):
#     assert new_user_01.email == "venkateshpothagani@gmail.com" and new_user_01.phoneNumber == "7984561230"


# @pytest.mark.django_db
# def test_new_user_01(new_user_02):
#     assert new_user_02.email == "venkateshpothagani@outlook.com" and new_user_02.phoneNumber == "7984561230"


# **************************************DATABASE FIXTURE FACTORY BOY*************************************

# @pytest.mark.django_db
# def test_new_user_01(user_factory):
#     user = user_factory.build()
#     print(user.email)
#     assert True


# @pytest.mark.django_db
# def test_new_profile_01(profile_factory):
#     profile = profile_factory.build()
#     print(profile.user.email)
#     assert True


# @pytest.mark.django_db
# def test_new_user_02(db, user_factory):
#     user = user_factory.create()
#     print(user.email)
#     assert True


# @pytest.mark.django_db
# def test_new_profile_02(db, profile_factory):
#     profile = profile_factory.create()
#     print(profile.user.email, User.objects.count())
#     assert True

# **************************************PARAMETRIZED FIXTURES*************************************
@pytest.mark.django_db
@pytest.mark.parametrize(
    'username, name, image, created', [
        ("username1", "name", "image", datetime.now()),
        ("username2", "name", "image", datetime.now()),
        ("username3", "name", "image", datetime.now()),
        ("username4", "name", "image", datetime.now()),
        ("username5", "name", "image", datetime.now()),
        ("username6", "name", "image", datetime.now()),
    ]
)
def test_sample_parametrize(db, user_factory, profile_factory, username, name, image, created):
    user = user_factory(
        phoneNumber="7984561230", email="venkatesh@email.com",
        password="venkatesh", created=datetime.now()
    )
    profile = profile_factory(
        username=username, name=name, image=image, created=created, user=user
    )

    item = Profile.objects.all().count()
    print(f"{profile.username} == {username} - {profile.user.email}")

    assert profile.username == username
