import serial
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from multiprocessing import Process, Manager
import numpy as np
import math

axedif = 4
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
file = open("copy.txt", "w")


def sayılr(neulist):
    ser = serial.Serial(port="COM3", baudrate=9600)
    for p in range(72 * axedif):
        b = ser.readline().decode('ascii')
        newest_dist = int(''.join(filter(str.isdigit, b)))
        time.sleep(0.055512)
        neulist.append(newest_dist), print(b)
    ser.close()


def multiprocess2(r, k, m, n, old_dist1, multi1, multi2, ileri, faz):
    p = math.sin(math.radians(ileri)) * r
    o = int(round(p * p))
    cosimux = abs(math.cos(math.radians(ileri)) * r)
    t = math.sqrt(abs((r ^ 2) - o))
    x_dif = abs(old_dist1 - t)
    y_dif = abs(p)
    x = multi1 * abs(cosimux) + 450
    y = multi2 * abs(y_dif) + 450
    z = 450
    if faz == 0:
        sncu_dict = [x, y, z]
    else:
        dif_bdt = math.sqrt(round(((k - x) * (k - x)) + ((m - y) * (m - y))))
        cos_dif = math.cos(math.radians(faz)) * r
        zmif = abs(int(round(math.sin(math.radians(faz)) * r))) + 450
        zdif = abs(450 - zmif)
        balk = abs(math.sin(math.radians(ileri)) * cos_dif)
        bro = math.sqrt(abs((zdif ^ 2) + round(balk * balk)))
        xmif = math.sqrt(round(abs((bro * bro) - (dif_bdt * dif_bdt))))
        bb1 = old_dist1 - xmif
        # ymif = math.sqrt(round(abs((dif_bdt * dif_bdt) - o)))
        # ymif = math.sqrt(abs((zdif ^ 2) - int(round(x_dif * x_dif))))
        if 90 < faz < 270:
            x = multi1 * (xmif + old_dist1) + 450
            y = multi2 * (-1 * balk) + 450
        else:
            x = multi1 * bb1 + 450
            y = multi2 * abs(balk) + 450
        z = zmif
        sncu_dict = [x, y, z]
        print(xmif, balk, multi1, multi2, old_dist1)
    return sncu_dict


def main1(ooora, cx, cy, cz, ccc):
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
    starttime = time.time()
    for ko in range(axedif):
        for h in range(72):
            if phase > 358:
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
                    bakko = [new_x, new_y, new_z]
                    xlin = bakko[0]
                    ylin = bakko[1]
                    zlin = bakko[2]
                    cx.append(xlin), cy.append(ylin), cz.append(zlin)
                    cccok = str(xlin) + ', ' + str(ylin) + ', ' + str(zlin)
                    ccc.append(str(cccok))
                else:
                    if baban:
                        old_x = (450 + new_dist)
                        old_y = first_y
                        old_dist = new_dist
                        baban = 0
                        cy.append(first_y)
                        cx.append(new_dist + 450)
                        cz.append(new_z)
                        print(new_dist, old_x, old_y)
                    else:
                        if phase != 90 and phase != 180 and phase != 270 and phase != 0:
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
                            dis_dict = multiprocess2(new_dist, old_x, old_y, old_z, old_dist, multiplyer1,
                                                     multiplyer2,
                                                     phase, up_phase)
                            print(new_dist, old_x, old_y, dis_dict, phase, up_phase)
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
                            print(dis_dict, new_x, new_y, new_z, phase)
                        xlin = dis_dict[0]
                        ylin = dis_dict[1]
                        zlin = dis_dict[2]
                        cx.append(xlin), cy.append(ylin), cz.append(zlin)
                        cccok = str(xlin) + ', ' + str(ylin) + ', ' + str(zlin) + '\n'
                        ccc.append(str(cccok))
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
        ccclist = Manager().list()
        cxlist = Manager().list()
        cylist = Manager().list()
        czlist = Manager().list()
        p1 = Process(target=sayılr, args=(neulist,))
        p2 = Process(target=main1, args=(neulist, cxlist, cylist, czlist, ccclist))
        p1.start()
        time.sleep(5)
        p2.start()
    while p1.is_alive() or p2.is_alive():
        time.sleep(5)
    else:
        file.writelines(ccclist)
        ax.scatter(cxlist, cylist, czlist, c=np.linalg.norm([cxlist, cylist, czlist], axis=0))
        ax.plot_trisurf(np.array(cxlist), np.array(cylist), np.array(czlist))
        ax.view_init(60, 35)
        file.close()
        plt.show()
