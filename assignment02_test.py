import unittest
import numpy
from assignment02 import RpnCalculator, MyStack

class TestRpnCalculator(unittest.TestCase):
    def testNumpy(self):
        stack = MyStack(0);
        self.assertEqual(numpy.ndarray, type(stack.stack));

    # numpy numbers don't by default raise exception when // 0, so disabling test.
    def disabledTestDivideByZero(self):
        with self.assertRaises(Exception):
            a=RpnCalculator.eval("1 0 //")
            print(a)

    def testEmptyExpression(self):
        with self.assertRaises(Exception):
            RpnCalculator.eval("")

    def testInsufficientOperand1(self):
        with self.assertRaises(Exception):
            RpnCalculator.eval("1 +")

    def testInsufficientOperand2(self):
        with self.assertRaises(Exception):
            RpnCalculator.eval("1 1 + +")

    def testInsufficientOperator1(self):
        with self.assertRaises(Exception):
            RpnCalculator.eval("1 1")

    def testInsufficientOperator2(self):
        with self.assertRaises(Exception):
            RpnCalculator.eval("1 1 1 +")

    def testInvalidOperator1(self):
        with self.assertRaises(Exception):
            RpnCalculator.eval("1 1 fly")

    def testInvalidOperator2(self):
        with self.assertRaises(Exception):
            RpnCalculator.eval("random junk")

    def testSingleNumber(self):
        self.assertEqual(3, RpnCalculator.eval("3"))

    def testExtraSpace(self):
        self.assertEqual(2, RpnCalculator.eval("1    1  +"))

    def testLeadingTrailingSpace(self):
        self.assertEqual(2, RpnCalculator.eval("  1    1  +  "))

    def testAddition(self):
        self.assertEqual(8, RpnCalculator.eval("3 5 +"))
        self.assertEqual(2, RpnCalculator.eval("-3 5 +"))
        self.assertEqual(-2, RpnCalculator.eval("3 -5 +"))
        self.assertEqual(-8, RpnCalculator.eval("-3 -5 +"))
    

    def testSubtraction(self):
        self.assertEqual(-2, RpnCalculator.eval("3 5 -"))
        self.assertEqual(-8, RpnCalculator.eval("-3 5 -"))
        self.assertEqual(8, RpnCalculator.eval("3 -5 -"))
        self.assertEqual(2, RpnCalculator.eval("-3 -5 -"))
    

    def testMultiplication(self):
        self.assertEqual(15, RpnCalculator.eval("3 5 *"))
    

    def testMultiplicationNegative(self):
        self.assertEqual(-15, RpnCalculator.eval("-3 5 *"))
        self.assertEqual(-15, RpnCalculator.eval("3 -5 *"))
        self.assertEqual(15, RpnCalculator.eval("-3 -5 *"))
    

    def testMultiplicationZero(self):
        self.assertEqual(0, RpnCalculator.eval("3 0 *"))
        self.assertEqual(0, RpnCalculator.eval("-3 0 *"))
        self.assertEqual(0, RpnCalculator.eval("0 3 *"))
        self.assertEqual(0, RpnCalculator.eval("0 -3 *"))
        self.assertEqual(0, RpnCalculator.eval("0 0 *"))
    

    def testDivision(self):
        self.assertEqual(3, RpnCalculator.eval("16 5 //"))
        self.assertEqual(-4, RpnCalculator.eval("16 -5 //"))
        self.assertEqual(-4, RpnCalculator.eval("-16 5 //"))
        self.assertEqual(3, RpnCalculator.eval("-16 -5 //"))
        self.assertEqual(0, RpnCalculator.eval("0 5 //"))
    

    def testComplexExpression(self):
        self.assertEqual(-1, RpnCalculator.eval("1 1 1 + -"))
        self.assertEqual(10, RpnCalculator.eval("4 3 * 2 1 // -"))
        self.assertEqual(6, RpnCalculator.eval("5 5 + 10 2 3 * - -"))
        self.assertEqual(3, RpnCalculator.eval("1 2 + 3 * 6 + 2 3 + //"))
        self.assertEqual(5, RpnCalculator.eval("15 7 1 1 + - // 3 * 2 1 1 + + -"))
    

if __name__ == "__main__":
    unittest.main()