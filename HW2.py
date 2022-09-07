# Задание 1
ulst = ['Hello', 15, 1.3]
n = len(ulst)

for el in ulst:
    print(f'{el} is {type(ulst[-n])}')
    n = n - 1

# Задание 2
ulst2 = list((input('Input no less than 4 elements: ')))
print(ulst2)

for i in range(0, len(ulst2)):
     if i == 0:
         ulst2[i], ulst2[i+1] = ulst2[i+1], ulst2[i]
     elif i == 2:
         ulst2[i], ulst2[i + 1] = ulst2[i + 1], ulst2[i]
print(ulst2)

# Задание 3
winter = [1,2,12]
spring = [3,4,5]
summer = [6,7,8]
autumn = [9,10,11]

udate = int(input('Please input a number of the month (1-12): '))

for el in winter:
    if el == udate:
        print('winter')
        break
for el in spring:
    if el == udate:
        print('spring')
        break
for el in summer:
    if el == udate:
        print('summer')
        break
for el in autumn:
    if el == udate:
        print('autumn')
        break

#Решение через dict

yeardi = {'winter': [1,2,12], 'spring': [3,4,5], 'summer': [6,7,8], 'autumn': [9,10,11]}
udate = int(input('Please input a number of the month (1-12): '))

for el in yeardi:
    if udate in yeardi[el]:
        print(el)
        break

# Задание 4
ustr = input('Please input words separated by spaces: ').split()

for i, el in enumerate(ustr, 1):
    if len(el) <= 10:
        print(f'{i}.{el}')
    else:
        frstl = el[0:10]
        print(f'{i}.{frstl}')

#Задание 5
rate = [7, 5, 4, 3, 1]
unum = int(input('Please input any non-negative integer: '))

for i in range(len(rate)):
    if rate[i] < unum:
        rate.insert(i, unum)
        break
    elif rate[i] > unum > rate[i + 1]:
        rate.insert(i + 1, unum)
        break
    elif rate[i] == unum:
        rate.insert(i + 1, unum)
        break
print(rate)

# решение через sorted.list
# rate.append(unum)
#
# print(sorted(rate))