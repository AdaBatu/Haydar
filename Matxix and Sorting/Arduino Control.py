import pyfirmata
import time
from tkinter import *
import tkinter
import serial

lal = []
listof1 = []
listof2 = []
final = []
final1 = []
final2 = []
bab = 'sa'
ser = serial.Serial(port="COM3", baudrate=9600)
time.sleep(4)
ser.write(bab.encode('ascii'))
for p in range(10):  #576
    b = ser.readline().decode('ascii')
    raw = b[:-2].strip()
    unraw = raw[2:]
    if b[0] == "1":
        listof1.append(unraw)
    else:
        listof2.append(unraw)
print(listof1, listof2)
listof1.sort()
print(listof1)
listof2.sort()
print(listof2)
for ka1 in listof1:
    final1.append(int(ka1.split(" ")[1]))
for ka2 in listof2:
    final2.append(int(ka2.split(" ")[1]))
print(final1, final2)
for fin in range(len(final1)):
    if final1[fin] == 0:
        final.append(final2[fin])
    else:
        if final2[fin] != 0:
            final.append(final1[fin]/2+final2[fin]/2)
        if final2[fin] == 0:
            final.append(int(0))
print(final)



