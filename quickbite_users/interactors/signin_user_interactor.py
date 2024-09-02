import json

from django.contrib.auth.hashers import check_password
from django.http import HttpResponse, HttpRequest
from oauth2_provider.views import TokenView

from quickbite_users.models import UserAccount


class UsernameDoesNotExistException(Exception):
    pass


class InvalidPasswordException(Exception):
    pass
class GetTokensFailedException(Exception):
    pass

class SignInInteractor:
    def login_user_wrapper(
            self, username: str, password: str):
        try:
            tokens = self.signin_user(username, password)
        except UsernameDoesNotExistException:
            return HttpResponse(status=400, content=json.dumps(
                {
                    "error": "User Name Not Exist"
                }
            ))
        except InvalidPasswordException:
            return HttpResponse(status=400, content=json.dumps(
                {
                    "error": "Invalid Password"
                }
            ))


        return HttpResponse(status=200, content=tokens)

    def signin_user(
            self, username: str, password: str):
        self._validate_username(username)

        user_account = UserAccount.objects.get(
            username=username)
        is_correct = check_password(password, user_account.password)
        if not is_correct:
            raise InvalidPasswordException("Invalid password")

        tokens = self.get_tokens(username, password)

        return tokens

    @staticmethod
    def _validate_username(username: str):
        is_user_exists = UserAccount.objects.filter(
            username=username
        ).exists()

        if not is_user_exists:
            raise UsernameDoesNotExistException("Username does not exist")

    @staticmethod
    def get_tokens(username, password):
        from django.conf import settings
        request=HttpRequest()
        request.META={
            "Content-Type": "application/x-www-form-urlencoded",
            "Cache-Control": "no-cache"
        }
        request.method='POST'
        request.POST={
            "client_id": settings.CLIENT_ID,
            "client_secret": settings.CLIENT_SECRET,
            "grant_type": "password",
            "scope": "write",
            "username": username,
            "password": password
        }
        token_view=TokenView()
        try:
            url, headers, body, status_code = token_view.create_token_response(
                request)
        except Exception as err:
            raise GetTokensFailedException

        return body
