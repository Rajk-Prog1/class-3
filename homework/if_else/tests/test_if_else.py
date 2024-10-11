from homework.if_else.if_else import if_else


class TestIfElse(object):
    def test_odd_small(self):
        assert if_else(3) == "Weird"

    def test_odd_medium(self):
        assert if_else(17) == "Weird"

    def test_odd_large(self):
        assert if_else(99) == "Weird"

    def test_even_small(self):
        assert if_else(2) == "Not Weird"

    def test_even_medium(self):
        assert if_else(20) == "Weird"

    def test_even_large(self):
        assert if_else(100) == "Not Weird"
