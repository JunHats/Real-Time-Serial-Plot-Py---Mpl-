import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


plt.style.use('fivethirtyeight')


def animate(i):
    data = pd.read_csv('data.csv')
    plt.xlabel('Pressure')
    plt.ylabel('Time')
    x = data['x_value']
    p1 = data['pressure_1']
    p2 = data['pressure_2']
    p3 = data['pressure_3']

    plt.cla()

    plt.plot(x, p1, label="Pressure Sensor 1")
    plt.plot(x, p2, label="Pressure Sensor 2")
    plt.plot(x, p3, label="Pressure Sensor 3")

    plt.legend(loc='upper left')
    plt.tight_layout()


anmt = FuncAnimation(plt.gcf(), animate, interval=20)

plt.tight_layout()
plt.show()
