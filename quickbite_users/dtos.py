from dataclasses import dataclass


@dataclass
class UserAccountDTO:
    user_id:str
    username: str
    email: str
    password: str


@dataclass
class   TokenDTO:
    access_token: str
    refresh_token: str
    expires_in: str

@dataclass
class UserTokenDTO(TokenDTO):
    user_id: str


@dataclass
class UserSigninDTO:
    username:str
    password:str
    
@dataclass
class UserProfileCompleteDetailsDTO:
    username: str
    email: str
    role: str
    user_id: str

@dataclass
class UserProfileDetailsDTO:
    id: str
    user_id: str
    role: str


