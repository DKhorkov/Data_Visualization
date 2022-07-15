import matplotlib.pyplot as plt


numbers = range(1, 6)
sequence_of_numbers_square = [num ** 2 for num in numbers]  # Создание квадратов чисел из заданного списка.

print(plt.style.available)  # Просмотр встроенных стилей для использования при построении графика.
plt.style.use('classic')  # Выбор стиля для графика (должен быть выбран ДО построения самого графика).
fig, ax = plt.subplots()  # "fig" - весь рисунок, на котором будут диаграммы. "ax" - диаграмма, на рисунке "fig".

# Создадим красные точки, чтобы было визуально понятнее, где находится квадрат числа.
# "s" - size, "c" - color (0 - темно, 1 - светло), "edgecolor"- цве контура вокруг точек.
ax.scatter(numbers, sequence_of_numbers_square, s=200, c=(0.7, 0.9, 0), edgecolor="red")

# Построение графика на основе входных данных. Первый аргумент - значения на оси ОХ, второй - ОУ:
ax.plot(numbers, sequence_of_numbers_square, linewidth=5)  # "linewidth" - толщина линии.
ax.set_title('Squares of numbers', fontsize=24)  # Установка названия графика + выбор размера шрифта.
ax.set_xlabel('Values', fontsize=14)  # Установка названия оси ОХ с размером 14.
ax.set_ylabel('Squares', fontsize=14)  # Установка названия оси OY с размером 14.
ax.tick_params(axis='both', labelsize=9)  # Установка обеим осям размера шрифта делений (цифр на оси).
ax.axis([0, 6, 0, 36])  # Метод для установки диапазона каждой оси (первые два значения для оси ОХ, вторые два для ОУ).


name_of_graph = input("Введите название графика для сохранения: ")
place_for_save = f'pictures_of_graphs/{name_of_graph}.png'
# plt.show()  # Вывод визуальной информации в окне просмотра. Можно либо вывести на экран, либо сохранить график в файле.
plt.savefig(place_for_save, bbox_inches='tight')
