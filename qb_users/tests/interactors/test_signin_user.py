import uuid
from unittest import mock

import pytest
from django.contrib.auth.hashers import make_password

from qb_users.constants.custom_exceptions import \
    InvalidUserNameFormatException
from qb_users.tests.factories.dtos import UserAccountDTOFactory


class TestSignInInteractor:
    @pytest.fixture()
    def user_profile_storge_mock(self):
        from qb_users.storages.user_profile_storage import \
            UserProfileStorage
        return (mock.create_autospec(UserProfileStorage)
                )

    @pytest.fixture()
    def presenter_mock(self):
        from qb_users.presenters.signin_presenter import \
            SigninPresenter
        return (mock.create_autospec(SigninPresenter)
                )

    @pytest.fixture()
    def interactor(self, user_profile_storge_mock):
        from qb_users.interactors.signin_user_interactor import \
            SignInInteractor
        return (SignInInteractor(
            user_profile_storge=user_profile_storge_mock)
        )

    @pytest.fixture()
    def user_token_dto(self):
        from qb_users.dtos import UserTokenDTO
        return (UserTokenDTO(
            user_id="user_id_1",
            expires_in="100",
            access_token="access_token_1",
            refresh_token="refresh_token_1")
        )

    @pytest.fixture()
    def signin_token_response_mocker(self, mocker):
        from qb_users.tests.mocks import \
            signin_token_response_mock
        return signin_token_response_mock(mocker)

    # @pytest.mark.django_db
    def test_for_valid_details_called_get_success_response(self, interactor,
                                                           user_profile_storge_mock,
                                                           presenter_mock,
                                                           signin_token_response_mocker,
                                                           user_token_dto):
        # arrange
        username = "apple"
        password = "Nikhil@1234"
        user_id = str(uuid.uuid4())
        user_profile_storge_mock.is_user_exists.return_value = True
        user_profile_storge_mock.get_user_account.return_value = UserAccountDTOFactory(
            username=username, password=make_password(password),
            user_id=user_id
        )
        user_token_dto.user_id = user_id
        signin_token_response_mocker.return_value = user_token_dto
        # act
        interactor.login_user_wrapper(
            username=username, password=password,
            presenter=presenter_mock
        )
        # assert
        presenter_mock.get_success_response.assert_called_once_with(
            user_token_dto)

    def test_for_invalid_username_called_get_username_does_not_exists_response(
            self, interactor, user_profile_storge_mock, presenter_mock):
        # arrange
        username = "apple"
        password = "Nikhil@1234"
        user_profile_storge_mock.get_user_account.side_effect = InvalidUserNameFormatException
        # act
        interactor.login_user_wrapper(
            username=username, password=password,
            presenter=presenter_mock
        )
        # assert
        presenter_mock.get_username_does_not_exists_response.assert_called_once()

    def test_for_invalid_password_called_get_invalid_password_response(self,
                                                                       interactor,
                                                                       user_profile_storge_mock,
                                                                       presenter_mock):
        # arrange
        username = "apple"
        password = "Nikhil@1234"
        user_profile_storge_mock.is_user_exists.return_value = True
        user_profile_storge_mock.get_user_account.return_value = UserAccountDTOFactory(
            username=username, password=make_password(password),
            user_id=str(uuid.uuid4())
        )
        # act
        interactor.login_user_wrapper(
            username=username, password="Nikhil@12345",
            presenter=presenter_mock
        )
        # assert
        presenter_mock.get_invalid_password_response.assert_called_once()


