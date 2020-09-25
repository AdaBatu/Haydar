import numpy as np
import matplotlib.pyplot as plt
distance1 = ()
distance2 = ()
tick_wait = ()
rotor_speed = ()
direction = ()
b=()
while True:
    fig = plt.figure()
    ax = plt.axes(projection='3d', c='r', axis=0)
    zline = np.linspace(0, 15, 1000)
    xline = np.sin(zline)
    yline = np.cos(zline)
    ax.plot3D(xline, yline, zline, 'gray')
    ax.view_init(60, 35)
    plt.show()

