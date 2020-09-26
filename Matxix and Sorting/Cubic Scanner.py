import serial
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
tick_wait = ()
rotor_speed = ()
direction = ()
b = ()
ser = serial.Serial('COM3', 9600)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('Select Point')
while 1:
    for h in range(313):
        b = ser.readline().decode('ascii')
        garr = int(''.join(filter(str.isdigit, b)))
        if garr < 500:
            print(b)
        time.sleep(0.021 + ((1/3)/1000))
    m = (180 - garr) / 2
    zline = np.linspace(0, 15, 1000)
    xline = np.sin(zline)
    yline = np.cos(zline)
    ax.plot3D(xline, yline, zline, 'gray')
    ax.view_init(60, 35)
    plt.show()
    ser.close()
