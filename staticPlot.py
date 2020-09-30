from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv')

x = data['x_value']
p1 = data['pressure_1']
p2 = data['pressure_2']
p3 = data['pressure_3']

plt.plot(x, p1, label="Pressure Sensor 1")
plt.plot(x, p2, label="Pressure Sensor 2")
plt.plot(x, p3, label="Pressure Sensor 3")

plt.legend(loc='upper left')
plt.xlabel('Time')
plt.ylabel('Pressure')
plt.tight_layout()

plt.title('Pressure x Time')

plt.show()
