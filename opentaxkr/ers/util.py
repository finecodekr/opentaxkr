import gettext
import glob
import math
import platform
import re
import unicodedata
from decimal import Decimal

import pycountry

ZERO = Decimal(0)


def yn(value):
    return 'Y' if value else 'N'


def first(fn, iterable):
    return next(filter(fn, iterable))


def percent(rate, decimal_point=0):
    d = Decimal(10 ** decimal_point)
    return math.floor(rate * Decimal(100) * d) / d


def strip(text):
    return re.sub(r'\s+', ' ', text).strip().replace('· ', '·').replace("'", '')


pycountry_translation = gettext.translation('iso3166-1', pycountry.LOCALES_DIR, languages=['ko'])


def country_name(country_code):
    if country_code == 'KR':
        return '한국'

    return pycountry_translation.gettext(pycountry.countries.get(alpha_2=country_code).name)


def deduct(value, max_deduction):
    value = max(0, value)
    return min(value, max_deduction), max(0, max_deduction - value)