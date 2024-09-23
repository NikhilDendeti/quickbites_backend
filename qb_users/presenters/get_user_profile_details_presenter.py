from django.http import HttpResponse
import json

from qb_users.dtos import UserProfileCompleteDetailsDTO
from qb_users.serializers import GetUserProfileDetailsResponseSerializer


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
        serializer = GetUserProfileDetailsResponseSerializer(user_details_dto)

        tokens = json.dumps(
            serializer.data
        )
        return HttpResponse(status=200, content=tokens)
