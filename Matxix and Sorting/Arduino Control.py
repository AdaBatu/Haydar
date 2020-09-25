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
orta = 1
bacı = 1
def süre(echord):
    time234 = 0
    if echord.read:
        while echord.read():
            time.sleep(0.001)
            time234 += 1
        else:
            return time234


while bacı == 1:
    triger.write(0)
    time.sleep(0.002)
    triger.write(1)
    time.sleep(0.01)
    triger.write(0)
    time23 = 0
    time23 = süre(echo)
    distance = time23 * 0.034 / 2
    liste34.insert(orta, distance)
    print(distance)
    orta += 1
    time.sleep(0.02)
liste34.mainloop()

