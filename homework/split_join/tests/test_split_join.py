from homework.split_join.split_join import split_join


class TestSplitJoin(object):

    def test_single_word(self):
        assert split_join("word") == "word"

    def test_empty_string(self):
        assert split_join("") == ""

    def test_simple_sentence(self):
        assert split_join("this is a string") == "this-is-a-string"

    def test_long_sentence(self):
        assert (
            split_join("quick brown fox jumps over a lazy dog")
            == "quick-brown-fox-jumps-over-a-lazy-dog"
        )

    def test_multiple_spaces_between_words(self):
        assert (
            split_join("multiple   spaces    between words")
            == "multiple---spaces----between-words"
        )
