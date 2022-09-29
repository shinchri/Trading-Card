from django import template

register = template.Library()

def get_int(value):
  # get rid of decimals
  return int(value)

register.filter('get_int', get_int)