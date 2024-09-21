import json

from snapshottest import TestCase

from quickbite_users.tests.factories.dtos import UserTokenDTOFactory


class TestCreateUserPresenter(TestCase):

    def test_for_success_case(self):
        from quickbite_users.presenters.create_user_presenter import \
            CreateUserPresenter
        presenter = CreateUserPresenter()
        # arrange
        token_dto = UserTokenDTOFactory(
            user_id="user_id_1",
            access_token="access_toekn_1",
            refresh_token="refresh_token_1",
            expires_in="100"
        )

        # act
        response = presenter.get_success_response(token_dto=token_dto)

        # assert
        self.assertMatchSnapshot(json.loads(response.content), 'response_data')

    def test_for_user_already_exist(self):
        from quickbite_users.presenters.create_user_presenter import \
            CreateUserPresenter
        presenter = CreateUserPresenter()
        # act
        response = presenter.get_user_already_exist_response()
        # assert
        self.assertMatchSnapshot(json.loads(response.content), 'response_data')

    def test_for_token_generation_failed(self):
        from quickbite_users.presenters.create_user_presenter import \
            CreateUserPresenter
        presenter = CreateUserPresenter()
        # act
        response = presenter.get_token_generation_failed_response()
        # assert
        self.assertMatchSnapshot(json.loads(response.content), 'response_data')

    def test_for_invalid_user_name_length(self):
        from quickbite_users.presenters.create_user_presenter import \
            CreateUserPresenter
        presenter = CreateUserPresenter()
        # act
        response = presenter.get_invalid_user_name_length_response()
        # assert
        self.assertMatchSnapshot(json.loads(response.content), 'response_data')

    def test_for_invalid_user_name_format(self):
        from quickbite_users.presenters.create_user_presenter import \
            CreateUserPresenter
        presenter = CreateUserPresenter()
        # act
        response = presenter.get_invalid_user_name_format_response()
        # assert
        self.assertMatchSnapshot(json.loads(response.content), 'response_data')

    def test_for_invalid_email(self):
        from quickbite_users.presenters.create_user_presenter import \
            CreateUserPresenter
        presenter = CreateUserPresenter()
        # act
        response = presenter.get_invalid_email_response()
        # assert
        self.assertMatchSnapshot(json.loads(response.content), 'response_data')

    def test_for_invalid_password_format(self):
        from quickbite_users.presenters.create_user_presenter import \
            CreateUserPresenter
        presenter = CreateUserPresenter()
        # act
        response = presenter.get_invalid_password_format(
            messages=['message1', 'message2'])
        # assert
        self.assertMatchSnapshot(json.loads(response.content), 'response_data')
