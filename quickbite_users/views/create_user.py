import json

from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)

from quickbite_users.presenters.create_user_presenter import \
    CreateUserPresenter


@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def create_user(request):
    request_body = json.loads(request.body)
    from quickbite_users.interactors.create_user_interactor import \
        CreateUserInteractor
    from quickbite_users.storages.user_profile_storage import \
        UserProfileStorage


    interactor = CreateUserInteractor(
        user_profile_storge=UserProfileStorage(),
    )

    username = request_body["username"]
    email = request_body["email"]
    password = request_body["password"]

    return interactor.create_user_wrapper(
        username=username, email=email, password=password,
        presenter=CreateUserPresenter()
    )
