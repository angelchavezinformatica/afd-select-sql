import unittest

from automata.errors import InvalidIdentifier, IdentifierIsAReservedWord
from automata.identifier import IdentifierAutomata


class IdentifierTest(unittest.TestCase):

    def test_string(self):
        string = 'identifier'
        IdentifierAutomata(string, 0).run()

    def test_string_with_space(self):
        string = 'other_identifier '
        IdentifierAutomata(string, 0).run()

    def test_string_with_comma(self):
        string = 'another_identifier,'
        IdentifierAutomata(string, 0).run()

    def test_string_with_ilegal_charater(self):
        string = 'id3ntific4dor'

        with self.assertRaises(InvalidIdentifier):
            IdentifierAutomata(string, 0).run()

    def test_string_is_reserved_word(self):
        string = 'SELECT'

        with self.assertRaises(IdentifierIsAReservedWord):
            IdentifierAutomata(string, 0).run()
