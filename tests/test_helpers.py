import unittest

from pyansistring.helpers import (
    find_spans,
    rsearch_separators,
    search_separators,
)
from pyansistring.constants import WHITESPACE, PUNCTUATION

class HelpersTest(unittest.TestCase):
    def test_find_spans(self):
        actual = tuple(find_spans("Hello, World! Hello, World! He", "He"))
        expected = ((0, 2), (14, 16), (28, 30))
        self.assertTupleEqual(actual, expected)

    def test_search_separators(self):
        actual = tuple(
            search_separators("Hello, World!", WHITESPACE.union(PUNCTUATION))
        )
        expected = (", ", "!")
        self.assertTupleEqual(actual, expected)

    def test_rsearch_separators(self):
        actual = tuple(
            rsearch_separators("Hello, World!", WHITESPACE.union(PUNCTUATION))
        )
        expected = ("!", " ,")
        self.assertTupleEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
