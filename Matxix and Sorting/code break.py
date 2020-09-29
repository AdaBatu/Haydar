import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

data = [[ 1900., 800., 442.82], [ 1900., 900., 463.04], [ 1900.,1000.,
473.06], [ 1900.,1100., 485.07],
[ 1900.,1200., 498.63], [ 1900.,1300., 513.83], [ 1900.,1400., 536.1 ], [
1900.,1500., 551.29],
[ 1900.,1600., 566.5 ], [ 1900.,1700., 581.65], [ 1900.,1800., 603.91], [
2000., 800., 453.5 ],
[ 2000., 900., 473.75], [ 2000.,1000., 487.14], [ 2000.,1100., 499.48], [
2000.,1200., 513.39],
[ 2000.,1300., 528.92], [ 2000.,1400., 551.85], [ 2000.,1500., 567.35], [
2000.,1600., 582.9 ],
[ 2000.,1700., 598.4 ], [ 2000.,1800., 621.32], [ 2100., 800., 464.23], [
2100., 900., 485.34],
[ 2100.,1000., 502.87], [ 2100.,1100., 515.71], [ 2100.,1200., 530.13], [
2100.,1300., 546.14],
[ 2100.,1400., 570.05], [ 2100.,1500., 586.1 ], [ 2100.,1600., 602.15], [
2100.,1700., 618.15],
[ 2100.,1800., 642.09], [ 2200., 800., 474.94], [ 2200., 900., 498.72], [
2200.,1000., 516.91],
[ 2200.,1100., 530.09], [ 2200.,1200., 544.83], [ 2200.,1300., 561.2 ], [
2200.,1400., 585.8 ],
[ 2200.,1500., 602.17], [ 2200.,1600., 618.55], [ 2200.,1700., 634.89], [
2200.,1800., 659.46],
[ 2300., 800., 487.69], [ 2300., 900., 513.43], [ 2300.,1000., 532.64], [
2300.,1100., 546.32],
[ 2300.,1200., 561.57], [ 2300.,1300., 578.43], [ 2300.,1400., 604.03], [
2300.,1500., 620.89],
[ 2300.,1600., 637.76], [ 2300.,1700., 654.62], [ 2300.,1800., 680.23], [
2400., 800., 500.75],
[ 2400., 900., 526.83], [ 2400.,1000., 546.69], [ 2400.,1100., 560.71], [
2400.,1200., 576.3 ],
[ 2400.,1300., 593.52], [ 2400.,1400., 619.78], [ 2400.,1500., 636.98], [
2400.,1600., 654.2 ],
[ 2400.,1700., 671.38], [ 2400.,1800., 697.66], [ 2500., 800., 516.1 ], [
2500., 900., 542.71],
[ 2500.,1000., 563.6 ], [ 2500.,1100., 578.12], [ 2500.,1200., 594.18], [
2500.,1300., 611.89],
[ 2500.,1400., 639.17], [ 2500.,1500., 656.87], [ 2500.,1600., 674.58], [
2500.,1700., 692.26],
[ 2500.,1800., 719.53], [ 2600., 800., .05], [ 2600., 900., 556.98], [
2600.,1000., 578.51],
[ 2600.,1100., 593.37], [ 2600.,1200., 609.77], [ 2600.,1300., 627.81], [
2600.,1400., 655.76],
[ 2600.,1500., 673.82], [ 2600.,1600., 691.86], [ 2600.,1700., 709.87], [
2600.,1800., 737.83]]

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

