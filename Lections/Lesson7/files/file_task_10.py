# ● Чтение методом read
# Ещё один вариант чтения файла — метод read().
# read(n=-1) — читает n символов или n байт информации из файла. Если n
# отрицательное или не указана, читает весь файл. Попытка чтения будет даже в том
# случае, когда файл больше оперативной памяти.

with open('text_data.txt', 'r', encoding='utf-8') as f:
    res = f.read()
    print(f'Читаем первый раз\n{res}')
    res = f.read()
    print(f'Читаем второй раз\n{res}')


# Если прочитать файл до конца, повторные попытки чтения не будут вызывать
# ошибку. Метод будет возвращать пустую строку.