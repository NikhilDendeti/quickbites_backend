import pytest
from django.test import TestCase
from quickbite_users.models import UserAccount
from quickbite_users.storages.user_profile_storage import UserProfileStorage


@pytest.mark.django_db
class TestCreateUserAccount(TestCase):

    def test_create_user_account_case(self):
        # Arrange
        storage=UserProfileStorage()
        username = "user_1"
        email = "user1@example.com"
        password = "password_1"

        # Act
        user_id = storage.create_user_account(username, email, password)

        # Assert
        user = UserAccount.objects.get(user_id=user_id)
        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
