import unittest
import inputting

strObj = inputting.Inputoutputstring()

class InputoutputTest(unittest.TestCase):
    
    def test_printString(self):
        lause = strObj.printString("Tämä lause")
        return self.assertEqual(lause, "TÄMÄ LAUSE")

if __name__ == '__main__':
    unittest.main()