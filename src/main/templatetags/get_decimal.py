from django import template

register = template.Library()

def get_decimal(value):
  changed_value = int((value*100)%100)
  if changed_value == 0:
    return "00"
  return changed_value

register.filter('get_decimal', get_decimal)