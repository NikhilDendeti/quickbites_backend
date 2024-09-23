import json
from typing import List

from django.http import HttpResponse

from quickbite_users.dtos import UserTokenDTO
from quickbite_users.serializers import CreateUserResponseSerializer


class CreateUserPresenter:
    @staticmethod
    def get_success_response(token_dto: UserTokenDTO):
        serializer = CreateUserResponseSerializer(token_dto)
        tokens = json.dumps(
            serializer.data
        )
        return HttpResponse(status=200, content=tokens)

    @staticmethod
    def get_user_already_exist_response():
        return HttpResponse(status=400, content=json.dumps(
            {
                "error": "User Already Exist"
            }
        ))

    @staticmethod
    def get_token_generation_failed_response():
        return HttpResponse(status=400, content=json.dumps(
            {
                "error": "Token generation failed"
            }
        ))

    @staticmethod
    def get_invalid_user_name_length_response():
        return HttpResponse(
            status=400,
            content=json.dumps({
                "error": "Invalid User Name Length"
            }),
        )

    @staticmethod
    def get_invalid_user_name_format_response():
        return HttpResponse(
            status=400,
            content=json.dumps({
                "error": "Invalid User Name Format"
            }),
        )

    @staticmethod
    def get_invalid_email_response():
        return HttpResponse(status=400, content=json.dumps(
            {
                "error": "Incorrect Mail Format"
            }
        ))

    @staticmethod
    def get_invalid_password_format(messages: List):
        return HttpResponse(status=400, content=json.dumps(
            {
                "error": "\n".join(messages)
            }
        ))
