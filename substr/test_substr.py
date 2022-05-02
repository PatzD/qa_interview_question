import unittest
from substr import check_repeat 

class TestRepeat(unittest.TestCase):

    def test_repeat(self):
        self.assertEqual(check_repeat('abcdededa'),['abcde',5])
    
    def test_repeat(self):
        self.assertEqual(check_repeat('abcsvdededa'),['abcsvde',7])

    def test_repeat(self):
        self.assertEqual(check_repeat('abcddededa'),['abcd',4])
    

if __name__ == '__main__':
    unittest.main()