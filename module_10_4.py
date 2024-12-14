from queue import Queue
import time
import threading
from random import randint

class Table:
    def __init__(self, number, guest = None):
        self.number = number
        self.guest = guest

class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        t = randint(3, 10)
        time.sleep(t)

class Cafe:
    queue = Queue()
    def __init__(self, *args):
        self.tables = args

    def guest_arrival(self, *guests):
        print('        КАФЕ ОТКРЫТО!\n')
        for i in range(len(guests)):
            for j in range(5):
                if self.tables[j].guest is None:
                    self.tables[j].guest = guests[i].name
                    print(f'{guests[i].name} сел(-а) за стол номер {self.tables[j].number}\n')
                    guests[i].start()
                    #print(threading.enumerate())
                    break
            if not guests[i].is_alive():
                self.queue.put(guests[i])
                print(f'{guests[i].name} встал(-а) в очередь')

    def discuss_guests(self):
        print()
        eater = [guests[i] for i in range(5)]

        while not self.queue.empty():
            for i in range(5):
                if not eater[i].is_alive():
                    print(f'{eater[i].name} покушал(-а) и ушёл(ушла)')
                    self.tables[i].guest = None
                    print(f'Стол номер {self.tables[i].number} свободен')
                    print()
                    eater[i] = self.queue.get()
                    self.tables[i].guest = eater[i].name
                    print(f'{eater[i].name} вышел(-ла) из очереди и сел(-а) за стол номер {self.tables[i].number}')
                    eater[i].start()
                    print(f'{eater[i].name} кушает , в очереди {self.queue.qsize()} посетителей')
                    print()

        etrs = True
        k = 0
        while etrs:
            for i in range(5):
                if not eater[i].is_alive() and self.tables[i].guest != None:
                    k += 1
                    print(f'{eater[i].name} покушал(-а) и ушёл(ушла)')
                    self.tables[i].guest = None
                    print(f'Стол номер {self.tables[i].number} свободен')
                    print()
                    if k == 5:
                        etrs = False
                        break
        print('Последний посетитель кафе ушёл.\n*******************************\n        КАФЕ ЗАКРЫТО!')
        
tables = [Table(number) for number in range(1, 6)]
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()
