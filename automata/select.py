from automata import constants as c
from .identifier import IdentifierAutomata
from .reserved_word import ReservedWordAutomata


class SelectAutomata:

    def __init__(self, query: str, index: str) -> None:
        self.query = query
        self.index = index

    def test(self):
        state = 0

        while True:
            if state == 0:
                rw = ReservedWordAutomata(self.query, self.index)
                rw.test(c.SELECT)
                self.index = rw.index
                state = 1
                continue
            elif state == 1 and self.query[self.index] == c.SPACE + c.ASTERISK:
                state = 2
                continue
            elif state == 1:
                self.index += 2
                ida = IdentifierAutomata(self.query, self.index)
                ida.run()
                self.index = ida.index

                if self.query[self.index] != c.COMMA:
                    state = 2
                continue
            elif state == 2:
                self.index += 1
                rw = ReservedWordAutomata(self.query, self.index)
                rw.test(c.FROM)
                self.index = rw.index
                state = 3
                continue
            elif state == 3:
                self.index += 2
                ida = IdentifierAutomata(self.query, self.index)
                ida.run()
                self.index = ida.index
                state = 4
                continue
            elif state == 4 and self.query[self.index]:
                state = 5
                continue
            elif state == 5:
                break

            raise SyntaxError("The SQL syntax is invalid.")

        if state != 5:
            raise SyntaxError("The SQL syntax is invalid.")
