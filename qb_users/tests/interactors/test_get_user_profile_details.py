from unittest import mock

import pytest

from qb_users.constants.custom_exceptions import InvalidUserIdException


@pytest.mark.django_db
class TestGetUserProfileDetailsInteractor:
    @pytest.fixture()
    def user_profile_storge_mock(self):
        from qb_users.storages.user_profile_storage import \
            UserProfileStorage
        return mock.create_autospec(UserProfileStorage)

    @pytest.fixture()
    def presenter_mock(self):
        from qb_users.presenters.get_user_profile_details_presenter import \
            GetUserDetailsPresenter
        return mock.create_autospec(GetUserDetailsPresenter)

    @pytest.fixture()
    def interactor(self, user_profile_storge_mock):
        from qb_users.interactors.get_user_profile_datails_interactor import \
            GetUserProfileDetailsInteractor
        return GetUserProfileDetailsInteractor(
            user_profile_storge=user_profile_storge_mock)

    @pytest.fixture()
    def user_profile_details_dto(self):
        from qb_users.dtos import UserProfileCompleteDetailsDTO
        return UserProfileCompleteDetailsDTO(
            username="apple",
            email="a@a.com",
            role="CUSTOMER",
            user_id="user_id_1")

    def test_for_valid_user_id_called_get_success_response(
            self, interactor, user_profile_storge_mock, presenter_mock,
            user_profile_details_dto):
        # arrange
        user_id = "user_id_1"

        user_profile_storge_mock.get_user_account_by_user_id.return_value = user_profile_details_dto

        # act
        interactor.get_user_profile_wrapper(
            user_id=user_id, presenter=presenter_mock
        )

        # assert
        presenter_mock.get_user_profile_details_success_response.assert_called_once()

    def test_for_invalid_user_id_called_invalid_user_response(self, interactor,
                                                              user_profile_storge_mock,
                                                              presenter_mock):
        # arrange
        user_id = "12345"
        user_profile_storge_mock.get_user_account_by_user_id.side_effect = \
            InvalidUserIdException

        # act
        interactor.get_user_profile_wrapper(
            user_id=user_id, presenter=presenter_mock
        )
        # assert
        presenter_mock.get_invalid_user_response.assert_called_once()



