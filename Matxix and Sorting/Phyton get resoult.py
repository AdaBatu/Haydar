import serial
import time

ser = serial.Serial('COM3', 9600)
data = []                       # empty list to store the data
while 1:
    b = ser.readline().decode('ascii')
    garr = int(''.join(filter(str.isdigit, b)))
    if int(garr) < 500:
        print(b)
    time.sleep(0.001)
ser.close()

