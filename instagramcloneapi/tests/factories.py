from datetime import datetime
import factory
from faker import Faker


from instagramcloneapi.models import User, Profile

fake_data = Faker()


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    phoneNumber = "7985461320"
    email = fake_data.email()


class ProfileFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Profile

    username = fake_data.name()
    name = fake_data.first_name() + " " + fake_data.last_name()
    image = fake_data.email()
    created = datetime.now()
    user = factory.SubFactory(UserFactory)
