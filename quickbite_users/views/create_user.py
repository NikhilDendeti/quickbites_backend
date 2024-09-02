import json
from django.core.exceptions import ValidationError
import re
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_user(request):
    request_body = json.loads(request.body)
    from quickbite_users.interactors.create_user_interactor import \
        CreateUserInteractor
    interactor = CreateUserInteractor()

    username = request_body["username"]
    email = request_body["email"]
    password = request_body["password"]

    return interactor.create_user_wrapper(
        username=username,email=email,password=password)

def validate_username(value):
    if not re.match(r'^[\w.@+-]+$', value):
        raise ValidationError('Invalid username')

def validate_password(value):
    if len(value) < 8:
        raise ValidationError('Password too short')

def validate_email(value):
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$', value):
        raise ValidationError('Invalid email format')