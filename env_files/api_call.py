import json


def make_api_call():
    import requests

    # URL of the API endpoint
    url = "http://127.0.0.1:8000/office_eats_users/create/user/"

    # Data to be sent in the POST request
    data = json.dumps({
        "user_name": "name",
        "email": "email",
        "password": "password"
    })

    # Send a POST request to the API
    response = requests.post(url, data=data)

    # Check if the request was successful
    if response.status_code == 201:
       print("success fully created")
    else:
        print(f"Failed to create data: {response.status_code}")

make_api_call()