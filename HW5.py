# Задача 1
with open(r'hw5_tasks/task1.txt', 'w', encoding="utf-8") as f:
    while True:
        ustr = input('Please input a string of data: ')
        if ustr != "":
            ustr += "\n"
            f.write(ustr)
        else:
            break

# Задача 2
with open(r'hw5_tasks/task2.txt', 'r', encoding="utf-8") as f:
    lines = len(f.readlines())
    f.seek(0)
    chr_w_spcs = len(f.read())
    f.seek(0)
    chr_wo_spcs = len(f.read().replace(" ", ""))
    print(f'The file contains {lines} lines as well as {chr_w_spcs} characters or {chr_wo_spcs} characters if counted '
          f'w/o spaces.')

# Задача 3
with open(r'hw5_tasks/task3.txt', 'r', encoding="utf-8") as f:
    org_dict = {}
    low_sal = []
    comp = 0
    for line in f:
        wrkr, salary = line.split()
        org_dict[wrkr] = float(salary)
        if float(salary) < 20000.00:
            low_sal.append(wrkr)

    avg = sum(org_dict.values()) // len(org_dict)

print(f'The following workers have salaries lover than 20k: {low_sal}')
print(f'The average salary in org is: {avg} rub')

# Задача 4
num_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
file_dict = {}

with open(r'hw5_tasks/task4-1.txt', 'r', encoding="utf-8") as f:
    for line in f:
        num_l, num = line.split(' — ')
        file_dict[num_l] = num.strip("\n")
    res_dict = file_dict
    if file_dict.keys() == num_dict.keys():
        res_dict = dict(zip(list(num_dict.values()), list(file_dict.values())))
with open(r'hw5_tasks/task4-2.txt', 'w', encoding="utf-8") as f2:
    for a, b in res_dict.items():
        f2.write(f'{a} — {b} \n')

# Задача 5
import random
randomlist = str(random.sample(range(1, 51), 5))
randomlist = randomlist.strip("[]").replace(",", "")
# print(randomlist)

with open(r'hw5_tasks/task5.txt', 'w', encoding="utf-8") as f:
    f.write(randomlist)

with open(r'hw5_tasks/task5.txt', 'r', encoding="utf-8") as f2:
    total = 0
    list = list(map(int, (f2.readline()).split()))
    print(list)
    for el in range(0, len(list)):
        total = total + list[el]

print(total)
