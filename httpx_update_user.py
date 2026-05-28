import httpx
from tools.fakers import fake

client = httpx.Client(base_url='http://localhost:8000/api/v1')

create_user_payload = {
    "email": fake.email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = client.post('users', json=create_user_payload)
create_user_response_data = create_user_response.json()
print(f"Status-code: {create_user_response.status_code}")
print("Create user date:", create_user_response_data)

login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}

login_response = client.post('authentication/login', json=login_payload)
login_response_data = login_response.json()

update_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}

update_user_payload = {
    "email": fake.email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

update_user_response = client.patch(f'users/{create_user_response_data["user"]["id"]}',
                                    headers=update_user_headers, json=update_user_payload)
update_user_response_data = update_user_response.json()
print(f"\nStatus-code: {update_user_response.status_code}")
print(f"Update user data: {update_user_response_data}")
