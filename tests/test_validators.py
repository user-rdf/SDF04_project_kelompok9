import unittest

from src.utils import is_positive_quantity, is_valid_email


class ValidatorTests(unittest.TestCase):
    def test_valid_email(self) -> None:
        self.assertTrue(is_valid_email("user@example.com"))
        self.assertFalse(is_valid_email("invalid-email"))

    def test_positive_quantity(self) -> None:
        self.assertTrue(is_positive_quantity(1))
        self.assertFalse(is_positive_quantity(0))
        self.assertFalse(is_positive_quantity(-1))


if __name__ == "__main__":
    unittest.main()
