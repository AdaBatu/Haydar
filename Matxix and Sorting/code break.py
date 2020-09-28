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
