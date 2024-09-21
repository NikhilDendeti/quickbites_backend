from django.contrib.auth.hashers import check_password

from quickbite_users.constants.custom_exceptions import \
    UsernameDoesNotExistException, InvalidPasswordException
from quickbite_users.dtos import TokenDTO, UserTokenDTO
from quickbite_users.interactors.mixins.access_tokens_mixin import \
    AccessTokenMixin
from quickbite_users.presenters.signin_presenter import SigninPresenter
from quickbite_users.storages.user_profile_storage import UserProfileStorage


class SignInInteractor(AccessTokenMixin):
    def __init__(
            self,
            user_profile_storge: UserProfileStorage,

    ):
        self.user_profile_storge = user_profile_storge

    def login_user_wrapper(
            self, username: str, password: str, presenter: SigninPresenter):
        try:
            tokens = self.signin_user(username, password)
        except UsernameDoesNotExistException:
            return presenter.get_username_does_not_exists_response()
        except InvalidPasswordException:
            return presenter.get_invalid_password_response()

        return presenter.get_success_response(tokens)

    def signin_user(
            self, username: str, password: str) -> UserTokenDTO:
        user_account = self.user_profile_storge.get_user_account(
            username)
        print(user_account)
        print(f"password: {password}")

        is_correct = check_password(password, user_account.password)
        if not is_correct:
            raise InvalidPasswordException("Invalid password")

        tokens = self.get_tokens(username, password)

        user_token_dto = UserTokenDTO(
            user_id=user_account.user_id,
            expires_in=tokens.expires_in,
            access_token=tokens.access_token,
            refresh_token=tokens.refresh_token
        )

        return user_token_dto
