from django.test import TestCase
from app.calc import add


class CalcTest(TestCase):
    def test_add_function(self):
        """Test two numbers addition"""
        self.assertEqual(add(2, 3), 5)
