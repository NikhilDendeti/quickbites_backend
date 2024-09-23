import uuid
from snapshottest import TestCase
import pytest
from quickbite_users.dtos import UserAccountDTO
from quickbite_users.models import UserAccount, UserProfileDetails
from quickbite_users.tests.factories.models import UserAccountFactory


@pytest.mark.django_db
class TestIsUserExists(TestCase):

    def  test_is_user_exists_when_user_exists(self):
        from quickbite_users.storages.user_profile_storage import \
            UserProfileStorage
        storage = UserProfileStorage()
         # arrange
        username = "user_1"
        user_id = str(uuid.uuid4())
        user_account = UserAccountFactory(
            user_id=user_id,
            username="user_1",
            email="user1@example.com",
            password="password_1"
        )
        # act
        is_user_exists = storage.is_user_exists(username=username)
        # assert
        self.assertTrue(is_user_exists)

    def  test_is_user_exists_when_user_not_exists(self):
        from quickbite_users.storages.user_profile_storage import \
            UserProfileStorage
        storage = UserProfileStorage()
         # arrange
        username = "user_1"

        # act
        is_user_exists = storage.is_user_exists(username=username)

        # assert
        self.assertFalse(is_user_exists)
