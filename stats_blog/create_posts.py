import requests
import datetime
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


todays_request = requests.get('http://162.243.153.66/api')
todays_data = todays_request.json()

data = todays_data['data']

today = datetime.date.today().strftime('%m/%d/%y')
print(today)

req = requests.post('http://localhost:8000/api/oauth2/token/', data=oauth_args)
json = req.json()

if 'access_token' in json:
    AUTHORIZATION=json['token_type'] + ' ' + json['access_token']
    print(AUTHORIZATION)
    params = dict(authorization=AUTHORIZATION)

    for d in data:
        title = d['away_team'] + ' @ ' + d['home_team'] + ' ' + today
        categories = 'NBA'

        winner = d['away_team'] if d['away_result_preds'] == 1.0 else d['home_team']

        total = d['home_pts_preds'] + d['away_pts_preds']

        line = "Over" if total >= d['over_under'] else "Under"

        content = d['away_team'] + ' ' + str(d['spread']) + '.' + ' Over/Under ' + str(d['over_under']) + '. ' + \
                        winner + ' and the ' + line + '.'

        content_data = dict(title=title,
                            content=content,
                            categories=categories)
        r = requests.post('http://127.0.0.1:8000/api/posts?format=json', headers=params, data=content_data)

        print(r)

else:
  print('No Key Given')


