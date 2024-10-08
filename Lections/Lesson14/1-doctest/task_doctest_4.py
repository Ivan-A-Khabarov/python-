# ➢ Запуск всех тестов: убедиться, что новые тесты не проходят
# Запускаем файл с кодом даже не включая режим отображения verbose. И получаем
# огромный список ошибок заканчивающийся следующим итогом:
# *****************************************************************
# *****
# 1 items had failures:
# 5 of 7 in __main__.is_prime
# ***Test Failed*** 5 failures.
# Логично провалить 5 новых тестов, ведь мы пока не писали код, который позволит
# их пройти.

# 🔥 Важно! Так как doctest сравнивает текст, вызов ошибки, например через
# raise и печать аналогичного текста через print() будут восприниматься
# одинаково.

def is_prime(p: int) -> bool:
    """
    Проверяет число P на простоту путем поиска остатка от деления в диапазоне [2, P).

    >>> is_prime(42)
    False
    >>> is_prime(73)
    True
    >>> is_prime(3.14)
    Traceback (most recent call last):
        ...
    TypeError: Число P должно быть целого типа
    >>> is_prime(-100)
    Traceback (most recent call last):
        ...
    ValueError: Число P должно быть больше 1
    >>> is_prime(1)
    Traceback (most recent call last):
        ...
    ValueError: Число P должно быть больше 1
    >>> is_prime(100_000_001)
    Если число P является простым, проверка может занять много времени.
    Работает...
    False
    >>> is_prime(100_000_007)
    Если число P является простым, проверка может занять много времени.
    Работает...
    True
    """
    if not isinstance(p, int):
        raise TypeError('Число P должно быть целого типа')
    elif p <= 1 or p < 0:
        raise ValueError('Число P должно быть больше 1')
    elif p > 100_000_000:
        print('Если число P является простым, проверка может занять много времени. Работаем...')
        for i in range(2, p):
            # Проверка делимости на все числа от 2 до p-1
            if p % i == 0:
                return False
        return True


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)