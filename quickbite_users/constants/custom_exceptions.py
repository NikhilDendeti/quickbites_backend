
class UserNameAlreadyExistsException(Exception):
    pass


class GetTokensFailedException(Exception):
    pass

class InvalidEmailException(Exception):
    pass

class InvalidPasswordFormat(Exception):
    def __init__(self, error_message: str):
        self.error_message = error_message

class InvalidUserNameLengthException(Exception):
    def __init__(self, error_message: str):
        self.error_message = error_message

class InvalidUserNameFormatException(Exception):
    def __init__(self, error_message: str):
        self.error_message = error_message


