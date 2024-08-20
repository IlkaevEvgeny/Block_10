from threading import Thread
import time

class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        enemies = 100
        days = 0
        print(f"{self.name}, на нас напали!")

        while enemies > 0:
            time.sleep(1) # Пауза в 1 секунду
            days += 1
            enemies -= self.power
            if enemies < 0:
                enemies = 0 # если врагов на день меньше чем сил рыцаря
            print(f" {self.name} сражается {days} день(дня)..., осталось {enemies} воинов.")
        print(f"{self.name} одержал победу спустя {days} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)


first_knight.start()
second_knight.start()


first_knight.join()
second_knight.join()

print("Все битвы закончились!")