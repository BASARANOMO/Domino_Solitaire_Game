"""
@Author: ZHANG Mofan
@Time: 10/05/2020 13:45-15:00

@Author2: XIE Ruiling
@Time: 10/05/2020 13:45-15:00
"""


class Domino:
    def __init__(self, nbr_left, nbr_right):
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
            if (num & 1) == 0: # even number
                num_str = [str_list[num], ' '*5, str_list[num+1]]
            else: # odd number
                num_str = [str_list[num-1], '  *  ', str_list[num]]
            num_str_list.append(num_str) # num_str is element of num_str_list

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
a = Domino(4, 5)
print(a.__repr__())
print(a.__str__())
print(a.__eq__(Domino(5, 4)))
b = a.__repr__()

print(a.__ne__(Domino(6, 3)))
"""
