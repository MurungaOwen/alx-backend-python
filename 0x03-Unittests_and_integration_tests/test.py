import unittest
from unittest.mock import Mock, patch
class TestingFn(unittest.TestCase):

    @patch("utils.requests.get")
    def test_mocking(self):
        pass