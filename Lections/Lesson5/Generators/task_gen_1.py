a = range(0, 10, 2)
print(f'{a = }, {type(a)=},{a.__sizeof__()=},{len(a)=}')
b = range(-1_000_000, 1_000_000, 2)
print(f'{b = }, {type(b)=},{b.__sizeof__()=},{len(b)=}')

# Генератор "a" на пять значений и генератор b на 1 млн. Значений занимают
# одинаковое место в память.