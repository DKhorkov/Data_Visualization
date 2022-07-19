# Визуализация данных CSV формата.
import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'data/sitka_jul_2018.csv'
with open(filename) as f:
    reader = csv.reader(f)  # Создание объекта чтения данных.
    header_row = next(reader)  # Первая строка из файла.

    for index, column_header in enumerate(header_row):  # Индекс элемента списка + его значение.
        print(index, column_header)

    # Программа продолжает чтение файла дальше. Заголовок прочитан ранее, поэтому продолжение со 2 ряда.
    dates, highs = [], []
    for row in reader:
        high = int(row[5])
        highs.append(high)
        date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(date)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='blue')
fig.autofmt_xdate()  # Вывод даты на диаграмму по диагонали для лучшей визуализации.
ax.set_title('Daily high temperatures, July 2018')
ax.set_xlabel('Day of the month', fontsize=12)
ax.set_ylabel('Temperature (F)', fontsize=12)
ax.tick_params(axis='both', labelsize=10)

plt.show()
