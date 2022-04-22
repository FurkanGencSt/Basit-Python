meyve = {}
sebze = {}

musteri_sepeti = {}

def kabzimal():

    secim = input("Meyve icin 'm' sebze için 's' harfini yazınız: ")

    if secim.upper() == "M":
        meyve_secimi = input("Hangi meyveyi istediğinizi yazınız: ")
        kilo = int(input("Kaç kilo olduğunu yazınız: "))

        if meyve_secimi.upper() in meyve:
            meyve[meyve_secimi.upper()] += kilo
        else:
            meyve[meyve_secimi.upper()] = kilo

        devamMi = input("Devam etmek istiyorsanız E , istemiyorsanız H yazınız: ")
        if devamMi.upper() == "E":
            kabzimal()
        elif devamMi.upper() == "H":
            print("************")
            print("Manava Hoşgeldiniz.")
            print("************")
            manav()
            pass

    elif secim.upper() == "S":
        sebze_secimi = input("Hangi meyveyi istediğinizi yazınız: ")
        kilo = int(input("Kaç kilo olduğunu yazınız: "))

        if sebze_secimi.upper() in meyve:
            meyve[sebze_secimi.upper()] += kilo
        else:
            meyve[sebze_secimi.upper()] = kilo

        devamMi = input("Devam etmek istiyorsanız E , istemiyorsanız H yazınız: ")

        if devamMi.upper() == "E":
            kabzimal()
        elif devamMi.upper() == "H":
            print("************")
            print("Manava Hoşgeldiniz.")
            print("************")
            manav()
            pass
    elif secim.upper() != "M" or "S":
        kabzimal()


def manav():


    secim = input("Meyve icin 'm' sebze için 's' harfini yazınız: ")

    if secim.upper() == "M":
        meyve_secimi = input("Hangi meyveyi istediğinizi yazınız: ")
        kilo = int(input("Kaç kilo olduğunu yazınız: "))

        if meyve_secimi.upper() in meyve:
            if meyve[meyve_secimi.upper()] < kilo:
                print("Maalesef elimizde o kadar kalmamıştır.")
                manav()
            else:
                meyve[meyve_secimi.upper()] -= kilo
                if meyve_secimi.upper() not in musteri_sepeti:
                    musteri_sepeti[meyve_secimi.upper()] = kilo
                else:
                    musteri_sepeti[meyve_secimi.upper()] += kilo

        else:
            print("Maalesef o üründen stokta yok.")

        devamMi = input("Devam etmek istiyorsanız E , istemiyorsanız H yazınız: ")
        if devamMi.upper() == "E":
            manav()
        elif devamMi.upper() == "H":
            print("***Aldıklarınız***","\n",musteri_sepeti)
            pass

    elif secim.upper() == "S":
        sebze_secimi = input("Hangi meyveyi istediğinizi yazınız: ")
        kilo = int(input("Kaç kilo olduğunu yazınız: "))

        if sebze_secimi.upper() in meyve:
            if meyve[sebze_secimi.upper()] < kilo:
                print("Maalesef elimizde o kadar kalmamıştır.")
                manav()
            else:
                meyve[sebze_secimi.upper()] -= kilo
                if sebze_secimi.upper() not in sebze:
                    musteri_sepeti[sebze_secimi.upper()] = kilo
                else:
                    musteri_sepeti[sebze_secimi.upper()] += kilo

        else:
            print("Maalesef o üründen stokta yok.")

        devamMi = input("Devam etmek istiyorsanız E , istemiyorsanız H yazınız: ")

        if devamMi.upper() == "E":
            manav()
        elif devamMi.upper() == "H":
            print("***Aldıklarınız***","\n",musteri_sepeti)
            pass


    elif secim.upper() != "M" or "S":
        manav()




def baslangic():
    print("1-- Kabzimal","\n","2-- Manav")
    secim = int(input("Bir tanesini seciniz: "))
    if secim == 1:
        print("************")
        print("Kabzimale Hoşgeldiniz.")
        print("************")
        kabzimal()
    elif secim == 2:
        print("************")
        print("Manava Hoşgeldiniz.")
        print("************")
        manav()
    else:
        baslangic()
baslangic()

