import json

import requests
from django.http import HttpRequest
from oauth2_provider.views import TokenView
from requests.auth import HTTPBasicAuth

def get_access_token():
    # Define the URL
    url = 'http://localhost:8000/o/token/'

    # Define the payload (data)
    payload = {
        "grant_type": "password",
        "username": "admin",
        "password": "admin"
    }

    # Define the client_id and client_secret
    client_id = "ntMteXULnGTDD3b96uYYKxMGbICU9W2PgXWYIxUL"
    client_secret = "CgZb8pjHwIX3M6Am4Bj1jmAMnpI0MuebLCoeWg1OVVLV8g38yxUp5LpzSzS7RZUYGCJrz2uQIuIuIE5wblL7cEl5evBhOwP7Hv2HjcvrHfHrAUz5sREQBF0irbuCAkQF"

    # Make the POST request
    response = requests.post(url, data=payload, auth=HTTPBasicAuth(client_id, client_secret))

    # Check if the request was successful
    try:
        response.raise_for_status()  # Raises an HTTPError for bad responses
        response_data = response.json()  # Attempt to parse JSON
        print("Status Code:", response.status_code)
        print("Response Content:", response_data)
        return response_data["access_token"]
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")  # Print the error if the request failed
    except requests.exceptions.JSONDecodeError:
        print("Response is not in JSON format.")
        print("Response Text:", response.text)  # Print the raw response text


def call_sign_in_api():
    # Obtain the access token
    access_token = get_access_token()

    # Check if access token retrieval was successful
    if not access_token:
        print("Failed to obtain access token.")
        return

    # Define the URL and request body
    url = 'http://127.0.0.1:8000/quickbite_users/signin/user/'
    request_body = {
        "username": "nikhil",  # Changed to "username" for consistency
        "password": "Nikhil@1234"
    }

    # Set up the headers with the Authorization token
    headers = {
        'Authorization': f'Bearer {access_token}',
        "Content-Type": "application/json"
    }

    # Make the POST request
    response = requests.post(url, headers=headers,
                             data=json.dumps(request_body))

    # Print the response status code
    print(f"Status Code: {response.status_code}")

    # Try to parse the response as JSON, otherwise print the raw text
    try:
        response_data = response.json()
        print(f"Response Body (JSON): {response_data}")
    except json.JSONDecodeError:
        print(f"Response Body (Text): {response.text}")

#
# def get_token():
#     client_id = "ntMteXULnGTDD3b96uYYKxMGbICU9W2PgXWYIxUL"
#     client_secret = "CgZb8pjHwIX3M6Am4Bj1jmAMnpI0MuebLCoeWg1OVVLV8g38yxUp5LpzSzS7RZUYGCJrz2uQIuIuIE5wblL7cEl5evBhOwP7Hv2HjcvrHfHrAUz5sREQBF0irbuCAkQF"
#
#     request = HttpRequest()
#     request.META = {
#         "Content-Type": "application/x-www-form-urlencoded",
#         "Cache-Control": "no-cache"
#     }
#     request.method = 'POST'
#     request.POST = {
#         "client_id": client_id,
#         "client_secret": client_secret,
#         "grant_type": "password",
#         "scope": "read",
#         "username": "admin",
#         "password": "admin"
#
#     }
#
#     token_view = TokenView()
#     try:
#
#         url, headers, body, status_code = token_view.create_token_response(
#             request)
#         print(body)
#
#     except Exception as err:
#         raise err


def get_tokens():
    client_id = "ntMteXULnGTDD3b96uYYKxMGbICU9W2PgXWYIxUL"
    client_secret = "CgZb8pjHwIX3M6Am4Bj1jmAMnpI0MuebLCoeWg1OVVLV8g38yxUp5LpzSzS7RZUYGCJrz2uQIuIuIE5wblL7cEl5evBhOwP7Hv2HjcvrHfHrAUz5sREQBF0irbuCAkQF"
    request=HttpRequest()
    request.META={
        "Content-Type": "application/x-www-form-urlencoded",
        "Cache-Control": "no-cache"
    }
    request.method='POST'
    request.POST={
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "password",
        "scope": "read,write",
        "username": "admin",
        "password": "admin"
    }
    token_view=TokenView()
    try:

        url, headers, body, status_code = token_view.create_token_response(
            request)

    except Exception as err:
        raise err

    return body
