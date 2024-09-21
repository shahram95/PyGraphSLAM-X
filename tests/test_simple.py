"""Unit tests for the python_package/simple.py module

"""


import unittest

from python_package import simple


class TestSimple(unittest.TestCase):
    """Simple tests."""

    def setUp(self):
        """Setup for the tests."""
        self.s = simple.create_simple()

    def test_get_data(self):
        """Test the ``get_data()`` method."""
        self.assertEqual(self.s.get_data(), 5)

    def test_set_data(self):
        """Test the ``set_data()`` method."""
        self.s.set_data(6)
        self.assertEqual(self.s.get_data(), 6)


if __name__ == '__main__':
    unittest.main()
