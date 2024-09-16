# Если не указывать режим открытия, файл открывается для чтения текста. При этом
# в качестве кодировки по умолчанию используется кодировка ОС. И если с режимом
# чтения понятно, то с кодировкой могут быть проблемы. Вот так выглядит “Привет,
# мир!”, сохранённый в utf-8, но открытый в cp1251 - РџСЂРёРІРµС‚, РјРёСЂ!
# Чтобы избежать проблем при работе с файлами рекомендуется при открытии
# указывать как минимум три параметра: название файла, режим и кодировк

f = open('text_data.txt', 'r', encoding='utf-8')
print(f)
print(list(f))

# Важно! Кодировка UTF-8 является современным стандартом для
# хранения и передачи текстовой информации. Если вы явно не планируете
# работать с другой кодировкой, всегда указывайте encoding='utf-8' при открытии
# текстовых файлов. Это обеспечит переносимость вашего кода между
# различными платформами.
