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
print((310 ** 2 - 166.74122584551102 ** 2 - 250 ** 2 + 310 ** 2) / (2 * 310 - 900))
