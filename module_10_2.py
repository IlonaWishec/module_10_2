import threading
import time
class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name # str
        self.power = power # int

    def run(self):
        print(f'{self.name}, на нас напали!')
        people = 100
        day = 0
        while people > 0:
            time.sleep(1)
            people -= self.power
            day += 1
            if people < 0:
                people = 0
            print(f'{self.name} сражается {day} день(дня)..., осталось {people} воинов.')
        print(f'{self.name} одержал победу, спустя {day} дней(дня)!')

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
# # Вывод строки об окончании сражения
print('Все битвы закончились!')