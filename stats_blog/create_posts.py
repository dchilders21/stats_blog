import requests
import datetime
import pytz

CLIENT_ID = "KFzaBysyi0lyPM8yqHovUZGWfYNMoQPRtEBHu4ef"
CLIENT_SECRET = "xxnkHpzjbR84IaLX387Lar1q9RkC1jQQgfWcchcnOmjhlXZ5tuiHgE5QVjdPlk34lMBMCefOiePRPuw8Axlf8vX9exs1dHdVX3a63MDoCG1UR11TQoOxYoG8M4KXeeMZ"

USERNAME = 'sammy'
PASSWORD = '1qaz2wsx'

oauth_args = dict(client_id=CLIENT_ID,
                  client_secret=CLIENT_SECRET,
                  grant_type='password',
                  username=USERNAME,
                  password=PASSWORD)


def tz2ntz(date_obj, tz, ntz):
    """
    :param date_obj: datetime object
    :param tz: old timezone
    :param ntz: new timezone
    """
    if isinstance(date_obj, datetime.date) and tz and ntz:
       date_obj = date_obj.replace(tzinfo=pytz.timezone(tz))
       return date_obj.astimezone(pytz.timezone(ntz))
    return False


todays_request = requests.get('http://162.243.153.66/api')
todays_data = todays_request.json()

data = todays_data['data']

today = tz2ntz(datetime.datetime.utcnow(), 'UTC', 'US/Pacific').strftime('%m/%d/%y')
print(today)

req = requests.post('http://sharperpicks.com/api/oauth2/token/', data=oauth_args)
print(req.text)
json = req.json()

if 'access_token' in json:
    AUTHORIZATION = json['token_type'] + ' ' + json['access_token']
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
        r = requests.post('http://sharperpicks.com/api/posts?format=json', headers=params, data=content_data)

        print(r)

else:
    print('No Key Given')


