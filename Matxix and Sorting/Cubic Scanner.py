import serial
import time
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D
old_x = int
old_y = int
new_x = int
new_y = int
old_dist = int
new_dist = int
first_y = 0
ser = serial.Serial('COM3', 9600)
X_Grid = [0, 900]
Y_Grid = [0, 900]
Z_Grid = [0, 900]
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3D Projection')
while 1:
    baban = 1
    for h in range(313):
        b = ser.readline().decode('ascii')
        new_dist = int(''.join(filter(str.isdigit, b)))
        if new_dist < 500:
            if baban:
                old_x = new_dist
                old_dist = new_dist
                baban = 0
            else:
                print(b)
                o = math.sqrt((new_dist ** 2) + (old_dist ** 2) - (2 * old_dist * new_dist * math.cos(12)))
                old_dist = new_dist
                new_x, new_y = math.sqrt(o ** 2 - old_y ** 2 + 2 * old_y * new_y - new_y ** 2) + old_x, math.sqrt(o ** 2 - new_x ** 2 + 2 * new_x * old_x - old_x ** 2) + old_y

                old_x, old_y = new_x, new_y
        else:
            baban = 1

        time.sleep(0.021 + ((1/3)/1000))

    zline = (0, 15, 1000)
    xline = (0, 15, 1000)
    yline = (0, 15, 1000)
    ax.plot3D(xline, yline, zline, 'gray')
    ax.view_init(60, 35)
    plt.show()
    ser.close()
