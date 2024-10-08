# ● Обход папок через os.walk()
# Функция os.walk рекурсивно обходит каталоги от переданного в качестве аргумента
# до самого нижнего уровня вложенности.

import os

for dir_path, dir_name, file_name in os.walk(os.getcwd()):
    print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')

# Функция возвращает кортеж из трёх значений:
# ➢ dir_path — абсолютный путь до каталога
# ➢ dir_names — список с названиями всех каталогов, находящихся в dir_path
# ➢ dir_names — список с названиями всех файлов, находящихся в dir_path
# Вывод продолжается до тех пор пока не будет возвращена информация обо всех
# директориях, т.е. каждая директория из dir_names передаётся в os.walk и
# оказывается в dir_path.
