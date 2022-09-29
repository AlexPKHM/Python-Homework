# Задание 1
class Matrix:
    def __init__(self, li):
        self.li = li

    def __str__(self):
        res = ''
        for row in self.li:
            res += f'{" ".join([str(l) for l in row])}\n'
        return res

    def __add__(self, other):
        if len(self.li[0]) == len(other.li[0]):
            rows_count = len(self.li)
            items_count = len(self.li[0])

            new_matrix = [[] for _ in range(len(self.li))]
            for i in range(rows_count):
                for j in range(items_count):
                    new_matrix[i].append(self.li[i][j] + other.li[i][j])
            return Matrix(new_matrix)
        else:
            print("Error - Matrix of different sizes cannot be added")


a = Matrix([
    [11, 12, 2],
    [14, 15, 5],
])

b = Matrix([
    [21, 22, 23],
    [24, 25, 26],
])

print(a)
print(b)

print(a+b)

# Задание 2
from abc import ABC, abstractmethod

li = []


class clothing_abs(ABC):
    @abstractmethod
    def cloth(self):
        pass


class coat(clothing_abs):
    def __init__(self):
        self.res = None

    @property
    def s(self):
        return self.__size

    @s.setter
    def s(self, size):
        self.__size = size

    def cloth(self):
        res = self.__size / 6.5 + 0.5
        print(f'The coat requires {res} meters of cloth')
        self.res = res
        return self.res


class suit(clothing_abs):
    def __init__(self):
        self.res = None

    @property
    def h(self):
        return self.__height

    @h.setter
    def h(self, height):
        self.__height = height

    def cloth(self):
        res = 2 * self.__height + 0.3
        print(f'The suit requires {res} meters of cloth')
        self.res = res
        return self.res


class Cloth:
    def __init__(self, li):
        self.li = li

    def total(self):
        res = sum(self.li)
        print(f'All products require {res} meters of cloth')


coat1 = coat()
coat1.s = 52
coat1.cloth()
li.append(coat1.res)

suit1 = suit()
suit1.h = 1.8
suit1.cloth()
li.append(suit1.res)

total_cloth = Cloth(li)
total_cloth.total()

# Задание 3
class Cell:

    def __init__(self, count: int):
        assert count > 0, "Количество ячеек должно быть больше 0"
        self.__count = count

    def __add__(self, other: 'Cell'):
        self.validate_item(other)
        value = self.count + other.count
        return Cell(value)

    def __sub__(self, other: 'Cell'):
        self.validate_item(other)
        value = self.count - other.count
        assert value > 0, "Разность ячеек меньше 0"
        return Cell(value)

    def __mul__(self, other: 'Cell'):
        self.validate_item(other)
        value = self.count * other.count
        return Cell(value)

    def __truediv__(self, other: 'Cell'):
        self.validate_item(other)
        value = round(self.count / self.count)
        return Cell(value)

    def __str__(self):
        return str(self.__count)

    def validate_item(self, other):
        assert isinstance(other, self.__class__), "Операции допустимы только между клетками"

    @property
    def count(self) -> int:
        return self.__count

    @staticmethod
    def make_order(cell_object: 'Cell', count_per_row: int) -> str:
        items = '*' * cell_object.count
        chunks = [
            items[i:i + count_per_row]
            for i in range(0, len(items), count_per_row)
        ]

        return '\n'.join(chunks)


first = Cell(3)
second = Cell(2)
huge = Cell(12)

print(first + second)
print(first - second)
print(first * second)
print(first / second)

print(Cell.make_order(huge, 5))
