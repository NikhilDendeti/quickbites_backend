import factory
from factory import Sequence
from quickbite_users.dtos import UserAccountDTO, TokenDTO, UserTokenDTO, \
    UserSigninDTO, UserProfileCompleteDetailsDTO, UserProfileDetailsDTO


class UserAccountDTOFactory(factory.Factory):
    class Meta:
        model = UserAccountDTO

    user_id = Sequence(lambda n: n + 1)
    username = Sequence(lambda n: f'user_{n}')
    email = Sequence(lambda n: f'user{n}@example.com')
    password = Sequence(lambda n: f'password{n}')


class TokenDTOFactory(factory.Factory):
    class Meta:
        model = TokenDTO

    access_token = Sequence(lambda n: f'access_token_{n}')
    refresh_token = Sequence(lambda n: f'refresh_token_{n}')
    expires_in = '3600'


class UserTokenDTOFactory(TokenDTOFactory):
    class Meta:
        model = UserTokenDTO

    user_id = Sequence(lambda n: f'user_id_{n}')


class UserSigninDTOFactory(factory.Factory):
    class Meta:
        model = UserSigninDTO

    username = Sequence(lambda n: f'signin_user_{n}')
    password = Sequence(lambda n: f'signin_password{n}')


class UserProfileCompleteDetailsDTOFactory(factory.Factory):
    class Meta:
        model = UserProfileCompleteDetailsDTO

    username = Sequence(lambda n: f'complete_user_{n}')
    email = Sequence(lambda n: f'complete{n}@example.com')
    role = Sequence(lambda n: ['vendor', 'student', 'employee'][n % 3])
    user_id = Sequence(lambda n: f'complete_user_id_{n}')


class UserProfileDetailsDTOFactory(factory.Factory):
    class Meta:
        model = UserProfileDetailsDTO

    id = Sequence(lambda n: f'details_id_{n}')
    user_id = Sequence(lambda n: f'details_user_id_{n}')
    role = Sequence(lambda n: ['vendor', 'student', 'employee'][n % 3])
