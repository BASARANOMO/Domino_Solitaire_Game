"""
@Author: ZHANG Mofan
"""
from exception import *


class Domino:
    def __init__(self, nbr_left, nbr_right):
        # domino value should be of int type between 0 and 6
        # if not, raise exception
        type_left, type_right = type(nbr_left), type(nbr_right)
        if (type_left is not int) or (type_right is not int):
            raise InvalidDominoTypeException(type_left, type_right)

        if (nbr_left < 0 or nbr_left > 6) or (nbr_right < 0 or nbr_right > 6):
            raise InvalidDominoValueException(nbr_left, nbr_right)

        self._left, self._right = nbr_left, nbr_right
        self._point = self._left + self._right

    def __repr__(self):
        num_tuple = (self._left, self._right)
        return f"Domino{num_tuple}"

    def __str__(self):
        domino_str = "+-----|-----+\n"

        str_list = [' '*5, ' '*5, '*    ', '    *', '*   *', '*   *', '* * *', '* * *']
        int_couple = (self._left, self._right)

        num_str_list = []
        for num in int_couple:
            if (num & 1) == 0:  # even number
                num_str = [str_list[num], ' '*5, str_list[num+1]]
            else:  # odd number
                num_str = [str_list[num-1], '  *  ', str_list[num]]
            num_str_list.append(num_str)  # num_str is element of num_str_list

        # add elements in num_str_list to domino_str
        for i in range(3):
            domino_str += "|{}|{}|\n".format(num_str_list[0][i], num_str_list[1][i])

        domino_str += "+-----|-----+"
        return domino_str

    def read_left(self):
        return self._left

    def read_right(self):
        return self._right

    def read_point(self):
        return self._point

    def __eq__(self, other):
        if self._point == other.read_point():
            if self._left == other.read_left() or self._left == other.read_right():
                return True
        return False

    def __ne__(self, other):
        if self._point != other.read_point():
            return True
        else:
            if self._left != other.read_left() and self._left != other.read_right():
                return True
        return False


"""
try:
    Domino('f', 'g')
except InvalidDominoTypeException as e:
    print(e.__str__())
try:
    Domino(0.5, 5)
except InvalidDominoTypeException as e:
    print(e.__str__())
try:
    Domino(7, -3)
except InvalidDominoValueException as e:
    print(e.__str__())
try:
    Domino(-1, 0)
except InvalidDominoValueException as e:
    print(e.__str__())
try:
    Domino(6, 11)
except InvalidDominoValueException as e:
    print(e.__str__())
"""
