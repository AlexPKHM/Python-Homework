# Задача 1
class Date:
    def __init__(self, date_str):
        n = Date.from_str(date_str)
        self.is_valid_date(n)
        self.day, self.month, self.year = n
        print(f'{self.day}-{self.month}-{self.year}')

    @classmethod
    def from_str(cls, date_str) -> list:
        date_li = date_str.split('-')
        day, month, year = map(int, date_li)
        list = day, month, year
        return list

    @staticmethod
    def is_valid_date(n: list):
        d, m, y = n

        assert 1 <= d <= 31, "Incorrect date format"
        assert 1 <= m <= 12, "Incorrect month format"
        assert 1970 <= y <= 2100, "Incorrect year format"


date1 = Date('19-12-2001')
date1 = Date('32-13-2100')  #Err Test

# Задание 2
class DivByZero(Exception):
    def __init__(self, msg):
        self.mas = msg


div1 = int(input('Please input a dividend: '))
div2 = int(input('Please input a divisor: '))

try:
    if div2 == 0:
        raise DivByZero('Division by Zero is not possible')
except (ValueError, DivByZero) as err:
    print(err)
else:
    res = div1 // div2
    print(res)
finally:
    print("End")

# Задача 3
class NonIntValue(Exception):
    def __init__(self, msg):
        self.msg = msg


user_inpt = 0
li = []

while user_inpt != 'End':
    user_inpt = input('Please enter a value to add to the list or enter "End" to stop: ')

    try:
        if int(user_inpt) == ValueError:
            raise NonIntValue('The value has non Int type')
    except (ValueError, NonIntValue) as err:
        print('The value has non Int type')
        y_or_n = input(f'Would you like to continue? Y/N ')
        if y_or_n == 'Y' or y_or_n == 'y':
            continue
        elif y_or_n == 'N' or y_or_n == 'n':
            print(f'End')
        break
    else:
        val = int(user_inpt)
        li.append(val)

print(f'The resulting list is folowint: {li}')

# Задачи 4-6
class Storage:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)


class Equipment:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.make} {self.year}'


class Printer(Equipment):
    def __init__(self, series, name, make, year):
        super().__init__(name, make, year)
        self.series = series

    def __repr__(self):
        return f'{self.name} {self.series} {self.make} {self.year}'

    def action(self):
        return 'Печатает'


class Scaner(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'Scans'


class Xerox(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'Copies'


storage = Storage()
# creating objects and adding them to storage
scaner = Scaner('hp', '321', 90)
storage.add_to(scaner)
scaner = Scaner('hp', '311', 97)
storage.add_to(scaner)
scaner = Scaner('hp', '330', 99)
storage.add_to(scaner)
printer = Printer('e-320', 'sony', 126, 2018)
storage.add_to(printer)
# print storage
print(storage._dict)
# extracting an obj from the storage and printing storage
storage.extract('Scaner')
print()
print(storage._dict)

# Задача 7
class ComplexNumber:
    real: float
    indeterminate: float

    def __init__(self, real: float, indeterminate: float):
        self.real = real
        self.indeterminate = indeterminate

    def __add__(self, other: 'ComplexNumber'):
        return ComplexNumber(
            self.real + other.real,
            self.indeterminate + other.indeterminate
        )

    def __mul__(self, other: 'ComplexNumber'):
        r1 = self.real * other.real
        r2 = self.indeterminate * other.indeterminate * -1

        i1 = self.real * other.indeterminate
        i2 = self.indeterminate * other.real

        real = r1 + r2
        indeterminate = i1 + i2

        return ComplexNumber(real, indeterminate)

    def __str__(self):
        return f"({self.real}{'+' if self.indeterminate > 0 else ''}{self.indeterminate}i)"


a = ComplexNumber(4, 55)
b = ComplexNumber(6, 22)

# (4+55i) + (6+22i) = (4 + 6) + (55 + 22)i = (10+77i)
print(a + b)

# (4+55i) * (6+22i) = (4 * 6) + (4 * 22i) + (55 * 6i) + (55 * 22i^2) = 24 + 88i + 330i - 1210 = (-1186+418i)
print(a * b)