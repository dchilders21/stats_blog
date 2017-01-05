from django import template
import datetime
import pytz

register = template.Library()


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


@register.filter(name='is_today')
def is_today(value):
    print(value)
    today = tz2ntz(datetime.datetime.utcnow(), 'UTC', 'US/Pacific').strftime('%m/%d/%y')
    print(today)

    if value > today:
        return True
    else:
        return False
