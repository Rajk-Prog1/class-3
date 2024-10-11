from homework.if_else.if_else import if_else


class TestIfElse(object):
    def test_odd_small(self):
        assert if_else(3) == "Weird"

    def test_odd_medium(self):
        assert if_else(17) == "Weird"

    def test_odd_large(self):
        assert if_else(99) == "Weird"

    def test_even_2_to_5(self):
        assert if_else(2) == "Not Weird"
        assert if_else(4) == "Not Weird"

    def test_even_6_to_20(self):
        assert if_else(6) == "Weird"
        assert if_else(20) == "Weird"

    def test_even_greater_than_20(self):
        assert if_else(22) == "Not Weird"

    def test_lower_bound(self):
        assert if_else(1) == "Weird"

    def test_upper_bound(self):
        assert if_else(100) == "Not Weird"

    def test_edge_cases(self):
        assert if_else(20) == "Weird"
        assert if_else(5) == "Weird"
