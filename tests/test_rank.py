import unittest
from src.numrank import rank


class TestRank(unittest.TestCase):
    def test_rank(self):
        self.assertEqual(rank(["1 2 1"]), [(1.0, 2), (2.0, 1)])


if __name__ == "__main__":
    unittest.main()
