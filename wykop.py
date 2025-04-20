import requests

url = 'https://wykop.pl/api/v3/auth'  # Replace with the actual URL

# Your actual key and secret
api_key = 'w563a9212ef4f7494d73489740d76a1d27'
api_secret = 'f4f0f521ab9c997f4e7860d07b6114f4'

# JSON body as requested
payload = {
    'data': {
        'key': api_key,
        'secret': api_secret
    }
}

# Set headers correctly
headers = {
    'Content-Type': 'application/json'
}

# Send request
response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    token_data = response.json()
    access_token = token_data['data']['token']
    print(access_token)

api_url = 'https://wykop.pl/api/v3/tags/popular'  # Replace with actual endpoint
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

response = requests.get(api_url, headers=headers)
if response.status_code == 200:
    print("Response data:", response.json())
else:
    print(f"Failed request: {response.status_code}, {response.text}")
