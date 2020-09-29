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
