from automata import constants as c
from .errors import InvalidIdentifier, IdentifierIsAReservedWord


class IdentifierAutomata:

    def __init__(self, full_string: str, index: int) -> None:
        self.full_string = full_string
        self.index = index

    def run(self):
        state = 0
        word = ''

        while True:
            try:
                char = self.full_string[self.index]
            except IndexError as e:
                raise InvalidIdentifier() from e

            if (state == 0 or state == 1) and char in c.CHARS:
                state = 1
            elif char in (c.SPACE, c.COMMA, c.SEMICOLON):
                break
            else:
                raise InvalidIdentifier()

            word += char
            if len(self.full_string) - 1 == self.index:
                break

            self.index += 1

        if word in c.RESERVED:
            raise IdentifierIsAReservedWord()
