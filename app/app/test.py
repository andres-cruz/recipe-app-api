# Sample tests
from django.test import SimpleTestCase # type: ignore

from app import calc

class CalcTest(SimpleTestCase):
  def test_add_numers(self):
    # Test adding numbers together
    res = calc.add(5, 5)
    self.assertEqual(res, 10)