import unittest
from Project2 import get_distance


class TestFile(unittest.TestCase):
    def test_get_distance(self):
        self.assertEqual(get_distance('1311 39th st Des Moines Iowa', '7235 Kingsland Drive Memphis Tennessee'), 1013)

if __name__ == '__main__':
    unittest.main()