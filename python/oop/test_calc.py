#can be from calc import add
#import calc (whole module)
from calc import *
import unittest

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        #the below line of code, checks whether the parameter in the add function is equal to 15, if true, it passes with a ., if not an F is displayed 
        self.assertEqual(add(10,5), 15)
        
if __name__ == "__main__":
    unittest.main()