import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Coordinates of Grid Lines
X_Grid = [0, 4]  # Joint Points X
Y_Grid = [0, 5]  # Joint Points Y
Z_Grid = [0, 3, 5]  # Joint Points Z

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('Select Point')

X, Y, Z = list(), list(), list()
for i in X_Grid:
    for j in Y_Grid:
        for k in Z_Grid:
            X.append(i)
            Y.append(j)
            Z.append(k)
ax.scatter(X, Y, Z, marker="*", c="green", picker=5)

picked = []


def onpick(event):
    ind = event.ind[0]
    x, y, z = event.artist._offsets3d
    # print((x[ind],y[ind],z[ind]))
    picked.append((x[ind], y[ind], z[ind]))
    print(picked)
    if len(picked) == 2:
        # draw the line
        temp = np.array(picked)  # use a numpy array to simplify notation
        ax.plot(temp[:, 0], temp[:, 1], temp[:, 2])
        ax.figure.canvas.draw_idle()
        picked[:] = []  # reset list for future pick events


fig.canvas.mpl_connect('pick_event', onpick)
plt.show()