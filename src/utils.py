import requests
from requests.auth import HTTPBasicAuth

url = 'http://localhost:8000/o/token/'
hello_url = 'http://localhost:8000/users/'
username = 'admin'
password = 'admin'


data = {
        'grant_type': 'password',
        'username': username,
        'password': password
}
client_id = 'FLt54SmvYwjNDNWTUnDAXqEKf0zGOda6MlStFpXb'
client_secret = 'y6XZgL3dgDKkfIthYZOXHSRtTyf3JZx6nmbhv4vP7yZdRJ2tzNtJN2g8oSX9KYyGnWt8KJVNecYO6YMCzeh7MWiOmo7lfm0kTPenie8EIsbxcv4FnC2EDKk5pleEeKlE'

response = requests.post(url=url, data=data, auth=HTTPBasicAuth(client_id, client_secret))


access_token = response.json().get('access_token')

headers = {
       'Authorization': f'Bearer {access_token}'
}
response = requests.get(url=hello_url, headers=headers)

print(response.text)
