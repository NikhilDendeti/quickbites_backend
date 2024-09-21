from quickbite_users.constants.custom_exceptions import InvalidUserIdException
from quickbite_users.dtos import UserProfileCompleteDetailsDTO
from quickbite_users.presenters.get_user_profile_details_presenter import \
    GetUserDetailsPresenter
from quickbite_users.storages.user_profile_storage import UserProfileStorage


class GetUserProfileDetailsInteractor:
    def __init__(
            self,user_profile_storge: UserProfileStorage):
        self.user_profile_storge = user_profile_storge

    def get_user_profile_wrapper(
            self, user_id, presenter: GetUserDetailsPresenter):
        try:
            user_profile_details = self.get_user_profile(user_id=user_id)
            return presenter.get_user_profile_details_success_response(
                user_profile_details)
        except InvalidUserIdException:
            return presenter.get_invalid_user_response()

    def get_user_profile(self, user_id: str):
        user_account_details = self.user_profile_storge.\
            get_user_account_by_user_id(user_id)
        user_profile_details = self.user_profile_storge.\
            get_user_profile_details_by_user_id(user_id)

        return UserProfileCompleteDetailsDTO(
                username=user_account_details.username,
                email=user_account_details.email,
                role=user_profile_details.role,
                user_id=user_account_details.user_id)
