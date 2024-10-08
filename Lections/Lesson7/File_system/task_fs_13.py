# ● Копирование файлов
# Для копирования файлов лучше всего подходит модуль shutil, который
# предоставляет ряд высокоуровневых операций

import shutil

shutil.copy('one.txt', 'dir')
shutil.copy2('two.txt', 'dir')


# Функции copy и copy2 работают схожим образом. Они принимают файл для
# копирования и целевой каталог. Если такого каталога не существует, функция
# попытается присвоить копируемому файлу имя “цели”.
# Отличие состоит в том, что функция copy2 помимо содержимого файла пытается
# скопировать и связанные с ним метаданные.
