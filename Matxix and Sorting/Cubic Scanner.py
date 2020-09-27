import serial
import time
import matplotlib.pyplot as plt
import math
from sympy import symbols, Eq, solve, sqrt, cos
from mpl_toolkits.mplot3d import Axes3D
k = int
m = int
x = int
y = int
old_dist = int
r = int
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
        r = int(''.join(filter(str.isdigit, b)))
        if r < 500:
            if baban:
                k = r
                old_dist = r
                baban = 0
            else:
                print(b)
                o = math.sqrt((r ** 2) + (old_dist ** 2) - (2 * old_dist * r * cos(12)))
                x, y, k, m, o, r = symbols('x y k m o r')
                eq1 = Eq((sqrt(o**2 - x**2 + 2*x*k - k**2) + m), y)
                eq2 = Eq((sqrt(r**2 - 202500 + 900*x - x**2) + 450), y)
                sncu_dict = solve((eq1, eq2), x, y)
                print(sncu_dict)
                print(x, y)
                k, m = x, y
                old_dist = r
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
