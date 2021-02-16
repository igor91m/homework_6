'''
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
и завершать скрипт.
'''

import time


class TrafficLight:
    __color = 'Красный' # приватный __атрибут класса

    def running(self): # собственный метод класса
        print('Светофор работает')

        self.__color = 'Красный'
        print(f'Установлен цвет: {self.__color}')
        time.sleep(7)

        self.__color = 'Желтый'
        print(f'Установлен цвет: {self.__color}')
        time.sleep(2)

        self.__color = 'Зеленый'
        print(f'Установлен цвет: {self.__color}')
        time.sleep(7) # время для равного значения с красным цветом светофора

        while True:
            self.running()

traff_light = TrafficLight()
print(traff_light.running())

'''
from time import sleep
from datetime import datetime as dt

class TrafficLight:
    states = {'red': 7, 'yellow': 2, 'green': 10}
    _color = ''

    def running(self):
        for color, e_time in self.states.items():
        self._color = color
        start_state_time = dt.now()
        print(f" Светофор '{self._color}' " f" светит {e_time} секунд")
        sleep(e_time)
        print(f" Светофор '{self._color}' проверка светил " f"{(dt.now() - start_state_time).seconds} секунд")
            if __name_ == 'main':
            r = TrafficLight()
            r.running()
'''