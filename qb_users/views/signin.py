import json
from http.client import HTTPResponse

from django.http import HttpResponse
from rest_framework.decorators import api_view, authentication_classes, \
    permission_classes

from qb_users.presenters.signin_presenter import SigninPresenter
from qb_users.serializers import SigninRequestSerializer


@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def sign_in(request):
    data = json.loads(request.body)
    serializer = SigninRequestSerializer(data=data)
    if not serializer.is_valid():
        return HttpResponse(
            json.dumps(
                {"error": "Invalid Data", "details": serializer.errors}),
            status=400
        )

    username = data.get('username')
    password = data.get('password')

    print(f"Username: {username}, Password: {password}")

    from qb_users.interactors.signin_user_interactor import \
        SignInInteractor
    from qb_users.storages.user_profile_storage import \
        UserProfileStorage

    interactor = SignInInteractor(
        user_profile_storge=UserProfileStorage(),
    )

    # Get the result from the interactor
    result = interactor.login_user_wrapper(
        username=username, password=password,presenter= SigninPresenter)

    return result
