# Визуализация бросков двух кубиков.
from plotly.graph_objs import Bar, Layout
from plotly import offline

from dice_roll import Dice

dice1 = Dice()
dice2 = Dice()

results = []
for roll in range(1000):
    result = dice1.roll() + dice2.roll()
    results.append(result)

frequencies = []
for value in range(2, dice1.sides + dice2.sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(2, dice1.sides + dice2.sides + 1))
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
data = [Bar(x=x_values, y=frequencies)]
my_layout = Layout(title='Results of roll double D6 dices 1 thousand times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='pictures_of_graphs/double_d6.html')
