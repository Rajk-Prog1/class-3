from homework.lists.lists import lists


class TestLists(object):

    def test_insert(self):
        assert lists(["insert 0 5", "return"]) == [5]
        assert lists(["insert 0 5", "insert 1 10", "return"]) == [5, 10]

    def test_append(self):
        assert lists(["append 5", "return"]) == [5]
        assert lists(["append 5", "append 10", "return"]) == [5, 10]

    def test_remove(self):
        assert lists(["append 5", "append 10", "remove 5", "return"]) == [10]
        assert lists(["append 5", "append 10", "remove 10", "return"]) == [5]

    def test_sort(self):
        assert lists(["append 5", "append 3", "sort", "return"]) == [3, 5]
        assert lists(["append 10", "append 5", "append 1", "sort", "return"]) == [
            1,
            5,
            10,
        ]

    def test_pop(self):
        assert lists(["append 5", "append 10", "pop", "return"]) == [5]
        assert lists(["append 1", "append 2", "append 3", "pop", "return"]) == [1, 2]

    def test_reverse(self):
        assert lists(["append 5", "append 10", "reverse", "return"]) == [10, 5]
        assert lists(["append 1", "append 2", "append 3", "reverse", "return"]) == [
            3,
            2,
            1,
        ]

    def test_complex_case_1(self):
        assert lists(
            [
                "insert 0 5",
                "insert 1 10",
                "insert 0 6",
                "remove 6",
                "append 9",
                "append 1",
                "sort",
                "pop",
                "reverse",
                "return",
            ]
        ) == [9, 5, 1]

    def test_complex_case_2(self):
        assert lists(
            [
                "append 1",
                "append 6",
                "append 10",
                "append 8",
                "append 9",
                "append 2",
                "append 12",
                "append 7",
                "append 3",
                "append 5",
                "insert 8 66",
                "insert 1 30",
                "insert 6 75",
                "insert 4 44",
                "insert 9 67",
                "insert 2 44",
                "insert 9 21",
                "insert 8 87",
                "insert 1 75",
                "insert 1 48",
                "reverse",
                "sort",
                "append 2",
                "append 5",
                "remove 2",
                "return",
            ]
        ) == [1, 3, 5, 6, 7, 8, 9, 10, 12, 21, 30, 44, 44, 48, 66, 67, 75, 75, 87, 2, 5]
