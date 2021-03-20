from django.test import TestCase
from project.logic import operation

# Create your tests here.
class LogicTestCase(TestCase):
    def test_plus(self):
        result = operation(1, 2, '+')
        self.assertEqual(3, result)

    def test_minus(self):
        result = operation(1, 2, '-')
        self.assertEqual(-1, result)
    
    def test_multiply(self):
        result = operation(1, 2, '*')
        self.assertEqual(2, result)