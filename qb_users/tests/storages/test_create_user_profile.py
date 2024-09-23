import pytest
from django.test import TestCase

from quickbite_users.models import UserAccount
from quickbite_users.storages.user_profile_storage import UserProfileStorage


@pytest.mark.django_db
class TestCreateUserProfile(TestCase):
    def test_create_user_profile_case(self):
        # Arrange
        storage = UserProfileStorage()
        username = "user_1"
        email = "user1@example.com"
        password = "password_1"

        # act
        user_id = storage.create_user_account(username, email, password)
        storage.create_user_profile(user_id, 'vendor')

        # Assert
        user = UserAccount.objects.get(user_id=user_id)
        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertEqual(user.userprofiledetails.role, 'vendor')
