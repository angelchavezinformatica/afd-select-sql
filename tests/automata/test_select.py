import unittest

from automata.errors import IdentifierIsAReservedWord, InvalidIdentifier
from automata.select import SelectAutomata


class SelectTest(unittest.TestCase):

    def test_select1(self):
        query = 'SELECT * FROM table;'
        SelectAutomata(query, 0)

    def test_select2(self):
        query = 'SELECT identificador FROM table;'
        SelectAutomata(query, 0)

    def test_select3(self):
        query = 'SELECT identifier, other_identifier FROM table;'
        SelectAutomata(query, 0)

    def test_invalid_select1(self):
        query = 'SELECT FROM table;'

        with self.assertRaises(IdentifierIsAReservedWord):
            SelectAutomata(query, 0).test()

    def test_invalid_select2(self):
        query = 'SELECT identifier FROM;'

        with self.assertRaises(InvalidIdentifier):
            SelectAutomata(query, 0).test()
