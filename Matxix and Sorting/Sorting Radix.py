giriş = input("Istediğiniz işlemi yazınız:")
liste = []
sonuc = []
anan = ""
dictinor = {}


def sortfactor(liste):
    x0 = []
    x1 = []
    x2 = []
    x3 = []
    x4 = []
    x5 = []
    x6 = []
    x7 = []
    x8 = []
    x9 = []
    for x in liste:
        for s in range(len(x)):
            son = x[-(s + 1)]
            dictinor[x] = son
    liste.clear()
    return print(dictinor)


if giriş == "sorting":
    while anan == int or "bitti":
        if anan != "bitti":
            anan = input("Sayınları giriniz.")
            liste.append(anan)
            print(anan + " Eklendi")
        else:
            liste.remove("bitti")
            print(liste)
            break
    else:
        print("lütfen sayı giriniz")
        liste.remove(anan)
    sortfactor(liste)
else:
    print("anan")
