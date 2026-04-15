import httpx

login_payload = {
    "email": "user@example.com",
    "password": "string"
}

client = httpx.Client(base_url='http://localhost:8000/api/v1')

login_response = client.post('authentication/login', json=login_payload)
login_response_data = login_response.json()
access_token = login_response_data['token']['accessToken']

headers = {
    "authorization": f"Bearer {access_token}"
}
response_user_me =  client.get('users/me', headers=headers)
response_user_me_data = response_user_me.json()

print(f"Status-code: {response_user_me.status_code}")
print(response_user_me_data)



