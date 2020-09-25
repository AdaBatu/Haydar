import pyfirmata
import time
from tkinter import *
import tkinter

board = pyfirmata.Arduino('COM3')

it = pyfirmata.util.Iterator(board)
it.start()
pencere = tkinter.Tk()
pencere.title("sonuçlar:")
liste34 = Listbox(pencere)
triger = board.get_pin('d:10:o')
echo = board.get_pin('d:8:i')
time23 = 0
orta = 1
sarrah = input("Bitsin mi?")
bacı = 1
if sarrah != "evet":
    while bacı:
        triger.write(0)
        time.sleep(0.002)
        triger.write(1)
        time.sleep(0.01)
        triger.write(0)
        time23 = 0
        while echo.read(1):
            time23 += 1
            time.sleep(0.001)
        else:
            break
        distance = time23 * 0.034 / 2
        liste34.insert(orta, distance)
        orta += 1
        time.sleep(0.02)
else:
    bacı = 0
liste34.mainloop()
