# Задание 1
from sys import argv

a, b, c = map(int, argv[1:])  # a - выработка, b - ставка, с - премия
res = (a * b) + c

print(res)

# Задание 2
li = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
reslist = [li[i] for i in range(len(li)) if li[i] > li[i - 1] and i != 0]
print(reslist)

# Задание 3
reslist = [i for i in range(22, 241) if i % 20 == 0 or i % 21 == 0]
print(reslist)

# Задание 4
li = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
reslist = [el for el in li if li.count(el) == 1]

print(reslist)

# Задание 5
from functools import reduce

li1 = [n for n in range(100, 1001) if n % 2 == 0]
res = reduce(lambda x, y: x * y, li1)
print(res)

# Задача 6

# Скрипт 1
from sys import argv
from itertools import count

n = int(argv[1])
new = (i for i in count(start=n, step=1) if i < 11)
for i in new:
    print(i)

# Скрипт 2
from itertools import cycle

li = [1, 15, 24, 35, 42, 0, 100, 38, 5]
i = 0

for num in cycle(li):
    i += 1
    if i > 10:
        break
    else:
        print(num)


# Задача 7
def fact(n):
    from functools import reduce

    li = [i for i in range(1, n + 1)]
    res = reduce(lambda x, y: x * y, li)
    yield res


for el in fact(4):
    print(el)
