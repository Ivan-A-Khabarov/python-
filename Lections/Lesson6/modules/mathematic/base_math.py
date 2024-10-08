# В зависимости от решаемой задачи некоторые пункты могут отсутствовать.
# Учебный пример модуля ниже:
# Файл base_math.py

"""Four basic mathematical operations.
Addition, subtraction, multiplication and division as functions.
"""
_START_SUM = 0
_START_MULT = 1
_BEGINNING = 0
_CONTINUATION = 1


def add(*args):
    res = _START_SUM
    for item in args:
        res += item
    return res

def sub(*args):
   res = args[_BEGINNING]
   for item in args[_CONTINUATION:]:
       res -= item
   return res

def mul(*args):
    res = _START_MULT
    for item in args:
        res *= item
    return res

def div(*args):
    res = args[_BEGINNING]
    for item in args[_CONTINUATION:]:
        res /= item
    return res

if __name__ == '__main__':
    print(f'{add(2, 4) = }')
    print(f'{add(2, 4, 6, 8) = }')
    print(f'{sub(10, 2) = }')
    print(f'{mul(2, 2, 2, 2, 2) = }')
    print(f'{div(-100, 5, -2) = }')


# Как вы заметили, в файле нет классов, только функции. Так же нам не
# понадобились переменные уровня модуля. Тесты мы не стали писать, т.к. не
# добрались до темы тестирования. Осталось добавить main код.

# if __name__ == '__main__':
#   print(f'{add(2, 4) = }')
# ...
# После определения функций, но перед вызовом print добавили логическую
# проверку. Строки с print после проверки и до конца файла сдвинули на 4 пробела,
# поместили внутрь блока проверки.
# Магическая переменная __name__ содержит полное имя модуля. Это имя
# используется для уникальной идентификации модуля в системе импорта.
# Когда мы запускаем сам модуль base_math, в переменную __name__ попадает имя
# “__main__”. Оно указывает, что файл запущен, а не импортирован. Никакой
# разницы в работе модуля не произошло.
# Когда модуль импортируется в другой файл, в переменную __name__ попадает его
# имя, название файла без расширения. import base_math также выполняет код в
# файле. Присваиваются значения константам, инициализируются функции. Но
# логическая проверка if __name__ == '__main__': возвращает ложь и дальнейший
# код пропускается.
# Отличной. Добавление “мейн” проверки позволило завершить создание модуля.
# Теперь запуск main.py работает так, как мы ожидаем.
