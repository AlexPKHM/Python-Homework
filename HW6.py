# Задача 1
class TrafficLight:
    __color = ["Red", "Yellow", "Green"]

    def running(self, __color=__color):
        import time
        for el in __color:
            if el == "Red":
                print(f'{el} is ON')
                time.sleep(7)
            elif el == "Yellow":
                print(f'{el} is ON')
                time.sleep(2)
            elif el == "Green":
                print(f'{el} is ON')
                time.sleep(5)


trafficlight = TrafficLight()
trafficlight.running()

# Задача 2
class Road:

    def __init__(self, _length, _width):
        mass = 25
        thickness = 5
        res = _length * _width * mass * thickness
        print(f'{res} kg')


Road(20, 5000)

# Задача 3
class Worker:
    name = "Ivan"
    surname = "Ivanov"
    position = "Junior Developer"
    _income = {"wage": 50000, "bonus": 15000}


class Position(Worker):
    def get_full_name(self):
        name = Worker.name
        surname = Worker.surname
        print(f'Full name is {name} {surname}')

    def get_total_income(self):
        wage = Worker._income["wage"]
        bonus = Worker._income["bonus"]
        income = wage + bonus
        print(f'Total income is {income}')

pos = Position()
pos.get_full_name()
pos.get_total_income()

# Задача 4
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Car goes')

    def stop(self):
        print(f'Car stops')

    def turn(self, direction):
        print(f'Car turns {direction}')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Your speed is {self.speed}, you are Speeding!')
        else:
            print(f'{self.speed}')


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Your speed is {self.speed}, you are Speeding!')
        else:
            print(f'{self.speed}')


class SportsCar(Car):

    def show_speed(self):
        print(f'{self.speed}')



class PoliceCar(Car):
    is_police = True

    def show_speed(self):
        print(f'{self.speed}')

    def police(self):
        print(f'{PoliceCar.is_police}')


towncar = TownCar(70, "green", "Mercedes")
print(towncar.name)
print(towncar.color)
towncar.go()
towncar.turn("left")
towncar.stop()
towncar.show_speed()

print("-" * 5)

sportscar = SportsCar(100, "Red", "Ferarri")
print(sportscar.name)
print(sportscar.color)
sportscar.go()
sportscar.turn("right")
sportscar.stop()
sportscar.show_speed()

print("-" * 5)

policecar = PoliceCar(70, "White and Blue", "Ford")
print(policecar.name)
print(policecar.color)
policecar.go()
policecar.turn("back")
policecar.stop()
policecar.show_speed()
policecar.police()

# Задание 5
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск Отрисовки')


class Pen(Stationery):

    def draw(self):
        print(f'Запуск Отрисовки Ручкой {self.title}')


class Pencil(Stationery):

    def draw(self):
        print(f'Запуск Отрисовки Карандашом {self.title}')


class Handle(Stationery):

    def draw(self):
        print(f'Запуск Отрисовки Маркером {self.title}')


pen = Pen("Parker")
pen.draw()
pencil = Pencil("Koh-i-Noor")
pencil.draw()
handle = Handle("Mazari Lindo")
handle.draw()