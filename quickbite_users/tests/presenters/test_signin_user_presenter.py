import json


from quickbite_users.tests.factories.dtos import UserTokenDTOFactory


class TestSigninUserPresenter:
    def test_for_success_response(self,snapshot):
        from quickbite_users.presenters.signin_presenter import SigninPresenter
        presenter = SigninPresenter()
        # arrange
        token_dto = UserTokenDTOFactory(
            user_id="user_id_1",
            access_token="access_toekn_1",
            refresh_token="refresh_token_1",
            expires_in=100
        )
        # act
        response = presenter.get_success_response(token_dto=token_dto)
        # assert
        snapshot.assert_match(json.loads(response.content), 'response_data')

    def  test_for_username_does_not_exists_response(self,snapshot):
        from quickbite_users.presenters.signin_presenter import SigninPresenter
        presenter = SigninPresenter()
        # act
        response = presenter.get_username_does_not_exists_response()
        # assert
        snapshot.assert_match(json.loads(response.content), 'response_data')

    def  test_for_invalid_password_response(self,snapshot):
        from quickbite_users.presenters.signin_presenter import SigninPresenter
        presenter = SigninPresenter()
        # act
        response = presenter.get_invalid_password_response()
        # assert
        snapshot.assert_match(json.loads(response.content), 'response_data')

