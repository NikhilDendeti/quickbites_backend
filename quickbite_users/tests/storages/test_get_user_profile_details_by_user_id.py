import pytest
from django.test import TestCase

from quickbite_users.dtos import UserProfileDetailsDTO
from quickbite_users.models import UserAccount, UserProfileDetails
from quickbite_users.storages.user_profile_storage import UserProfileStorage
from quickbite_users.tests.factories.dtos import UserProfileDetailsDTOFactory
from quickbite_users.tests.factories.models import UserProfileDetailsFactory, UserAccountFactory


@pytest.mark.django_db
class TestGetUserProfileDetailsByUserId(TestCase):

    def test_get_user_profile_details_by_user_id(self):
        # Arrange
        storage = UserProfileStorage()
        user = UserAccountFactory()
        user_profile = UserProfileDetailsFactory(user=user)
        user_id = str(user_profile.user_id)

        user_profile_details_dto_expected = UserProfileDetailsDTOFactory(
            id=str(user_profile.id),
            role=user_profile.role,
            user_id=str(user_profile.user_id)
        )

        # Act
        user_profile_details_dto_actual = storage.get_user_profile_details_by_user_id(
            user_id=user_id
        )

        # Assert
        self.assertEqual(
            user_profile_details_dto_actual.id,
            user_profile_details_dto_expected.id
        )
