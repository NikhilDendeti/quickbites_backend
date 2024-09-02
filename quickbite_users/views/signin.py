from django.views.decorators.csrf import csrf_exempt
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework.decorators import api_view, authentication_classes
from django.http import JsonResponse
import json
from django.core.exceptions import ValidationError
import re


# @api_view(["POST"])
@csrf_exempt
def sign_in(request):
    # Accessing the data using DRF's request.data
    data = json.loads(request.body)

    # Example usage of the parsed data
    username = data.get('username')
    password = data.get('password')

    print(f"Username: {username}, Password: {password}")

    from quickbite_users.interactors.signin_user_interactor import \
        SignInInteractor
    interactor = SignInInteractor()

    # Get the result from the interactor
    result = interactor.login_user_wrapper(
        username=username, password=password)

    return result

