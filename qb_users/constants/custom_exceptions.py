from typing import List


class UserNameAlreadyExistsException(Exception):
    pass


class GetTokensFailedException(Exception):
    pass


class InvalidEmailException(Exception):
    pass


class InvalidPasswordFormat(Exception):
    def __init__(self, messages: List):
        self.messages = messages


class InvalidUserNameLengthException(Exception):
    def __init__(self, error_message: str):
        self.error_message = error_message


class InvalidUserNameFormatException(Exception):
    def __init__(self, error_message: str):
        self.error_message = error_message


class UserNotExistException(Exception):
    pass

class UsernameDoesNotExistException(Exception):
    pass



class InvalidPasswordException(Exception):
    pass

class ObjectDoesNotExist(Exception):
    pass

class GetUserProfileException(Exception):
    pass

class UserNotFoundException(Exception):
    pass

class InvalidUserIdException(Exception):
    pass

