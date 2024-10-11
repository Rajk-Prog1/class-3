from homework.leap_year.leap_year import leap_year


class TestLeapYear(object):

    def test_leap_year_divisible_by_400(self):
        assert leap_year(2000) == True

    def test_not_leap_year_divisible_by_100_not_400(self):
        assert leap_year(2100) == False

    def test_leap_year_divisible_by_400_edge_case(self):
        assert leap_year(2400) == True

    def test_not_leap_year_random(self):
        assert leap_year(3455) == False

    def test_not_leap_year_not_divisible_by_4(self):
        assert leap_year(1990) == False

    def test_leap_year_divisible_by_4(self):
        assert leap_year(1992) == True
