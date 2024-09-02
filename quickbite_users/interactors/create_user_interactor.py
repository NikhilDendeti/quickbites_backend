import json
from django.core.exceptions import ValidationError
import re
from django.http import HttpResponse, HttpRequest
from oauth2_provider.views import TokenView
from quickbite_users.constants import custom_exceptions
from quickbite_users.models import UserAccount


def get_tokens(username, password):
    from django.conf import settings
    request = HttpRequest()
    request.META = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cache-Control": "no-cache"
    }
    request.method = 'POST'
    request.POST = {
        "client_id": settings.CLIENT_ID,
        "client_secret": settings.CLIENT_SECRET,
        "grant_type": "password",
        "scope": "write",
        "username": username,
        "password": password
    }

    token_view = TokenView()
    try:

        url, headers, body, status_code = token_view.create_token_response(
            request)

    except Exception as err:
        raise custom_exceptions.GetTokensFailedException

    return body


class CreateUserInteractor:
    def create_user_wrapper(
            self, username: str, email: str, password: str):
        try:
            tokens = self.create_user(username, email, password)
        except custom_exceptions.UserNameAlreadyExistsException:
            return HttpResponse(status=400, content=json.dumps(
                {
                    "error": "User Already Exist"
                }
            ))
        except custom_exceptions.GetTokensFailedException:
            return HttpResponse(status=400, content=json.dumps(
                {
                    "error": "Token generation failed"
                }
            ))
        except custom_exceptions.InvalidUserNameLengthException as e:
            return HttpResponse(status=400, content=json.dumps(
                {
                    "error": e.error_message
                }
            ))
        except custom_exceptions.InvalidUserNameFormatException as e:
            return HttpResponse(status=400, content=json.dumps(
                {
                    "error": e.error_message
                }
            ))
        except custom_exceptions.InvalidEmailException:
            return HttpResponse(status=400, content=json.dumps(
                {
                    "error": "Incorrect Mail Format"
                }
            ))
        except custom_exceptions.InvalidPasswordFormat:
            return HttpResponse(status=400, content=json.dumps(
                {
                    "error": "Incorrect Password Format"
                }
            ))
        return HttpResponse(status=201, content=tokens)

    def create_user(
            self, username: str, email: str, password: str):

        self._validate_create_user_details(
            username=username, email=email, password=password)
        UserAccount.objects.create_user(
            username=username,
            email=email,
            password=password)

        # todo: have to create the UserRoleProfile based on the data given

        return get_tokens(username, password)

    def _validate_create_user_details(
            self, username: str, email: str, password: str):
        self._validate_username(username)
        self._validate_email(email)
        self._validate_password(password)
        self._validate_is_user_exists(username)

    @staticmethod
    def _validate_is_user_exists(username: str):
        is_user_exists = UserAccount.objects.filter(
            username=username
        ).exists()
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
