from quickbite_users.constants.custom_exceptions import InvalidUserIdException, \
    UsernameDoesNotExistException
from quickbite_users.dtos import UserAccountDTO, UserProfileDetailsDTO
from quickbite_users.models import UserAccount, UserProfileDetails


class UserProfileStorage:

    def get_user_account(self, username:str) -> UserAccountDTO:
        try:
            user_account = UserAccount.objects.get(
                username=username)
        except UserAccount.DoesNotExist:
            raise UsernameDoesNotExistException

        return self._get_user_account_dto_from_obj(user_account)

    @staticmethod
    def is_user_exists(username: str) -> bool:
        is_user_exists = UserAccount.objects.filter(
            username=username
        ).exists()

        return is_user_exists


    def create_user_account(self,username: str, email: str, password: str) -> str:
        user = UserAccount.objects.create_user(
            username=username,
            email=email,
            password=password)

        return user.user_id

    @staticmethod
    def create_user_profile(user_id: str, role: str):
        UserProfileDetails.objects.create(
            user_id=user_id,
            role=role
        )

    def get_user_account_by_user_id(
            self, user_id: str) -> UserAccountDTO:
        try:
            user_account = UserAccount.objects.get(
                user_id=user_id)
        except UserAccount.DoesNotExist:
            raise InvalidUserIdException

        return self._get_user_account_dto_from_obj(user_account)

    @staticmethod
    def get_user_profile_details_by_user_id(user_id: str) -> UserProfileDetailsDTO:
        try:
            user_profile = UserProfileDetails.objects.get(
                user_id=user_id)
        except UserProfileDetails.DoesNotExist:
            raise InvalidUserIdException

        return UserProfileDetailsDTO(
            id=str(user_profile.id),
            user_id=str(user_profile.user_id),
            role=user_profile.role
        )

    @staticmethod
    def _get_user_account_dto_from_obj(user_account):
        return UserAccountDTO(
            user_id=str(user_account.user_id),
            username=user_account.username,
            email=user_account.email,
            password=user_account.password)
