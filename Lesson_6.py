# import time
# class TrafficLight:
#     __color = ['red', 'yellow', 'green']
#     def running(self):
#         print(f'{TrafficLight.__color[0]} -stop!')
#         time.sleep(7)
#         print(f'{TrafficLight.__color[1]} -wait')
#         time.sleep(2)
#         print(f'{TrafficLight.__color[2]} -Go')
#         time.sleep(10)
#         print('Have a good trip')
# colors = TrafficLight()
# colors.running()

# class Road:
#     def __init__(self,lenght ,width):
#         self._lenght = lenght
#         self._widht = width
#         self.mas = 25
#         self.tl = 5
#     def weight(self):
#         return self._lenght*self._widht*self.mas*self.tl
# road = Road(20, 5000)
# print(road.weight())

# class Worker:
#     def __init__(self, name, surname, position):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": 30000, "bonus": 5000}
#
#
# class Position(Worker):
#     def get_full_name(self):
#         return f'{self.name} {self.surname}'
#
#     def get_total_income(self):
#         return self._income["wage"] + self._income["bonus"]
#
#
# worker = Position('Ivan', 'Ivanov', 'Saler')
# print(worker.get_full_name())
# print(worker.get_total_income())

# class Car:
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#     def go(self):
#         return f'{self.name} goes'
#     def stop(self):
#         return f'{self.name} stop'
#     def turn(self, direction):
#         return f'{self.name}  is turn {direction}'
#     def show_speed(self):
#         return f' speed {self.speed}'
# class TownCar(Car):
#     def show_speed(self):
#         if self.speed > 60:
#             return f'Скорость превышена'
# class SportCar(Car):
#     pass
# class WorkCar(Car):
#     def show_speed(self):
#         if self.speed > 40:
#             return f'Скорость превышена'
# class PoliceCar(Car):
#     pass
#
# car1 = TownCar(70,'red', 'BMW', False)
# car2= SportCar(130,'green', 'lamborgini', False)
# car3= WorkCar(50,'red', 'Ford', False)
# car4= PoliceCar(80,'red', 'Scoda', True)
# print(car1.go())
# print(car1.stop())
# print(car1.turn('left'))
# print(car1.show_speed())
# print(car2.go())
# print(car2.stop())
# print(car2.turn('left'))
# print(car2.show_speed())
# print(car3.go())
# print(car3.stop())
# print(car3.turn('left'))
# print(car3.show_speed())
# print(car4.go())
# print(car4.stop())
# print(car4.turn('left'))
# print(car4.show_speed())

# class Stationery:
#     def __init__(self, title):
#         self.title = title
#     def draw(self):
#         return f'Запуск отрисовки'
# class Pen(Stationery):
#     def draw(self):
#         return f'Рисуем ручкой'
# class Pencil(Stationery):
#     def draw(self):
#         return f'Рисуем карандашом'
# class Handle(Stationery):
#     def draw(self):
#         return f'Рисуем Маркером'
# pen = Pen('Ручка')
# print(pen.draw())
# pencil = Pencil('Карандаш')
# print(pencil.draw())
# handle = Handle('Маркер')
# print(handle.draw())




