import serial
import time
import csv

ser = serial.Serial(port="COM3", baudrate=115200)
ser.flushInput()
fieldnames = ["x_value", "pressure_1", "pressure_2", "pressure_3"]

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()


while True:
    ser_bytes = ser.readline()
    reading = (ser_bytes.decode('utf-8').strip('\r\n').split(','))
    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        x_value = reading[0]
        pressure_1 = reading[1]
        pressure_2 = reading[2]
        pressure_3 = reading[3]

        info = {
            "x_value": x_value,
            "pressure_1": pressure_1,
            "pressure_2": pressure_2,
            "pressure_3": pressure_3
            }

        csv_writer.writerow(info)
        print(x_value, pressure_1, pressure_2, pressure_3)
        time.sleep(0.01)




