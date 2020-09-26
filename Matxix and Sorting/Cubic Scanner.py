import serial
import time
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D
tick_wait = ()
rotor_speed = ()
direction = ()
b = ()
ser = serial.Serial('COM3', 9600)
X_Grid = [0, 900]
Y_Grid = [0, 900]
Z_Grid = [0, 900]
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('Select Point')
while 1:
    baban = 0
    for h in range(313):
        b = ser.readline().decode('ascii')
        garr = int(''.join(filter(str.isdigit, b)))
        if garr < 500:
            print(b)
            oma = garr
        else:
            oma = 0
            garr = 0
        o = math.sqrt((garr ** 2) + (oma ** 2) - (2 * oma * garr * math.cos(12)))

        baban = oma
        time.sleep(0.021 + ((1/3)/1000))

    zline = (0, 15, 1000)
    xline = (0, 15, 1000)
    yline = (0, 15, 1000)
    ax.plot3D(xline, yline, zline, 'gray')
    ax.view_init(60, 35)
    plt.show()
    ser.close()
