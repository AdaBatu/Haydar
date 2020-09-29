import serial
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

old_x = 0
old_y = 0
new_x = 0
new_y = 0
old_dist = 0
new_dist = 0
ilerleyis = 12
multiplyer1 = 0
multiplyer2 = 0
zline = []
xline = []
yline = []
first_y = 450
new_z = 450
ser = serial.Serial('COM3', 9600)
X_Grid = [0, 900]
Y_Grid = [0, 900]
Z_Grid = [0, 900]
phase = 0
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3D Projection')


def multiprocess2(r, k, m, old_dist1, multi1, multi2):
    o = math.sqrt((r ** 2) + (old_dist1 ** 2) - (2 * old_dist1 * r * math.cos(ilerleyis)))
    x = (r ** 2 - o ** 2 - multi1 * m ** 2 + multi2 * k ** 2) / (2 * k - 900)
    y = math.sqrt(o ** 2 - x ** 2 + 2 * x * k - k ** 2 + m ** 2)
    z = 450
    sncu_dict = [x, y, z]
    return sncu_dict


def addpoints(dicto):
    xlin = dicto[0]
    ylin = dicto[1]
    zlin = dicto[2]
    return xline.append(xlin), yline.append(ylin), zline.append(zlin)


while 1:
    baban = 1
    starttime = time.time()
    for h in range(5):
        if phase > 348:
            phase -= 360
        try:
            b = ser.readline().decode('ascii')
        except:
            b = ser.readline().decode('ascii')
        new_dist = int(''.join(filter(str.isdigit, b)))
        if new_dist < 500:
            if baban:
                old_x = (450 + new_dist)
                old_y = first_y
                old_dist = new_dist
                baban = 0
                yline.append(first_y)
                xline.append(new_dist + 450)
                zline.append(new_z)
            else:
                print(b)
                if phase != 90 or 180 or 270:
                    if phase < 90:
                        multiplyer1 = 1
                        multiplyer2 = 1
                    if 180 > phase > 90:
                        multiplyer1 = -1
                        multiplyer2 = 1
                    if 180 < phase < 270:
                        multiplyer1 = -1
                        multiplyer2 = -1
                    if phase > 270:
                        multiplyer1 = 1
                        multiplyer2 = -1
                    dis_dict = multiprocess2(new_dist, old_x, old_y, old_dist, multiplyer1, multiplyer2)
                    print(new_dist, old_x, old_y, old_dist, dis_dict)
                else:
                    if phase == 90:
                        new_x = 450
                        new_y = new_dist + 450
                        dis_dict = [new_x, new_y, new_z]
                    if phase == 180:
                        new_y = 450
                        new_x = new_dist + 450
                        dis_dict = [new_x, new_y, new_z]
                    if phase == 270:
                        new_x = 450
                        new_y = -new_dist + 450
                        dis_dict = [new_x, new_y, new_z]
                addpoints(dis_dict)
                old_x = dis_dict[0]
                old_y = dis_dict[1]
                old_dist = new_dist
                dis_dict.clear()
        else:
            baban = 1
        phase += ilerleyis
        time.sleep(0.021 + ((1 / 3) / 1000))
    print('That took {} seconds'.format(time.time() - starttime))
    ax.scatter(xline, yline, zline, c=np.linalg.norm([xline, yline, zline], axis=0))
    ax.plot_trisurf(np.array(xline), np.array(yline), np.array(zline))
    ax.view_init(60, 35)
    plt.show()
ser.close()
