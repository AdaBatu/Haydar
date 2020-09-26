import pyfirmata
import time
from tkinter import *
import tkinter

board = pyfirmata.Arduino('COM3')
it = pyfirmata.util.Iterator(board)
it.start()
triger = board.get_pin('d:10:o')
echo = board.get_pin('d:8:i')
orta = 1
bacı = 1

while bacı == 1:
    triger.write(0)
    time.sleep(0.002)
    triger.write(1)
    time.sleep(0.01)
    triger.write(0)
    time23 = 0
    if echo.read():
        while echo.read() == 0:
            time23 += 1
        else:
            distance = time23 * 0.034 / 2
            print(distance)
            orta += 1
            time.sleep(0.02)
else:
    print(distance)



