import pytest
from django.test import TestCase
from qb_users.models import UserAccount
from qb_users.storages.user_profile_storage import UserProfileStorage
from qb_users.tests.factories.dtos import UserAccountDTOFactory
from django.contrib.auth.hashers import check_password

@pytest.mark.django_db
class TestUserAccountByUserId(TestCase):
    def test_get_user_account_by_user_id_case(self):
        # Arrange
        storage = UserProfileStorage()
        username = "user_1"
        email = "user1@example.com"
        password = "password_1"

        user_id = storage.create_user_account(
            username=username,
            email=email,
            password=password
        )

        user_account = UserAccount.objects.get(user_id=user_id)
        user_account_dto_expected = UserAccountDTOFactory(
            user_id=user_account.user_id,
            username=user_account.username,
            email=user_account.email,
            password=user_account.password
        )

        # Act
        user_account_dto_actual = storage.get_user_account_by_user_id(
            user_id=user_id
        )

        # Assert
        self.assertEqual(
            user_account_dto_actual.username,
            user_account_dto_expected.username
        )
        self.assertEqual(
            user_account_dto_actual.email,
            user_account_dto_expected.email
        )
        self.assertTrue(
            check_password(password, user_account_dto_actual.password)
        )
