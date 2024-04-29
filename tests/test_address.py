from unittest import TestCase

from opentaxkr.ers.address import 도로명주소


class TestAddress(TestCase):
    def test_address(self):
        a = 도로명주소.parse('세종 보람동로 14, 809동 1402호 (보람동,호려울마을8단지)')
        a = 도로명주소.parse('인천광역시 남구 염창로 35 1414 (주안동, 베스티움)')
        print(a)