import csv
import random
import time

x_value = 0
pressure_1 = 1000
pressure_2 = 1000
pressure_3 = 1000

fieldnames = ["x_value", "pressure_1", "pressure_2", "pressure_3"]


with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()


while True:

    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "x_value": x_value,
            "pressure_1": pressure_1,
            "pressure_2": pressure_2,
            "pressure_3": pressure_3
        }

        csv_writer.writerow(info)
        print(x_value, pressure_1, pressure_2, pressure_3)

        x_value += 1
        pressure_1 += random.randint(-6, 8)
        pressure_2 += random.randint(-6, 8)
        pressure_3 += random.randint(-6, 9)

    time.sleep(1)
