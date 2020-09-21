giriş = input("Istediğiniz işlemi yazınız:")
liste = []
sonuc = []
anan = ""
dictinor = {}
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
    for x in liste:
        for s in range(len(x)):
            son = x[len(x) - (s + 1)]
            dictinor[x] = son
    liste.remove(x)
    print(dictinor)
else:
    print("anan")





