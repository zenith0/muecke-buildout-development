__author__ = 'stefan'
from django import template
import locale
import decimal

register = template.Library()

@register.filter(name='currency')
def currency(value):
    try:
        locale.setlocale(locale.LC_ALL,'de_DE.UTF-8')
    except:
        locale.setlocale(locale.LC_ALL,'')
    value = decimal.Decimal(value)
    loc = locale.localeconv()
    return locale.currency(value, loc['currency_symbol'], grouping=True)
