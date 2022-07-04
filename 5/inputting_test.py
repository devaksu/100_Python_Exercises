from unittest import TestCase, mock
from inputting import Inputoutputstring

strObj = Inputoutputstring()

class InputoutputTest(TestCase):
    @mock.patch('inputting.input', create=True)
    def TestgetString(self, mocked_input):
        mocked_input.side_effect = 'Tämä lause'
        lause = strObj.printString()
        return self.assertEqual(lause, 'TÄMÄ LAUSE')


     