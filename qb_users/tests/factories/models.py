import factory
import uuid
from django.contrib.auth.hashers import make_password
from qb_users.models import UserAccount, UserProfileDetails


class UserAccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserAccount

    user_id = factory.LazyFunction(uuid.uuid4)
    username = factory.Sequence(lambda n: f'user_{n}')
    email = factory.Sequence(lambda n: f'user{n}@example.com')
    password = factory.LazyAttribute(lambda n: make_password('defaultpassword_{n}'))

    first_name = factory.Sequence(lambda n: f'FirstName{n}')
    last_name = factory.Sequence(lambda n: f'LastName{n}')


class UserProfileDetailsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserProfileDetails

    id = factory.LazyFunction(uuid.uuid4)
    user = factory.SubFactory(UserAccountFactory)
    role = factory.Iterator(
        ['vendor', 'student', 'employee'])


