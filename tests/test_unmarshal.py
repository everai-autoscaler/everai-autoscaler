import unittest

from everai_autoscaler.model import Factors


class TestUnmarshal(unittest.TestCase):
    def test_unmarshal(self):
        factors = Factors.from_json('{}')
        print(factors)