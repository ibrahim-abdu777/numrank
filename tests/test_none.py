import unittest
from src.numrank import rank


class TestNone(unittest.TestCase):
    def test_none(self):
        self.assertEqual(rank(["a b"]), [])


if __name__ == "__main__":
    unittest.main()
