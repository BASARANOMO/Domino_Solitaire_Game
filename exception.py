class InvalidDominoTypeException(Exception):
    def __init__(self, left, right):
        super().__init__()
        self._left = left
        self._right = right
    def __str__(self):
        return f"Invalid domino type {self.get_value()}"
    def get_value(self):
        return (self._left, self._right)


class InvalidDominoValueException(Exception):
    def __init__(self, val, pos):
        super().__init__()
        self._val = val
        self._pos = pos
    def __str__(self):
        return f"Invalid half domino value {self.get_value()} at {self.get_pos()}"
    def get_value(self):
        return self._val
    def get_pos(self):
        return self._pos

class NonNumericalInputException(Exception):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return "The input value is not numerical or can not be converted to numerical!"
