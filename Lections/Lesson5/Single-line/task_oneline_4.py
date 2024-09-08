# ● Распаковка коллекции с упаковкой “лишнего”, упаковка со звёздочкой
# Для упаковки может применяться символ “звёздочка” перед именем переменной.
# Такая переменная превратиться в список и соберёт в себя все значения, не
# поместившиеся в остальные переменные.

data = ["один", "два", "три", "четыре", "пять", "шесть", "семь",]
a, b, c, *d = data
print(f'{a=} {b=} {c=} {d=}')

a, b, *c, d = data
print(f'{a=} {b=} {c=} {d=}')

a, *b, c, d = data
print(f'{a=} {b=} {c=} {d=}')

*a, b, c, d = data
print(f'{a=} {b=} {c=} {d=}')

# Элементы коллекции попадают в переменные в зависимости от того, какая из
# переменных отмечена звёздочкой.
# 🔥 Важно! Звёздочкой можно отметить только одну переменную из
# перечня.