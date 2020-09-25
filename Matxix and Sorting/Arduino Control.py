import pyfirmata
import time

board = pyfirmata.Arduino('COM3')

it = pyfirmata.util.Iterator(board)
it.start()

triger = board.get_pin('d:10:o')
echo = board.get_pin('d:8:i')
time23 = 0
sarrah = input("Bitsin mi?")
while True:
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
    print(distance)
    time.sleep(0.02)
    if sarrah == "evet":
        break
