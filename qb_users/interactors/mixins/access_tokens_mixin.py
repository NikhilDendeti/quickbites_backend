import json

from django.http import HttpRequest
from oauth2_provider.views import TokenView

from qb_users.constants.custom_exceptions import \
    GetTokensFailedException
from qb_users.dtos import TokenDTO
from qb_backend import settings
class AccessTokenMixin:
    @staticmethod
    def get_tokens(username, password) -> TokenDTO:
        # from django.conf import settings
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
            body=json.loads(body)
        except Exception as err:
            raise GetTokensFailedException

        return TokenDTO(
            access_token=body["access_token"],
            refresh_token=body["refresh_token"],
            expires_in=body["expires_in"]
        )
