import pytest
from django.test import TestCase

from quickbite_users.dtos import UserAccountDTO
from quickbite_users.models import UserAccount
from quickbite_users.storages.user_profile_storage import UserProfileStorage


class TestGetUserAccountDTOFromObj(TestCase):
    def test_get_user_account_dto_from_obj(self):
        # Arrange
        storage = UserProfileStorage()
        username = "user_1"
        email = "user1@example.com"
        password = "password_1"
        # Act
        user_account = UserAccount.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user_account_dto_expected = UserAccountDTO(
            user_id=str(user_account.user_id),
            username=user_account.username,
            email=user_account.email,
            password=user_account.password
        )
        # Assert
        user_account_dto_actual = storage._get_user_account_dto_from_obj(
            user_account)
        self.assertEqual(
            user_account_dto_actual.username,
            user_account_dto_expected.username
        )
        self.assertEqual(
            user_account_dto_actual.email,
            user_account_dto_expected.email
        )
        self.assertEqual(
            user_account_dto_actual.password,
            user_account_dto_expected.password
        )
        self.assertEqual(
            user_account_dto_actual.user_id,
            user_account_dto_expected.user_id
        )
