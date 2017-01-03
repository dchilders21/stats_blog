import requests
import urlparse
import subprocess
import warnings

CLIENT_ID = "ZDIYrYeuu09pWRgDaOEsMsteu8u95BzL2BXWc95y"
CLIENT_SECRET = "UumOO1wjPf88gVA93091dlcobrOhrpFw30HeOHwjvr2Ld1o6poqucHCJAPOp0axqvN5ryHvvDjA5lmVT89UD0kuFfhFVCYQqgv9LYLz9VXiZTojrv0JrVV7TqObmf7yf"

USERNAME = 'sammy'
PASSWORD = '1qaz2wsx'

oauth_args = dict(client_id=CLIENT_ID,
                  client_secret=CLIENT_SECRET,
                  grant_type='password',
                  username=USERNAME,
                  password=PASSWORD)

req = requests.post('http://localhost:8000/api/oauth2/token/', data=oauth_args)
print(req.text)
json = req.json()

if 'access_token' in json:
  AUTHORIZATION=json['token_type'] + ' ' + json['access_token']
  print(AUTHORIZATION)
  params = dict(authorization=AUTHORIZATION)
  content = dict(title='automated_title',
                 content='automated_content')
  r = requests.post('http://127.0.0.1:8000/api/posts?format=json', headers=params, data=content)
  print(r.text)
else:
  print('No Key Given')


