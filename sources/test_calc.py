import unittest
import calc

class TestCalc(unittest.TestCase):
    """
    Test the add function from the calc library
    """

    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = calc.add2(1, 2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = calc.add2('10.5', 2)
        self.assertEqual(result, 12.5)

    def test_add_strings(self):
        """
        Test the addition of two strings returns the two strings as one
        concatenated string
        """
        result = calc.add2('abc', 'def')
        self.assertEqual(result, 'abcdef')

    def test_add_string_and_integer(self):
        """
        Test the addition of a string and an integer returns them as one
        concatenated string (in which the integer is converted to a string)
        """
        result = calc.add2('abc', 3)
        self.assertEqual(result, 'abc3')

    def test_add_string_and_number(self):
        """
        Test the addition of a string and a float returns them as one
        concatenated string (in which the float is converted to a string)
        """
        result = calc.add2('abc', '5.5')
        self.assertEqual(result, 'abc5.5')
        
  #Add 4
    def test_add4_integers(self):
        """
        Test that the addition of four integers returns the correct total
        """
        result = calc.add4(1, 2, 3, 4)
        self.assertEqual(result, 10)

    def test_add4_floats(self):
        """
        Test that the addition of four floats returns the correct result
        """
        result = calc.add4('10.5', 2, 5, '2.5')
        self.assertEqual(result, 20.0)

    def test_add4_strings(self):
        """
        Test the addition of four strings returns the two strings as one
        concatenated string
        """
        result = calc.add4('abc', 'def', 'ghi', 'jkl')
        self.assertEqual(result, 'abcdefghijkl')

    def test_add4_string_and_integer(self):
        """
        Test the addition of a string and an integer returns them as one
        concatenated string (in which the integer is converted to a string)
        """
        result = calc.add4('abc', 3, 'def', 4)
        self.assertEqual(result, 'abc3def4')

    def test_add4_string_and_number(self):
        """
        Test the addition of a string and a float returns them as one
        concatenated string (in which the float is converted to a string)
        """
        result = calc.add4('abc', '5.5', 'def', '2.5' )
        self.assertEqual(result, 'abc5.5def2.5')

if __name__ == '__main__':
    unittest.main()
