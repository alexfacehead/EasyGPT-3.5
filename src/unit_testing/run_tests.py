import unittest
from src.unit_testing.testing import TestContentGenerator
from .testing import TestContentGenerator

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestContentGenerator))