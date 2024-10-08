# ● Чтение циклом for
# Вместо метода readline без аргумента можно использовать более короткую запись с
# циклом for

with open('text_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')

# Файл построчно попадает в переменную line. А для того чтобы избавиться от пустых
# строк отключили перенос строки в функции print.
