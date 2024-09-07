# map(function, iterable) — принимает на вход функцию и последовательность.
# Функция применяется к каждому элементу последовательности и возвращает map
# итератор.


"""map(function, iterable)"""
text = ["Привет", "ЗДОРОВА", "привеТствую"]
res = map(lambda x: x.lower(), text)
print(*res) # ['привет', 'здорова', 'приветствую']

# В качестве функции использовали лямбду для вызова метода lower у каждого из
# переданных объектов. Объект итератор res был распакован в функцию print через
# символ “звёздочка”.
