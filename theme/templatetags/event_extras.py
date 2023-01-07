from django import template
from datetime import datetime

register = template.Library()

@register.filter(name='format_datetime')
def format_datetime(butterdatetime):
    """Takes butter datetime string and returns formatted datetime in EST"""
    datetime_object = datetime.strptime(butterdatetime, '%Y-%m-%dT%H:%M:%S')
    return datetime_object

@register.filter(name='format_date')
def format_date(butterdatetime):
    """Takes butter datetime string and returns formatted date"""
    datetime_object = datetime.strptime(butterdatetime, '%Y-%m-%dT%H:%M:%S').date()
    return datetime_object