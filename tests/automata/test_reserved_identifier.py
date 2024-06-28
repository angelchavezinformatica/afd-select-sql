import unittest

from automata.errors import InvalidReservedWord
from automata.reserved_word import ReservedWordAutomata


class ReservedIdentifierTest(unittest.TestCase):

    def test_reserved_word(self):
        string = 'SELECT * FROM table;'
        index = 0
        rw = ReservedWordAutomata(string, index)
        rw.test(reserved_word='SELECT')
        rw.index = 9
        rw.test(reserved_word='FROM')

    def test_invalid_reserved_word(self):
        string = 'S3LECT * FR0M table;'
        index = 0
        rw = ReservedWordAutomata(string, index)

        with self.assertRaises(InvalidReservedWord):
            rw.test(reserved_word='SELECT')

        rw.index = 9

        with self.assertRaises(InvalidReservedWord):
            rw.test(reserved_word='FROM')
