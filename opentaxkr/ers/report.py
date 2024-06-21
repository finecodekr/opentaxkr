import csv
import os
import re


FORMAT_DOC_DIR = os.path.dirname(__file__)


with open(FORMAT_DOC_DIR + '/전국세무서.csv', encoding='utf-8-sig') as f:
    전국세무서정보 = [{k: v.strip() for k, v in row.items()} for row in csv.DictReader(f)]


# TODO replace this with util.법정동코드표
with open(FORMAT_DOC_DIR + '/법정동코드_국세청홈페이지_18년6월7일.csv', encoding='utf8') as f:
    법정동코드표_국세청 = [[col for col in row] for row in csv.reader(f)]


def find_세무서코드(주소):
    주소 = re.sub(' +', ' ', 주소)
    주소 = re.sub('서울시 ', '서울특별시 ', 주소) # 서울특별시로 일괄 맞춤

    시도, *나머지 = 주소.split(' ')
    match = re.match(r'([^,]*[시군구])\s+(.*)', ' '.join(나머지))
    시군구 = match.group(1) if match else ''
    시군구_이하주소 = match.group(2) if match else ' '.join(나머지)

    법정동주소_candidate = 시군구_이하주소.split(' ')[0]
    if re.match('.*로', 법정동주소_candidate) or re.match('.*길', 법정동주소_candidate):
        # 도로명주소로는 세무서를 찾을 수 없다. 괄호 안에 있는 내용을 이용함
        법정동 = re.match(r'.+?\(([^,]+\d가|[^, ()]+동|[^, ]+읍).*\)', 시군구_이하주소).group(1).replace(' ', '')
    else:
        법정동 = 시군구_이하주소.split(' ')[0]

    try:
        return next(filter(lambda row: 시도 == row[2] and row[3] == 시군구 and 법정동 == row[4], 법정동코드표_국세청))[0]
    except StopIteration:
        return next(filter(lambda row: 시도 == row[2] and row[3] == 시군구, 법정동코드표_국세청))[0]


def 세무서명(세무서코드):
    try:
        return next(filter(lambda row: row['세무서코드'] == 세무서코드, 전국세무서정보))['세무서명']
    except StopIteration:
        return None


def validate_사업자등록번호(target):
    if len(target) != 10 or not target.isdigit():
        return False

    code = "137137135"
    check_sum = sum([int(a) * int(b) for a, b in zip(code, target[:-1])])
    check_sum = (check_sum + int(target[-2]) * 5 // 10) % 10

    return int(target[-1]) == (check_sum if check_sum == 0 else 10 - check_sum)
