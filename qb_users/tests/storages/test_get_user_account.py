import uuid

import pytest
from snapshottest import TestCase

from qb_users.constants.custom_exceptions import \
    UsernameDoesNotExistException
from qb_users.storages.user_profile_storage import UserProfileStorage
from qb_users.tests.factories.dtos import UserAccountDTOFactory
from qb_users.tests.factories.models import UserAccountFactory


@pytest.mark.django_db
class TestGetUserAccount:

    def test_get_user_account_when_username_exists(self, snapshot):
        # arrange
        storage = UserProfileStorage()
        username = "user_1"
        user_id = str(uuid.uuid4())
        user_account_dto_expected = UserAccountDTOFactory(
            user_id=user_id,
            username="user_1",
            email="user1@example.com",
            password="password_1"
        )
        user_account = UserAccountFactory(
            user_id=user_id,
            username="user_1",
            email="user1@example.com",
            password="password_1"
        )

        # act
        user_account_dto_actual = storage.get_user_account(
            username=username)

        # assert
        snapshot.assert_match(
            user_account_dto_actual,
            user_account_dto_expected
        )

    def test_get_user_account_when_username_not_exists(self):
        # arrange
        storage = UserProfileStorage()
        username = "user_1"

        # act
        with pytest.raises(UsernameDoesNotExistException):
            storage.get_user_account(username=username)
