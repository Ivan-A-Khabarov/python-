# ● Запись CSV
# Для записи данных в файл используют функцию writer, которая возвращает объект
# конвертирующий данные в формат CSV. Функция writer принимает файловый
# дескриптор и дополнительные параметры записи аналогичные параметрам
# функции reader. При этом данные в файл не записываются пока у возвращённого
# объекта не будет вызван метод writerow для записи одной строки или writerows для
# записи нескольких строк.
# Рассмотри на примере.


import csv
with (
    open('biostats_tab.csv', 'r', newline='') as f_read,
    open('new_biostats.csv', 'w', newline='', encoding='utf-8') as f_write
    ):
    csv_read = csv.reader(f_read, dialect='excel-tab',quoting=csv.QUOTE_NONNUMERIC)
    csv_write = csv.writer(f_write, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    all_data = []
    for i, line in enumerate(csv_read):
        if i == 0:
            csv_write.writerow(line)
        else:
            line[2] += 1
            for j in range(2, 4 + 1):
                line[j] = int(line[j])
            all_data.append(line)
    csv_write.writerows(all_data)