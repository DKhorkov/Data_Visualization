# Визуализация минимальных и максимальных температур в Ситке за 2018 год.
import csv

import matplotlib.pyplot as plt
from datetime import datetime


filename = 'data/sitka_2018.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    highs, dates, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f'Missing data for {date}.')
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', linewidth=2, alpha=0.6)  # "alpha" - регулирует уровень прозрачности (0 - прозрачно).
plt.plot(dates, lows, c='blue', linewidth=2, alpha=0.6)
plt.fill_between(dates, lows, highs, facecolor='green', alpha=0.2)  # Заличка между графиками.
plt.title('Sitka 2018 lowest and highest daily temperature', fontsize=20)
plt.ylabel('Temperature (F)', fontsize=20)
fig.autofmt_xdate()
plt.show()
