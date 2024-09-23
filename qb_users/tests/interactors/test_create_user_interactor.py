import json
from unittest import mock

import pytest


@pytest.mark.django_db
class TestCreateUserInteractor:

    @pytest.fixture()
    def user_profile_storge_mock(self):
        from quickbite_users.storages.user_profile_storage import \
            UserProfileStorage
        return mock.create_autospec(UserProfileStorage)

    @pytest.fixture
    def presenter_mock(self):
        from quickbite_users.presenters.create_user_presenter import \
            CreateUserPresenter
        return mock.create_autospec(CreateUserPresenter)

    @pytest.fixture
    def interactor(self, user_profile_storge_mock):
        from quickbite_users.interactors.create_user_interactor import \
            CreateUserInteractor
        return CreateUserInteractor(
            user_profile_storge=user_profile_storge_mock)

    @pytest.fixture()
    def create_token_response_mocker(self, mocker):
        from quickbite_users.tests.mocks import  create_token_response_mock
        return create_token_response_mock(mocker)

    def test_for_valid_details_called_get_success_response(
            self, interactor, create_token_response_mocker,
            user_profile_storge_mock, presenter_mock):
        # arrange
        username = "apple"
        email = "a@a.com"
        password = "Nikhil@1234"

        user_profile_storge_mock.is_user_exists.return_value = False
        user_profile_storge_mock.create_user_account.return_value = "new_user_id"
        create_token_response_mocker.return_value = "url", "headers", json.dumps(
            {
                "access_token": "access_token_1",
                "refresh_token": "refresh_token_1",
                "expires_in": 100
            }
        ), 200
        # act
        interactor.create_user_wrapper(
            username=username, email=email, password=password,
            presenter=presenter_mock
        )
        # assert
        presenter_mock.get_success_response.assert_called_once()

    def test_for_invalid_username_length_called_invalid_user_name_length_response(
            self, interactor, user_profile_storge_mock, presenter_mock):
        # arrange
        username = "AB"
        email = "a@a.com"
        password = "password"

        # act
        interactor.create_user_wrapper(
            username=username, email=email, password=password,
            presenter=presenter_mock
        )

        # assert
        presenter_mock.get_invalid_user_name_length_response. \
            assert_called_once()

    def test_for_invalid_username_format_called_invalid_user_name_format_response(
            self, interactor, user_profile_storge_mock, presenter_mock):
        # arrange
        username = "apple\--=]"
        email = "a@a.com"
        password = "password"

        # act
        interactor.create_user_wrapper(
            username=username, email=email, password=password,
            presenter=presenter_mock
        )

        # assert
        presenter_mock.get_invalid_user_name_format_response. \
            assert_called_once()

    def test_for_invalid_email_called_invalid_email_response(
            self, interactor, user_profile_storge_mock, presenter_mock):
        # arrange
        username = "apple"
        email = "a@a--09com"
        password = "password"

        # act
        interactor.create_user_wrapper(
            username=username, email=email, password=password,
            presenter=presenter_mock
        )

        # assert
        presenter_mock.get_invalid_email_response. \
            assert_called_once()

    def test_for_invalid_password_format_called_invalid_password_format_response(
            self, interactor, user_profile_storge_mock, presenter_mock):
        # arrange
        username = "apple"
        email = "a@a.com"
        password = "password"

        # act
        interactor.create_user_wrapper(
            username=username, email=email, password=password,
            presenter=presenter_mock
        )

        # assert
        presenter_mock.get_invalid_password_format. \
            assert_called_once()

    def test_for_user_already_exist_called_user_already_exist_response(
            self, interactor, user_profile_storge_mock, presenter_mock):
        # arrange
        username = "apple"
        email = "a@a.com"
        password = "Nikhil@1234"

        user_profile_storge_mock.is_user_exists.return_value = True

        # act
        interactor.create_user_wrapper(
            username=username, email=email, password=password,
            presenter=presenter_mock
        )

        # assert
        user_profile_storge_mock.is_user_exists.assert_called_once_with(
            username)
        presenter_mock.get_user_already_exist_response.assert_called_once()
