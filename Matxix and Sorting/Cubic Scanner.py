import serial
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from multiprocessing import Process, Manager
import threading
import numpy as np
import math

zline = []
xline = []
yline = []
fig = plt.figure()
X_Grid = [0, 900]
Y_Grid = [0, 900]
Z_Grid = [0, 900]
ax = plt.axes(projection='3d')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3D Projection')


def sayılr(neulist):
    ser = serial.Serial(port="COM3", baudrate=9600)
    for p in range(72 * 3):
        b = ser.readline().decode('ascii')
        newest_dist = int(''.join(filter(str.isdigit, b)))
        time.sleep(0.0042)
        neulist.append(newest_dist), print(b)
    ser.close()


def multiprocess2(r, k, m, n, old_dist1, multi1, multi2, ileri, faz):
    p = math.sin(math.radians(ileri)) * r
    o = int(round(p * p))
    t = math.sqrt(abs((r ^ 2) - o))
    x_dif = old_dist1 - t
    y_dif = p
    x = multi1 * abs(x_dif) + k
    y = multi2 * abs(y_dif) + m
    z = 450
    if faz == 0:
        sncu_dict = [x, y, z]
    else:
        zmif = abs(int(round(math.sin(math.radians(faz)) * r))) + 450
        zdif = abs(n - zmif)
        xmif = math.sqrt(abs((zdif ^ 2) - o))
        ymif = math.sqrt(abs((zdif ^ 2) - int(round(x_dif * x_dif))))
        x = multi1 * abs(xmif) + k
        y = multi2 * abs(ymif) + m
        z = zmif
        sncu_dict = [x, y, z]
    return sncu_dict


def addpoints(dicto):
    xlin = dicto[0]
    ylin = dicto[1]
    zlin = dicto[2]
    return xline.append(xlin), yline.append(ylin), zline.append(zlin)


def main1(ooora, colist1):
    anan = 0
    old_x = int
    old_y = 0
    old_z = 450
    new_x = 0
    new_y = 0
    new_z = 450
    old_dist = 0
    ilerleyis = 10
    yukarı_ieri = 5
    multiplyer1 = 0
    multiplyer2 = 0
    first_y = 450
    phase = 0
    up_phase = 0
    baban = 1
    for ko in range(3):
        starttime = time.time()
        for h in range(72):
            if phase > 348:
                phase -= 360
            try:
                new_dist = int(ooora[0])
            except IndexError:
                time.sleep(1)
                new_dist = int(ooora[0])
            del ooora[0]
            if new_dist < 500:
                if anan:
                    hhug = abs((math.sin(up_phase) * new_dist))
                    new_z = 450 + hhug
                    new_x = old_x - (math.sqrt(abs((new_dist ^ 2) - int(round(hhug * hhug)))))
                    new_y = old_y
                    old_x = new_x
                    old_y = new_y
                    old_dist = new_dist
                    bakko = [new_x, new_y, new_z]
                    addpoints(bakko)
                    baban = 0
                else:
                    if baban:
                        old_x = (450 + new_dist)
                        old_y = first_y
                        old_dist = new_dist
                        baban = 0
                        yline.append(first_y)
                        xline.append(new_dist + 450)
                        zline.append(new_z)
                    else:
                        if phase != 90 or 180 or 270 or 0:
                            if phase < 90:
                                multiplyer1 = -1
                                multiplyer2 = 1
                            if 180 > phase > 90:
                                multiplyer1 = -1
                                multiplyer2 = -1
                            if 180 < phase < 270:
                                multiplyer1 = 1
                                multiplyer2 = -1
                            if phase > 270:
                                multiplyer1 = 1
                                multiplyer2 = 1
                            dis_dict = multiprocess2(new_dist, old_x, old_y, old_z, old_dist, multiplyer1, multiplyer2,
                                                     phase, up_phase)
                            print(new_dist, old_x, old_y, old_dist, dis_dict)
                        else:
                            if phase == 90:
                                new_x = 450
                                new_y = new_dist + 450
                                new_z = 450 + abs((math.sin(math.radians(up_phase)) * new_dist))
                            if phase == 180:
                                new_x = 450 - new_dist
                                new_y = 450
                                new_z = 450 + abs((math.sin(math.radians(up_phase)) * new_dist))
                            if phase == 270:
                                new_x = 450
                                new_y = -new_dist + 450
                                new_z = 450 + abs((math.sin(math.radians(up_phase)) * new_dist))
                            if phase == 0:
                                new_x = new_dist + 450
                                new_y = 450
                                new_z = 450 + abs((math.sin(math.radians(up_phase)) * new_dist))
                            dis_dict = [new_x, new_y, new_z]
                        addpoints(dis_dict)
                        colist1 = dis_dict
                        old_dist = new_dist
                        dis_dict.clear()
            else:
                print("bozuk veri")
            phase += ilerleyis
            anan = 0
        up_phase += yukarı_ieri
        anan = 1
    print('That took {} seconds'.format(time.time() - starttime))


if __name__ == '__main__':
    with Manager() as manager:
        neulist = Manager().list()
        colist = Manager().list()
        p1 = Process(target=sayılr, args=(neulist, ))
        p2 = Process(target=main1, args=(neulist, colist))
        p3 = Process(target=multiprocess2, args=(colist, ))
        p1.start()
        time.sleep(5)
        p2.start()
    while p1.is_alive() or p2.is_alive():
        time.sleep(5)
    else:
        ax.scatter(xline, yline, zline, c=np.linalg.norm([xline, yline, zline], axis=0))
        ax.plot_trisurf(np.array(xline), np.array(yline), np.array(zline))
        ax.view_init(60, 35)
        plt.show()
