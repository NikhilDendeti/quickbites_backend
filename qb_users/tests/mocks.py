def create_token_response_mock(mocker):
    from oauth2_provider.views import TokenView

    func_to_mock = TokenView.create_token_response
    path = f"{func_to_mock.__module__}.{func_to_mock.__qualname__}"
    return mocker.patch(path)

def signin_token_response_mock(mocker):
    from quickbite_users.interactors.mixins.access_tokens_mixin\
        import AccessTokenMixin

    func_to_mock = AccessTokenMixin.get_tokens
    path = f"{func_to_mock.__module__}.{func_to_mock.__qualname__}"
    return mocker.patch(path)
