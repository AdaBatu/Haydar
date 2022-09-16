import serial
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from multiprocessing import Process, Manager
import numpy as np
import math

fig = plt.figure()
X_Grid = [0, 900]
Y_Grid = [0, 900]
Z_Grid = [0, 900]
ax = plt.axes(projection='3d')
ax.set_xlabel('X-Achse')
ax.set_ylabel('Y-Achse')
ax.set_zlabel('Z-Achse')
ax.set_title('3 d-Projection')
file = open("Datei.txt", "w")


def Sammle_Datei():
    Roh_Daten = []
    Echte_Daten = []
    bab = 'asd'
    ser = serial.Serial(port="COM4", baudrate=9600)
    time.sleep(4)
    ser.write(bab.encode('ascii'))
    while 1:  # 577-1=576
        b = ser.readline().decode('ascii')[:-2]
        #raw = b[:-2].strip()
        #unraw = raw[2:]
        if b == "finito":
            break
        if b == "durduk ab":
            print("Überhitzung!!")
        Roh_Daten.append(b)
        Roh_Daten.sort()
        for Data1 in Roh_Daten:
            Axe1 = Data1.split()[:2]
            Abstand1 = Data1.split()[2]
            for Data2 in Roh_Daten:
                Axe2 = Data2.split()[:2]
                Abstand2 = Data2.split()[2]
                if Axe1 == Axe2:
                    Final_Abstand = (Abstand1 + Abstand2)/2 
                    Echte_Daten.append(str(Axe1[0] + " " + Axe1[1] + " " + Final_Abstand))
                    Roh_Daten.remove(Data1)
        return Echte_Daten

    
def Messen(Punkt_Data):
    x_list = []
    y_list = []
    z_list = []
    Daten_list = []
    for Data in Punkt_Data:
        Höhe = Data.split()[0] 
        Azimut = Data.split()[1]
        Abstand = Data.split()[2]
        vi = abs(math.cos(math.degrees(Höhe)) * Abstand)
        vx = abs(math.cos(math.degrees(Azimut)) * vi)
        vy = abs(math.sin(math.degrees(Azimut)) * vi)
        vz = abs(math.sin(math.degrees(Höhe)) * Abstand)
        if Höhe > 90 and Höhe < 270:
            v1 = -1
        else: 
            v1 = -1
        if Azimut > 180 :
            v2 = 1
        else:
            v2 = -1
        x_list.append(vx * v1)
        y_list.append(vy * v2)
        z_list.append(vz)
        Daten_list.append(str(vx * v1) + ', ' + str(vy * v2) + ', ' + str(vz) + '\n')
    return x_list, y_list, z_list, Daten_list

Echte_Daten = Sammle_Datei()
cx_list, cy_list, cz_list, cDaten_list = Messen(Echte_Daten)

file.writelines(cDaten_list)
ax.scatter(cx_list, cy_list, cz_list, c=np.linalg.norm([cx_list, cy_list, cz_list], axis=0))
ax.plot_trisurf(np.array(cx_list), np.array(cy_list), np.array(cz_list))
ax.view_init(60, 35)
file.close()
plt.show()