# Случайное блуждание

import matplotlib.pyplot as plt
from random import choice


class RandomWalk:
    """Класс случайного блуждания"""

    def __init__(self, number_of_points=500):
        """Инициализация атрибутов блуждания."""
        self.number_of_points = number_of_points

        # Начало блуждания в начале координат:
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Создание пути рандомного блуждания."""
        while len(self.x_values) < self.number_of_points:
            self.x_direction = choice([-1, 1])
            self.x_distance = choice(range(1, 5))
            self.x_step = self.x_distance * self.x_direction

            self.y_direction = choice([-1, 1])
            self.y_distance = choice(range(1, 5))
            self.y_step = self.y_distance * self.y_direction

            # Следующее значение зависит от последнего значения в списках координат:
            x = self.x_values[-1] + self.x_step
            y = self.y_values[-1] + self.y_step

            self.x_values.append(x)
            self.y_values.append(y)


while True:
    rw = RandomWalk(5_000)
    rw.fill_walk()

    plt.style.use('classic')
    # "figsize" - размер основного окна вывода, "dpi" - кол-во точек на дюйм:
    fig, ax = plt.subplots(figsize=(18, 10), dpi=150)
    points_number = range(rw.number_of_points)
    ax.scatter(rw.x_values, rw.y_values, s=25, c=points_number, cmap=plt.cm.Blues)
    ax.set_title('Random Walking')
    ax.set_xlabel('OX', fontsize=14)
    ax.set_ylabel('OY', fontsize=14)
    ax.tick_params(axis='both', labelsize=9)

    # Выделим первую и последнюю точку
    ax.scatter(0, 0, c='red', s=50)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='yellow', s=50)

    # При необходимости можно убрать с рисунка Оси ОХ и ОУ в коде ниже:
    # ax.get_xaxis().set_visible(False)
    # ax.get_yaxis().set_visible(False)

    plt.show()

    cont = str(input('Do u want to create another random-walk?(y/n): ').lower())
    answers_list = ['y', 'n']
    while cont not in answers_list:
        cont = input('Error! Press "y" to create another random-walk or "n" to stop: ').lower()
    if cont == 'n':
        break
