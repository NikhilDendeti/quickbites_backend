import json
from typing import List

from django.http import HttpResponse

from quickbite_users.dtos import UserTokenDTO


class CreateUserPresenter:
    @staticmethod
    def get_success_response(token_dto: UserTokenDTO):
        tokens = json.dumps(
            {
                "access_token": token_dto.access_token,
                "refresh_token": token_dto.refresh_token,
                "expires_in": token_dto.expires_in,
                "user_id": token_dto.user_id
            }
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
