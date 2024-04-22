import re


def 연월일(dateobj):
    return dateobj.strftime('%Y%m%d')


def date(dateobj):
    return dateobj.strftime('%Y-%m-%d')


def strip_dash(text):
    return text.replace('-', '') or '-'


전화번호_첫자리 = [
    # 공통서비스
    '030',
    '050',
    '060',
    '070',
    '080',
    # 지역번호
    '02',
    '031',
    '032',
    '033',
    '041',
    '042',
    '043',
    '044',
    '051',
    '052',
    '053',
    '054',
    '055',
    '061',
    '062',
    '063',
    '064',
    # 휴대폰
    '010',
    '011',
    '012',
    '015',
    '016',
    '017',
    '018',
    '019',
]


전화번호_pattern = re.compile(f'({"|".join(전화번호_첫자리)})-?([0-9]{{3,4}})-?([0-9]{{4}})')


def 지역번호(phone_number):
    if not phone_number: return ''
    try:
        return 전화번호_pattern.match(phone_number).group(1)
    except:
        return ''


def 국번(phone_number):
    if not phone_number: return ''
    try:
        return 전화번호_pattern.match(phone_number).group(2)
    except:
        return ''


def 전화번호_나머지(phone_number):
    if not phone_number: return ''
    try:
        return 전화번호_pattern.match(phone_number).group(3)
    except:
        return ''
