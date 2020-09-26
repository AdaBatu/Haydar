import matplotlib.pyplot as plt
import serial
import time
distance1 = ()
distance2 = ()
tick_wait = ()
rotor_speed = ()
direction = ()
b=()
ser = serial.Serial('COM3', 9600)
while 1:
    b = ser.readline().decode('ascii')
    garr = int(''.join(filter(str.isdigit, b)))
    if int(garr) < 500:
        print(b)
    time.sleep(0.001)
ser.close()

while True:
    fig = plt.figure()
    ax = plt.axes(projection='3d', c='r', axis=0)
    zline = np.linspace(0, 15, 1000)
    xline = np.sin(zline)
    yline = np.cos(zline)
    ax.plot3D(xline, yline, zline, 'gray')
    ax.view_init(60, 35)
    plt.show()

