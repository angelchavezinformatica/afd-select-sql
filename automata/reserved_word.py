from .errors import InvalidReservedWord


class ReservedWordAutomata:
    def __init__(self, full_string: str, index: int) -> None:
        self.full_string = full_string
        self.index = index

    def test(self, reserved_word: str):
        state = 0

        while True:
            char = self.full_string[self.index]

            if len(self.full_string) - 1 == self.index or len(reserved_word) - 1 == state:
                break

            if char != reserved_word[state]:
                raise InvalidReservedWord()

            self.index += 1
            state += 1
