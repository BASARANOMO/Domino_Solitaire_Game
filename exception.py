class InvalidDominoTypeException(Exception):
    def __init__(self, type_left, type_right):
        super().__init__()
        self._type_left = type_left
        self._type_right = type_right
    def __str__(self):
        type_tuple = self.get_type()
        err_str = ""
        pos = ['left', 'right']
        for i in range(2):
            if type_tuple[i] is not int:
                err_str += f"Invalid domino type {type_tuple[i]} at {pos[i]}\n"
        return err_str
    def get_type(self):
        return (self._type_left, self._type_right)


class InvalidDominoValueException(Exception):
    def __init__(self, val_left, val_right):
        super().__init__()
        self._val_left = val_left
        self._val_right = val_right
    def __str__(self):
        val_tuple = self.get_value()
        err_str = ""
        pos = ['left', 'right']
        for i in range(2):
            if (val_tuple[i] < 0 or val_tuple[i] > 6):
                err_str += f"Invalid half domino value {val_tuple[i]} at {pos[i]}\n"
        return err_str
    def get_value(self):
        return (self._val_left, self._val_right)


class InvalidHandIndexException(Exception):
    def __init__(self, invalid_idx_list):
        super().__init__()
        self._invalid_idx_list = invalid_idx_list
    def __str__(self):
        idx_list_len = self.get_len()
        if idx_list_len == 1:
            return f"The index {self.get_idx_list()[0]} is out of range!"
        else:
            invalid_idx_str = ", ".join([str(elem) for elem in self.get_idx_list()])
            return f"The indices {invalid_idx_str} are out of range!"
    def get_idx_list(self):
        return self._invalid_idx_list
    def get_len(self):
        return len(self.get_idx_list())

class DuplicateIndexException(Exception):
    def __init__(self, duplicate_idx_list):
        super().__init__()
        self._duplicate_idx_list = duplicate_idx_list
    def __str__(self):
        idx_list_len = self.get_len()
        if idx_list_len == 1:
            return f"The index {self.get_idx_list()[0]} is duplicated!"
        else:
            duplicate_idx_str = ", ".join([str(elem) for elem in self.get_idx_list()])
            return f"The indices {duplicate_idx_str} are duplicated!"
    def get_idx_list(self):
        return self._duplicate_idx_list
    def get_len(self):
        return len(self.get_idx_list())

class PointsNotTwelveException(Exception):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return f"Total points different from 12."
