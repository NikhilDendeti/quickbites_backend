import json

from django.core.serializers import serialize
from django.http import HttpResponse

from quickbite_users.dtos import UserTokenDTO
from quickbite_users.serializers import SigninResponseSerializer


class SigninPresenter:
    @staticmethod
    def get_success_response(token_dto: UserTokenDTO):
        serializer = SigninResponseSerializer(token_dto)
        tokens = json.dumps(
            serializer.data
        )
        return HttpResponse(status=200, content=tokens)

    @staticmethod
    def get_username_does_not_exists_response():
        return HttpResponse(status=400, content=json.dumps(
            {
                "error": "User Name Not Exist"
            }
        ))

    @staticmethod
    def get_invalid_password_response():
        return HttpResponse(status=400, content=json.dumps(
            {
                "error": "Invalid Password"
            }
        ))
