def Bucket_sorter(liste):
    dictinor = {}
    sonucum = []
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
    bu = 1
    while bu < (len(max(liste, key=len))) - 1:
        for x in liste:
            while bu < len(max(liste, key=len)):
                son = x[-bu]
                dictinor[x] = son
                break
            for i in dictinor:
                c = dictinor.get(i)
                if c == 0:
                    x0.append(i)
                if c == 1:
                    x1.append(i)
                if c == 2:
                    x2.append(i)
                if c == 3:
                    x3.append(i)
                if c == 4:
                    x4.append(i)
                if c == 5:
                    x5.append(i)
                if c == 6:
                    x6.append(i)
                if c == 7:
                    x7.append(i)
                if c == 8:
                    x8.append(i)
                if c == 9:
                    x9.append(i)
                break
                dictinor.clear()
                liste.pop()
        if x0:
            liste.append(x0)
        if x1:
            liste.append(x1)
        if x2:
            liste.append(x2)
        if x3:
            liste.append(x3)
        if x4:
            liste.append(x4)
        if x5:
            liste.append(x5)
        if x6:
            liste.append(x6)
        if x7:
            liste.append(x7)
        if x8:
            liste.append(x8)
        if x9:
            liste.append(x9)
        bu += 1
    else:
        for x in liste:
            while bu < len(max(liste, key=len)):
                son = x[-bu]
                dictinor[x] = son
                break
            for i in dictinor:
                c = dictinor.get(i)
                if c == 0:
                    x0.append(i)
                if c == 1:
                    x1.append(i)
                if c == 2:
                    x2.append(i)
                if c == 3:
                    x3.append(i)
                if c == 4:
                    x4.append(i)
                if c == 5:
                    x5.append(i)
                if c == 6:
                    x6.append(i)
                if c == 7:
                    x7.append(i)
                if c == 8:
                    x8.append(i)
                if c == 9:
                    x9.append(i)
                break
                dictinor.clear()
                liste.pop()
        if x0:
            sonucum.append(x0)
        if x1:
            sonucum.append(x1)
        if x2:
            sonucum.append(x2)
        if x3:
            sonucum.append(x3)
        if x4:
            sonucum.append(x4)
        if x5:
            sonucum.append(x5)
        if x6:
            sonucum.append(x6)
        if x7:
            sonucum.append(x7)
        if x8:
            sonucum.append(x8)
        if x9:
            sonucum.append(x9)

    return print(sonucum)


giriş = input("Istediğiniz işlemi yazınız:")
sonuc = []
anan = ""
list1 = []
if giriş == "sorting":
    while anan == int or "bitti":
        if anan != "bitti":
            anan = input("Sayınları giriniz.")
            list1.append(anan)
            print(anan + " Eklendi")
        else:
            list1.remove("bitti")
            print(list1)
            break
    else:
        print("lütfen sayı giriniz")
        list1.remove(anan)
    Bucket_sorter(list1)
else:
    print("anan")
