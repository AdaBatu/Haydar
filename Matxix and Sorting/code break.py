import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


data = np.asarray(data)

a,b = len(np.unique(data[:,0])),  len(np.unique(data[:,1]))

X = data[:,0].reshape(a,b).T
Y = data[:,1].reshape(a,b).T
Z = data[:,2].reshape(a,b).T

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot_surface(X,Y,Z)

plt.show()
data = np.asarray(data)

plot_figure (data)

import math
sifre = input("fireni gir.")
listem = []

for x in range(len(sifre)):
    for i in range(10):
        ff = str(sifre)
        print(ff[x], i)
        gg = ff[x]
        while i == int(gg):
            print("tuttu")
            listem.append(i)
            break
print(listem)
print((310 ** 2 - 166.741 ** 2 - 250 ** 2 + 475 ** 2) / (2 * 475 - 900))

