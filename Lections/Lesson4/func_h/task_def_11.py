# Если в качестве значения по умолчанию нужен изменяемый тип данных,
# используют особый приём с None

def from_one_to_n(n, data=None):
    if data is None:
        data = []
    for i in range(1, n + 1):
        data.append(i)
    return data

new_list = from_one_to_n(5)
print(f'{new_list = }')
other_list = from_one_to_n(new_list)
print(f'{other_list = }')

# Если изменяемый объект не передан, он создаётся по новой для каждого вызова
# функции.
