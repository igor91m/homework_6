'''
4. Реализуйте базовый класс Car. У данного класса должны быть
следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
'''

class Car:
    # атрибуты класса
    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
    '''
    speed = float
    color = str
    name = str
    is_police = bool
    '''
    # методы класса
    def go(self):
        return f'Машина {self.name} движется.'

    def stop(self):
        return f'Машина {self.name} остановилась.'

    def turn(self, direction):
        return f'Машина {self.name} повернула {direction},'
    # Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля:
    def show_speed(self):
        return f'Ваша скорость {self.speed}'
    '''
    def go(self):
        return print('Машина поехала')

    def stop(self):
        return print('Машина остановилась')

    def turn(self, direction):
        return print(f'Машина повернула {direction}')

    def show_speed(self):
        return self.speed
    '''
# дочерние классы основного класса Car: TownCar(Car), SportCar(Car), WorkCar(Car), PoliceCar(Car)
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Вы превысили скорость 60км/ч, сейчас она составляет {self.speed}км/ч.'
        else:
            return f'Скорость {self.name}'

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Вы превысили скорость 60км/ч, сейчас она составляет {self.speed}км/ч.'
        else:
            return f'Скорость {self.name}'

class PoliceCar(Car):
    pass


town = TownCar ('BMW', 80, 'red', False)
print('1: ' + town.go(), town.show_speed(), town.turn('налево'), town.turn('направо'), town.stop())

sport = SportCar('Lexus', 200, 'red', False)
print('2: ' + sport.go(), sport.show_speed(), sport.turn('налево'), sport.stop())

work = WorkCar('Ford', 40, 'orange', False)
print('3: ' + work.go(), str(work.show_speed()), work.turn('направо'), work.stop())

police = PoliceCar('Nissan', 150, 'yellow', True)
print('4: ' + police.go(), work.show_speed(), work.turn('направо'), work.stop())

