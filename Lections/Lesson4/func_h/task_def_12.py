# Позиционные и ключевые параметры
# Пришло время поговорить о позиционных и ключевых параметрах функции. Начнём
# с общего синтаксиса.
# def func(positional_only_parameters, /, positional_or_keyword_parameters, *,
#     keyword_only_parameters):
#     pass
# При указании параметров функции вначале идут позиционные параметры. При
# вызове функции передаются значения без указания имени переменной-аргумента.
# Косая черта не является переменной. Это символ разделитель. После неё могут
# 12
# идти как позиционные, так и ключевые параметры. Далее символ разделитель
# звёздочка указывает только на ключевые параметры.
# 🔥 Важно! Косая черта и звёздочка одновременно или по отдельности
# могут отсутствовать при определении функции
# Разберем передачу аргументов по позиции и по имени на примерах

def func(positional_only_parameters, /, positional_or_keyword_parameters, *,
    keyword_only_parameters):
    pass

def standard_arg(arg):
    print(arg) # Принтим для примера, а не для привычки


standard_arg(42)
standard_arg(arg=42)