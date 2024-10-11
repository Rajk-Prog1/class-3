from homework.loops.loops import loops


class TestLoops(object):
    def test_squares_of_5_numbers(self):
        assert loops(5) == [0, 1, 4, 9, 16]

    def test_squares_of_9_numbers(self):
        assert loops(9) == [0, 1, 4, 9, 16, 25, 36, 49, 64]

    def test_edge_case_n_equals_1(self):
        assert loops(1) == [0]

    def test_edge_case_n_equals_20(self):
        assert loops(20) == [
            0,
            1,
            4,
            9,
            16,
            25,
            36,
            49,
            64,
            81,
            100,
            121,
            144,
            169,
            196,
            225,
            256,
            289,
            324,
            361,
        ]

    def test_n_zero(self):
        assert loops(0) == []
