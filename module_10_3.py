import threading
import time
import random

class Bank:
    def __init__(self):
        self.balance = 0  # начальный баланс
        self.lock = threading.Lock()  #для блокировки потоков

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500) # рандомная сумма пополнения
            self.balance += amount
            print(f'Пополнение: {amount}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():# Если баланс 500 или больше и замок заблокирован, разблокируем его
                self.lock.release()
            time.sleep(0.001)  # пауза

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500) # рандомная сумма пополнения
            print(f'Запрос на {amount}')

            if amount <= self.balance:
                self.balance -= amount
                print(f'Снятие: {amount}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()  # блокируем поток
            time.sleep(0.001)  # пауза

bk = Bank()

th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

th1.start()
th2.start()

th1.join()
th2.join()

# Выводим итоговый баланс
print(f'Итоговый баланс: {bk.balance}')
