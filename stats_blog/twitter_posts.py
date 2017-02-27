from twython import Twython
import requests
import datetime
import pytz

APP_KEY = 'kvow7dyFxzzjeCEaANZeCfzjO'
APP_SECRET = 'yCu5AFXwqK10n5qZxbQKKnIkaT2OMharZZRqdZXPp0myxgwrWb'

OAUTH_TOKEN = '820869365868306432-MWGoXbPsgUL1tItHlA9T85VwEzUNw9v'
OAUTH_TOKEN_SECRET = 'UPqQotuGyzSeueBdmX5LAJLyBCOH6QF0nctskiFZxIaXM'


twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


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

last_game = data[-1]

title = last_game['away_market'] + ' ' + last_game['away_team'] + ' @ ' + last_game['home_market'] + ' ' + last_game['home_team'] + ' ' + today
categories = 'NBA'

winner = last_game['away_team'] if last_game['away_result_preds'] == 1.0 else last_game['home_team']

total = last_game['home_pts_preds'] + last_game['away_pts_preds']

line = "Over" if total >= last_game['over_under'] else "Under"

content = last_game['away_market'] + ' ' + last_game['away_team'] + ' ' + str(last_game['spread']) + '.' + ' Over/Under ' + str(
    last_game['over_under']) + '. ' + \
          winner + ' and the ' + line + '. #nbabets #pickem #sportsbettor sharperpicks.com'

twitter.update_status(status=content)

print('updated status')

