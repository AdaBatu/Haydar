import serial
import time
import matplotlib.pyplot as plt
import math
from sympy import symbols, Eq, solve, sqrt, cos
import multiprocessing
from mpl_toolkits.mplot3d import Axes3D
old_x = int
old_y = int
new_x = int
new_y = int
old_dist = int
new_dist = int
zline = []
xline = []
yline = []
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


def multiprocess(r, k, m, old_dist1):
    o = math.sqrt((r ** 2) + (old_dist1 ** 2) - (2 * old_dist1 * r * cos(12)))
    x, y, k, m, o, r = symbols('x y k m o r')
    multiprocessing.pool
    eq1 = Eq((sqrt(o ** 2 - x ** 2 + 2 * x * k - k ** 2) + m), y)
    eq2 = Eq((sqrt(r ** 2 - 202500 + 900 * x - x ** 2) + 450), y)
    sncu_dict = solve((eq1, eq2), x, y)
    return sncu_dict

def addpoints(dicto):
    xlin = dicto[0]
    ylin = dicto[1]
    zlin = dicto[2]
    return xline.append(xlin), yline.append(ylin), zline.append(zlin)


while 1:
    baban = 1
    starttime = time.time()
    for h in range(360):
        b = ser.readline().decode('ascii')
        new_dist = int(''.join(filter(str.isdigit, b)))
        if new_dist < 500:
            if baban:
                old_x = new_dist
                old_dist = new_dist
                baban = 0
                xline.append(new_dist)
                yline.append(first_y)
                zline.append(0)
            else:
                print(b)
        else:
            baban = 1

        time.sleep(0.021 + ((1/3)/1000))
    print('That took {} seconds'.format(time.time() - starttime))
    ax.scatter(xline, yline, zline, 'gray')
    ax.view_init(60, 35)
    plt.show()
ser.close()
