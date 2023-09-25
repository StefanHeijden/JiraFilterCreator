from operations import *
import unittest


class TestIsIn(unittest.TestCase):
    def test_is_in_string(self):
        result = is_in("field", "test")
        self.assertEqual("field = test", result)

    def test_is_in_list(self):
        result = is_in("field", ["test"])
        self.assertEqual("field = test", result)

    def test_is_in_summary(self):
        result = is_in("summary", ["test"])
        self.assertEqual("summary ~ test", result)

    def test_multiple_entries(self):
        result = is_in("field", ["test1", "test2"])
        self.assertEqual('field in ("test1", "test2")', result)


if __name__ == '__main__':
    unittest.main()

