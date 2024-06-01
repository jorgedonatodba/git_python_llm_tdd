import unittest
from math_samples01 import MathSamples

class FibonacciTest(unittest.TestCase):

    def test_fib01(self):
    	self.assertEqual(MathSamples.fibonacci(0), 0)

    def test_fib02(self):
        self.assertEqual(MathSamples.fibonacci(1),1)

    def test_fib03(self):
    	self.assertEqual(MathSamples.fibonacci(2), 1)

    def test_fib04(self):
    	self.assertEqual(MathSamples.fibonacci(3), 2)        

    def test_fib05(self):
    	self.assertEqual(MathSamples.fibonacci(4), 3)         

    def test_fib06(self):
    	self.assertEqual(MathSamples.fibonacci(10), 55)              