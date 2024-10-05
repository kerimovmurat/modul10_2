from threading import Thread
import time

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0
        self.enemies = 100

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemies > 0:
            self.days += 1
            time.sleep(1) # 1 день сражения (1 секунда задержка)
            self.enemies -= self.power # количество врагов уменьшается на power текущего рыцаря
            if self.enemies < 0:
                self.enemies = 0
            print(f'{self.name} сражается {self.days}, осталось {self.enemies} воинов.')
        print(f'{self.name} одержал победу спустя {self.days} день(дней) ')
# Рыцари :
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)
# Запускаем потоки
first_knight.start()
second_knight.start()
# Ожидание завершения всех битв
first_knight.join()
second_knight.join()

print('Все битвы закончились! ')
