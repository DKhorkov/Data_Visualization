# Визуализация бросков кубика с помощью Plotly
from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline


class Dice:
    """Класс игрального кубика."""

    def __init__(self, num_sides=6):
        """Атрибуты кубика. ПО умолчанию у кубика 6 граней."""
        self.sides = num_sides

    def roll(self):
        """Симуляция броска кубика."""
        return randint(1, self.sides)


d6 = Dice()
results = []
for roll in range(1_000):
    result = d6.roll()
    results.append(result)

# Проанализируем частоту выпадения граней кубика:
frequency = {}
for value in range(1, d6.sides + 1):
    frqns = results.count(value)
    frequency[value] = frqns

frequency_list = [v for v in frequency.values()]  # Нужен список, а не словарь, для функции "offline.plot", иначе error.
# Визуализация результатов:
x_values = list(range(1, d6.sides + 1))  # Значения по оси ОХ.
data = [Bar(x=x_values, y=frequency_list)]  # Создание данных для визуализации по оси ОХ и ОУ.
x_axis_config = {'title': 'Side of dice'}
y_axis_config = {'title': 'Frequency of result'}
my_layout = Layout(title='Results of rolling dice with 6 sides 1 thousand times',
                   xaxis=x_axis_config, yaxis=y_axis_config, )  # Создание макета данных для визуализации.
offline.plot({'data': data, 'layout': my_layout}, filename='pictures_of_graphs/d6.html')


