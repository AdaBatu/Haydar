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
    sncu_dict[x] = x
    sncu_dict[y] = y
    return x, y


while 1:
    baban = 1
    for h in range(313):
        b = ser.readline().decode('ascii')
        new_dist = int(''.join(filter(str.isdigit, b)))
        if new_dist < 500:
            if baban:
                old_x = new_dist
                old_dist = new_dist
                baban = 0
            else:
                print(b)
                if __name__ == '__main__':
                    starttime = time.time()
                    processes = []
                    for i in range(0, 10):
                        p = multiprocessing.Process(target=multiprocess, args=(i,))
                        processes.append(p)
                        p.start()
                    for process in processes:
                        process.join()
                print(multiprocess(new_dist, old_x, old_y, old_dist))
                print('That took {} seconds'.format(time.time() - starttime))
                print(new_x, new_y)
                old_x, old_y = new_x, new_y
                old_dist = new_dist
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
