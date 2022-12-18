from django import template
from datetime import datetime

register = template.Library()

@register.filter(name='format_datetime')
def format_datetime(butterdatetime):
    """Takes butter datetime string and returns formatted datetime in EST"""
    datetime_object = datetime.strptime(butterdatetime, '%Y-%m-%dT%H:%M:%S')
    print(datetime_object)
    return datetime_object