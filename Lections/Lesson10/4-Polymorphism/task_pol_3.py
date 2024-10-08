class DivStr(str):
    def __init__(self, obj):
        self.obj = str(obj)

    def __truediv__(self, other):
        first = self.obj.endswith('/')
        start = self.obj

        if isinstance(other, str):
            second = other.startswith('/')
            finish = other
        elif isinstance(other, DivStr):
            second = other.obj.startswith('/')
            finish = other.obj
        else:
            second = str(other).startswith('/')
            finish = str(other)

        if first and second:
            return DivStr(start[:-1] + finish)
        if (first and not second) or (not first and second):
            return DivStr(start + finish)
        if not first and not second:
            return DivStr(start + '/' + finish)


path_1 = DivStr('/home/user/')
path_2 = DivStr('/my_project/workdir')
result = path_1 / path_2
print(f'{result = }, {type(result)}')
print(f'{result / "text" = }')
print(f'{result / 42 = }')
print(f'{result * 3 = }')

# Создаём класс DivStr как наследник класса str. При инициализации определяем
# аргумент obj, который является обычной строкой. Вся магия деления строк будет
# спрятана в магическом методе __truediv__ который срабатывает при делении
# экземпляра класса DivStr на другой такой же экземпляр или на обычную строку str:
# 1. Первым делом определяем заканчивается ли первая часть на символ /, а саму
# строку сохраняем в переменной start.
# 2. Далее проверяем начинается ли на символ / и сохраняем вторую половинку в
# finish
# a. Если вторая половинка строка, работаем с объектом other как со
# строкой.
# b. Если вторая половинка экземпляр класса DivStr, работаем со свойством
# obj.
# c. Если оба варианта неверны, пробуем привести объект к строковому
# виду.
# 3. В зависимости от того заканчивается или нет первая часть на символ / и
# начинается или нет вторая часть на символ / соединяем объекты и
# возвращаем новый экземпляр DivStr.
