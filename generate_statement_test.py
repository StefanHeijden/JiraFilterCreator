from generate_statement import *
import unittest


def get_example(filename):
    file = open(filename, "r")
    result = ""
    for line in file:
        result = result + line
    file.close()
    return result


class TestGenerateFilter(unittest.TestCase):
    def test_backend_filter(self):
        result = generate_statement("values/backend.json")
        self.assertEqual(get_example("examples/backend"), result)


if __name__ == '__main__':
    unittest.main()

