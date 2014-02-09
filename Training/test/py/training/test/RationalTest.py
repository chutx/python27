'''
Created on Jan 23, 2014

@author: angelo
'''
import unittest

from py.training.Rational import Rational


class RationalTest(unittest.TestCase):

    def setUp(self):
        self.numOne = Rational(numer=1, denom=2);
    
    def tearDown(self):
        pass
    
    def testSum(self):
        # Setup         
        otherRational = Rational(numer=1, denom=2);
        expected = Rational(numer=1, denom=1);
        # Execute         
        result = self.numOne.sum(otherRational)
        # Assert         
        self.assertEqual(expected, result, "The sum is incorrect")
    
    def testSub(self):
        #Setuo
        expected = Rational(1, 4)
        otherRational = Rational(numer=1, denom=4);
        #Execute
        result = self.numOne.sub(otherRational)
        #Assert
        self.assertEqual(expected, result, "Subtraction operation is wrong")
        
    def testMult(self):
        #Setup
        expected = Rational(1)
        otherRational = Rational(2, 1)
        #Execute
        result = self.numOne.mult(otherRational)
        #Assert
        self.assertEqual(expected, result, "Multiplication is incorrect")
        
    def testDiv(self):
        #Setup
        expected = Rational(1)
        otherRational = Rational(1, 2)
        #Execute
        result = self.numOne.div(otherRational)
        #Assert
        self.assertEqual(expected, result, "Division is incorrect")
        
        
        
        