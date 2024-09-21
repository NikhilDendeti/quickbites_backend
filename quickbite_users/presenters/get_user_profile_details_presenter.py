from django.http import HttpResponse
import json

from quickbite_users.dtos import UserProfileCompleteDetailsDTO


class GetUserDetailsPresenter:
    @staticmethod
    def get_invalid_user_response():
        return HttpResponse(
            status=404,
            content=json.dumps({"error": "User not found"})
        )

    @staticmethod
    def get_user_profile_details_success_response(
            user_details_dto: UserProfileCompleteDetailsDTO):
        tokens=json.dumps(
            {
                "username": user_details_dto.username,
                "email":user_details_dto.email,
                "role":user_details_dto.role,
                "user_id":user_details_dto.user_id
            }
        )
        return HttpResponse(status=200,content=tokens)
