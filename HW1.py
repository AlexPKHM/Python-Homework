# Задание 1
name = 'Alexandr'
age = 24
print('My name is', name, 'and I am', age, 'years old.')

uname = input('Enter your name: ')
uage = input('Enter your age: ')
print(f'Your name is {uname} and you are {uage} years old.')

# Задание 2
stime = int(input('Please input time in seconds: '))
hour = stime // (60 * 60)
min = (stime - (hour * 3600)) // 60
sec = stime - ((hour * 3600) + (min * 60))
print(f'{stime} seconds in hh:mm:ss format is {hour}:{min}:{sec}')

# Задание 3
num = str(input('Please input a number: '))
n = int(num)
nn = int(num * 2)
nnn = int(num * 3)
res = (n + nn + nnn)

print(f'{n}+{nn}+{nnn}={res}')

# Задание 4
unum = int(input('Please input a number: '))

if unum < 10:
    print(unum)
else:
    while True:
        lst = unum % 10
        unum = unum // 10
        if unum > lst and unum < 10:
            print(unum)
            break
        elif unum > lst and unum > 10:
            lst2 = unum % 10
            unum = unum // 10
            if unum > lst2 and unum < 10:
                print(unum)
                break
            elif unum < lst2 and lst2 > lst:
                print(lst2)
                break
            elif unum < lst2 and lst2 < lst:
                print(lst)
                break
        else:
            print(lst)
            break

# Задание 5 и 6
profit = int(input('Пожалуйста, введте размер прибыли организации: '))
expense = int(input('Пожалуйста, введте размер издержек организации: '))

if profit > expense:
    print('Выручка привышает издержки')
    ros = (profit / expense) * 100
    print(f'Рентабильность выручки составляет {ros}%')
    empln = int(input('Введите колличество сотрудников организации: '))
    empprf = profit / empln
    print(f'Прибыль на одного сотрудника составляет: {empprf}')
else:
    print ('Выручка не привышает издержек')