import serial
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from multiprocessing import Process, Manager
import numpy as np
import math

axedif = 36 * 8
ilerleyis = 10
yukarı_ieri = 10
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


def sayılr():
#def sayılr(neulist):
    listof1 = []
    listof2 = []
    final1 = []
    final2 = []
    bab = 'afdsfsdf'
    ser = serial.Serial(port="COM4", baudrate=9600)
    time.sleep(4)
    ser.write(bab.encode('ascii'))
    for p in range(axedif*2):  # 577-1=576
        b = ser.readline().decode('ascii')
        raw = b[:-2].strip()
        unraw = raw[2:]
        if b[0] == "1":
            listof1.append(unraw)
        else:
            listof2.append(unraw)
        print(b)
        #time.sleep(0.055512)
    print(listof1, listof2)
    listof1.sort()
    print(listof1)
    listof2.sort()
    print(listof2)
    for ka1 in listof1:
        final1.append(int(ka1.split(" ")[1]))
    for ka2 in listof2:
        final2.append(int(ka2.split(" ")[1]))
    print(final1, final2)
    for fin in range(len(final1)):
        if final1[fin] == 0:
            neulist.append(final2[fin])
        else:
            if final2[fin] != 0:
                neulist.append(final1[fin] / 2 + final2[fin] / 2)
            if final2[fin] == 0:
                neulist.append(int(0))
    ser.close()
    return neulist


def multiprocess2(r, k, m, n, old_dist1, multi1, multi2, ileri, faz):
    p = math.sin(math.radians(ileri)) * r
    #o = int(round(p * p))
    cosimux = abs(math.cos(math.radians(ileri)) * r)
    #t = math.sqrt(abs((r ^ 2) - o))
    #x_dif = abs(old_dist1 - t)
    y_dif = abs(p)
    x = multi1 * abs(cosimux) + 450
    y = multi2 * abs(y_dif) + 450
    z = 450
    if faz == 0:
        sncu_dict = [x, y, z]
    else:
        ui = abs(math.cos(math.radians(faz)) * r)
        po = abs(math.sin(math.radians(ileri)) * ui)
        ou = abs(math.cos(math.radians(ileri)) * ui)
        #yu = math.sin(math.radians(ileri)) * cosimux
        #dif_bdt = math.sqrt(round(((k - x) * (k - x)) + ((m - y) * (m - y))))
        #cos_dif = math.cos(math.radians(faz)) * r
        zmif = abs(int(math.sin(math.radians(faz)) * r)) + 450
        #zdif = round(abs(450 - zmif))
        #balk = abs(math.sin(math.radians(ileri)) * cos_dif)
        #bro = math.sqrt(abs(round((zdif * zdif) + (balk * balk))))
        #xmif = math.sqrt(round(abs((bro * bro) - (dif_bdt * dif_bdt))))
        # ymif = math.sqrt(round(abs((dif_bdt * dif_bdt) - o)))
        # ymif = math.sqrt(abs((zdif ^ 2) - int(round(x_dif * x_dif))))
        x = multi1 * abs(ou) + 450
        y = multi2 * abs(po) + 450
        #if 90 < faz < 270:
            #x = multi1 * abs(old_dist1 - xmif) + 450   #causes problem in Algorithm
            #y = multi2 * abs(balk) + 450
        #else:
            #x = multi1 * abs(old_dist1 - xmif) + 450
            #y = multi2 * abs(balk) + 450
        z = zmif
        sncu_dict = [x, y, z]
        print(multi1, multi2, old_dist1) # balk, xmif
    return sncu_dict


#def main1(ooora, cx, cy, cz, ccc):
def main1(ooora):
    gargamel = int
    anan = 0
    old_x = int
    old_y = 0
    old_z = 450
    new_x = 0
    new_y = 0
    new_z = 450
    old_dist = 0
    cx, cy, cz, ccc = ([] for hj in range(4))

    multiplyer1 = 0
    multiplyer2 = 0
    first_y = 450
    phase = 0
    up_phase = 0
    baban = 1
    starttime = time.time()
    for ko in range(8):
        for h in range(36):
            if phase > 358:
                phase -= 360
            try:
                new_dist = int(ooora[0])
            except IndexError:
                time.sleep(1)
                new_dist = int(ooora[0])
            del ooora[0]
            print(new_dist)
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
                            dis_dict = multiprocess2(new_dist, old_x, old_y, gargamel, old_dist, multiplyer1,
                                                     multiplyer2,
                                                     phase, up_phase)
                            print(new_dist, old_x, old_y, dis_dict, phase, up_phase)
                        else:
                            if phase == 90:
                                new_x = 450
                                new_y = new_dist + 450
                                new_z = 450 + abs((math.sin(math.radians(up_phase)) * new_dist))
                                if up_phase != 0:
                                    new_y = abs(math.cos(math.radians(up_phase)) * new_dist) + 450
                            if phase == 180:
                                new_x = 450 - new_dist
                                new_y = 450
                                new_z = 450 + abs((math.sin(math.radians(up_phase)) * new_dist))
                                if up_phase != 0:
                                    new_x = -abs(math.cos(math.radians(up_phase)) * new_dist) + 450
                            if phase == 270:
                                new_x = 450
                                new_y = -new_dist + 450
                                new_z = 450 + abs((math.sin(math.radians(up_phase)) * new_dist))
                                if up_phase != 0:
                                    new_y = -abs(math.cos(math.radians(up_phase)) * new_dist) + 450
                                gargamel = new_dist
                            if phase == 0:
                                new_x = new_dist + 450
                                new_y = 450
                                new_z = 450 + abs((math.sin(math.radians(up_phase)) * new_dist))
                                if up_phase != 0:
                                    new_x = abs(math.cos(math.radians(up_phase)) * new_dist) + 450
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
    #anan = 1
    print('That took {} seconds'.format(time.time() - starttime))
    return cx, cy, cz, ccc


if __name__ == '__main__':
    with Manager() as manager:
        neulist = Manager().list()
        ccclist = Manager().list()
        cxlist = Manager().list()
        cylist = Manager().list()
        czlist = Manager().list()
        p1 = Process(target=sayılr, args=(neulist,))
        p2 = Process(target=main1, args=(neulist, cxlist, cylist, czlist, ccclist))
        #p1.start()
        #time.sleep(5)
        #p1.join()
        oooooo = sayılr()
        #oooooo = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
        #print(neulist)
        cxlist, cylist, czlist, ccclist = main1(oooooo)
        print(cxlist, cylist, czlist, ccclist)
        #p2.start()
    while p1.is_alive() or p2.is_alive():
        time.sleep(5)
    else:
        file.writelines(ccclist)
        ax.scatter(cxlist, cylist, czlist, c=np.linalg.norm([cxlist, cylist, czlist], axis=0))
        ax.plot_trisurf(np.array(cxlist), np.array(cylist), np.array(czlist))
        ax.view_init(60, 35)
        file.close()
        plt.show()
