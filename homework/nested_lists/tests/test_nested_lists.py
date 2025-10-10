from homework.nested_lists.nested_lists import nested_lists


class TestNestedLists(object):

    def test_single_student_with_second_lowest(self):
        assert nested_lists(
            [["Prashant", 32], ["Pallavi", 36], ["Dheeraj", 39], ["Shivam", 40]]
        ) == ["Pallavi"]

    def test_multiple_students_with_second_lowest(self):
        assert nested_lists(
            [
                ["Harry", 37.21],
                ["Berry", 37.21],
                ["Tina", 37.2],
                ["Akriti", 41],
                ["Harsh", 39],
            ]
        ) == ["Berry", "Harry"]

    def test_negative_grades(self):
        assert nested_lists(
            [["Sona", -25.001], ["Mona", -25.0001], ["Mini", -25.000], ["Rita", -25.0]]
        ) == ["Mona"]

    def test_identical_grades(self):
        assert nested_lists(
            [["Amy", 50], ["David", 50], ["Eva", 50], ["John", 60], ["Paul", 60]]
        ) == ["John", "Paul"]

    def test_all_unique_grades(self):
        assert nested_lists(
            [
                ["Alan", 20],
                ["Brianna", 30],
                ["Charlie", 40],
                ["Diana", 50],
                ["Elena", 60],
            ]
        ) == ["Brianna"]
