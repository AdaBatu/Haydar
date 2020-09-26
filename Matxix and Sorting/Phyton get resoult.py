import serial
import time

ser = serial.Serial('COM3', 9600)
data = []                       # empty list to store the data
for i in range(10):
    b = ser.readline()         # read a byte string
    string_n = b.decode()  # decode byte string into Unicode
    string = string_n.rstrip()  # remove \n and \r
    flt = float(string)        # convert string to float
    print(flt)
    data.append(flt)           # add to the end of data list
    time.sleep(0.001)            # wait (sleep) 0.1 seconds
ser.close()
for line in data:
    print(line)
