class InvalidIdentifier(Exception):
    """The character is not part of an identifier."""


class InvalidReservedWord(Exception):
    """The reserved word is not defined."""


class IdentifierIsAReservedWord(Exception):
    """The identifier is a reserved word."""
