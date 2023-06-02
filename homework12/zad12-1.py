#!/usr/bin/python3
import unittest
import math
from homework6 import Vector

class TestVector(unittest.TestCase):   # the class name starts with 'Test'
    def setUp(self):
        print("Creating Vector v(3,1,-3) and vector w(5,-2,-2) for testing")
        self.v = Vector(3, 1, -3)
        self.w = Vector(5, -2, -2)
    # individual tests
    def test_vector(self):
        self.assertNotEqual(self.v, self.w)
        self.assertEqual(self.v + self.w, Vector(8, -1, -5))
        self.assertEqual(self.v - self.w, Vector(-2, 3, -1))
        self.assertEqual(self.v * self.w, 19)
        
    # individual tests
    def test_vector_length(self):
        self.assertEqual(self.v.length(),  math.sqrt(19))

    def tearDown(self):
        print("cleaning")
        pass

if __name__ == "__main__":
    unittest.main()