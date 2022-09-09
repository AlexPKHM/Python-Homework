# Задание 1
def division(n1, n2):
    if n2 == 0:
        print('Division by 0 is prohibited by Law')
    else:
        res = n1 / n2
        print(f'{n1} divided by {n2} equals {res}')


n1 = int(input('Please input a dividend: '))
n2 = int(input('Please input a divisor: '))

division(n1, n2)


# Задание 2
def datainpt(name='uname', surname='usname', city='ucity', email='uemail', phone='uphone'):
    print(f'Hi {name} {surname} from {city}. Your email is {email} and phone is {phone}')


name = input('Please input your Name: ')
surname = input('Please input your Surname: ')
city = input('Please input your city: ')
email = input('Please input your email: ')
phone = input('Please input your phone: ')

datainpt(name, surname, city, email, phone)


# Задание 3
def my_func(a, b, c):
    if a < c < b or a < b < c:
        res = c + b
        print(f'The result of {c}+{b} equals {res}')
    elif b < c < a or b < a < c:
        res = c + a
        print(f'The result of {c}+{a} equals {res}')
    elif c < a < b or c < b < a:
        res = a + b
        print(f'The result of {a}+{b} equals {res}')


a = int(input('Please input an integer: '))
b = int(input('Please input a second integer: '))
c = int(input('Please input a third integer: '))

my_func(a, b, c)


# Задание 4
def my_func(x, y):
    res = x ** y
    print(res)


my_func(5, -3)


# or by using for loop

def my_func2(x, y):
    ypos = -y
    xpwr = 1

    for n in range(ypos):
        xpwr = xpwr * x
    res = 1 / xpwr
    print(res)


my_func2(5, -3)


# Задание 5
def usum():
    res = 0
    while True:
        li = input('Input a string of numbers separated by spaces, or input "q" to stop: ').split()
        for n in li:
            if n == 'q':
                print(res)
                print('Thank you for your input i guess')
                return
            else:
                n = int(n)
                res = res + n
        print(res)


usum()


# Задание 6
def int_func():
    while True:
        intwrd = input('Input a word in lowercase or "stop" to exit: ')
        if intwrd == 'stop':
            print('Thank you for your input i guess')
            return
        else:
            wrd = intwrd.capitalize()
            print(wrd)

    wrd = intwrd.capitalize()
    print(wrd)


int_func()


# Задание 7
def int_func():
    li = []
    intli = input('Input words in lowercase: ').split()
    for wrd in intli:
        wrd = wrd.capitalize()
        li.append(wrd)
        strli = ' '.join(li)
    print(strli)
    


int_func()
