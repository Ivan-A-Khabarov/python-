# Визуальное тестирование прошло успешно. Импортируем модуль в основной код
# нашего учебного проекта, в файл main.py

from Lections.Lesson6.modules.mathematic import base_math

x = base_math.mul # Плохой приём
y = base_math._START_MULT # Очень плохой приём
z = base_math.sub(73, 42)
print(x(2, 3))
print(y)
print(z)

# Запускаем файл и наблюдаем вывод “принтов” из файла base_math раньше наших
# расчётов в “мейне”. Дело в том, что команда import запускает импортируемый
# модуль. В результате лишние вызовы функций, а следовательно более медленное
# выполнение кода. Для решения проблемы необходимо внести правки в файл
# base_math.py.
