import threading
import time
from tkinter import PanedWindow


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.days = 0
    def war(self, name, power):
        warriors = 100
        while warriors:
            time.sleep(1)
            self.days += 1
            warriors -= power
            print(f'{name} сражается {self.days} дней, осталось {warriors} врагов')
    def run(self):
        print(f'{self.name}, на нас напали!')
        self.war(self.name, self.power)
        print(f'    {self.name} одержал победу спустя {self.days} дней(дня)!')
lancelot = Knight('Sir Lancelot', 10)
galahad = Knight('Sir Galahad', 20)
lancelot.start()
galahad.start()
lancelot.join()
galahad.join()
print()
print('ВСЕ БИТВЫ ЗАКОНЧИЛИСЬ!')
