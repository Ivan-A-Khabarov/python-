# Приватная переменная __max_up не исчезает за пределами класса. Срабатывает
# механизм модификации имени. В общем случае он превращает переменную
# __name в переменныю _classname__name.

class Person:
    __max_up = 3
    _max_level = 80

    def __init__(self, name, race='unknown', speed=100):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100
        self._speed = speed
        self.up = 3

    def _check_level(self):
        return self.level < self._max_level

    def level_up(self):
        if self._check_level():
            self.level += 1

    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity

    def add_up(self):
        self.up += 1
        self.up = min(self.up, self.__max_up)


p1 = Person('Сильвана', 'Эльф', 120)
print(f'{p1.up = }')
p1.up = 1
print(f'{p1.up = }')
for _ in range(5):
    p1.add_up()
    print(f'{p1.up = }')


# В нашем примере переменная __max_up превратилась в _Person__max_up.
# Обратите внимание на заглавную P в имени, ведь Python является
# регистрозависимым языком.
# Важно! У вас должны быть особые обстоятельства чтобы обращаться и тем более
# изменять значения переменных, которые начинаются с двух подчёркиваний за
# пределами их класса. Скорее всего есть другой способ решить вашу задачу.
