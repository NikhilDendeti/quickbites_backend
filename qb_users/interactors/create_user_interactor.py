import re

from django.core.exceptions import ValidationError
from django.db import transaction

from qb_users.constants import custom_exceptions
from qb_users.constants.enums import RoleEnum
from qb_users.dtos import UserTokenDTO
from qb_users.interactors.mixins.access_tokens_mixin import \
    AccessTokenMixin
from qb_users.presenters.create_user_presenter import \
    CreateUserPresenter
from qb_users.storages.user_profile_storage import UserProfileStorage


class CreateUserInteractor(AccessTokenMixin):
    def __init__(
            self,
            user_profile_storge: UserProfileStorage
    ):
        self.user_profile_storge = user_profile_storge

    @transaction.atomic()
    def create_user_wrapper(
            self, username: str, email: str, password: str,
            presenter: CreateUserPresenter
    ):
        try:
            tokens = self.create_user(username, email, password)
        except custom_exceptions.UserNameAlreadyExistsException:
            return presenter.get_user_already_exist_response()
        except custom_exceptions.GetTokensFailedException:
            return presenter.get_token_generation_failed_response()
        except custom_exceptions.InvalidUserNameLengthException:
            return presenter.get_invalid_user_name_length_response()
        except custom_exceptions.InvalidUserNameFormatException:
            return presenter.get_invalid_user_name_format_response()
        except custom_exceptions.InvalidEmailException:
            return presenter.get_invalid_email_response()
        except custom_exceptions.InvalidPasswordFormat as err:
            return presenter.get_invalid_password_format(err.messages)
        return presenter.get_success_response(tokens)

    def create_user(
            self, username: str, email: str, password: str) -> UserTokenDTO:

        self._validate_create_user_details(
            username=username, email=email, password=password)

        user_id = self.user_profile_storge.create_user_account(username, email,
                                                               password)
        self._create_user_role_profile(user_id)

        tokens = self.get_tokens(username, password)

        user_token_dto = UserTokenDTO(
            user_id=user_id,
            expires_in=tokens.expires_in,
            access_token=tokens.access_token,
            refresh_token=tokens.refresh_token
        )

        return user_token_dto

    def _validate_create_user_details(
            self, username: str, email: str, password: str):
        self._validate_username(username)
        self._validate_email(email)
        self._validate_password(password)
        self._validate_is_user_exists(username)

    def _validate_is_user_exists(self, username: str):
        is_user_exists = self.user_profile_storge.is_user_exists(username)
        if is_user_exists:
            raise custom_exceptions.UserNameAlreadyExistsException

    @staticmethod
    def _validate_username(username: str):
        if len(username) < 3 or len(username) > 30:
            error_message = "Username must be between 3 and 30 characters long."
            raise custom_exceptions.InvalidUserNameLengthException(
                error_message=error_message)

        if not re.match(r'^[\w]+$', username):
            error_message = "Username can only contain letters, numbers, and underscores."
            raise custom_exceptions.InvalidUserNameFormatException(
                error_message=error_message)

    @staticmethod
    def _validate_email(email: str):
        from django.core.validators import validate_email
        try:
            validate_email(email)
        except ValidationError:
            raise custom_exceptions.InvalidEmailException

    @staticmethod
    def _validate_password(password: str):
        from django.contrib.auth.password_validation import validate_password
        try:
            validate_password(password)
        except ValidationError as e:
            raise custom_exceptions.InvalidPasswordFormat(e.messages)

    def _create_user_role_profile(self, user_id: str):
        role = RoleEnum.student.value
        self.user_profile_storge.create_user_profile(user_id, role)
