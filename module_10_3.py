import threading
import time
from random import randint

class Bank():
    def __init__(self):
        self.lock = threading.Lock()
        self.balance = 0

    def deposit(self):
        for _ in range(100):
            self.replenishment = randint(50, 500)
            self.balance += self.replenishment
            print(f'Пополнение: {self.replenishment}. Баланс:{self.balance}')
            if self.balance >= 500:
                if self.lock.locked():
                    self.lock.release()
                    print(f'\nБаланс > 500, счёт разблокирован для снятия денежных средств!')
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            self.request = randint(50, 100)
            print(f'\nЗапрос на снятие {self.request} при балансе = {self.balance}\n')
            if self.balance - self.request  > 500:
                self.balance -= self.request
                print(f'\nСнятие: {self.request}. Баланс: {self.balance}')
                time.sleep(0.001)
            else:
                print(f'Баланс < 500 недостаточно средств для снятия по условиям договора!\n')
                self.lock.acquire()
                time.sleep(0.001)

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
print()
th1.join()
th2.join()

print('Итоговый баланс: ', bk.balance)
