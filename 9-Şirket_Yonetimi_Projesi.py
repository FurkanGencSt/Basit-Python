
IK = {}

IT = {}

MUH = {}

def yoneticiPaneli():
    print("**********\nYönetici Paneline Hoşgeldiniz.\n**********")
    print("1-IK\n2-IT\n3-MUH")
    secim = int(input("Bir secim yapınız: "))

    if secim == 1: #IK
        print("1-İşçi Ekleme-Çıkarma\n2-Maaş Güncelleme\n3-Çalışanları Listele\nGeri gelmek icin '4' e basınız.\n")
        secim2 = int(input("Bir secim yapınız: "))
        if secim2 == 1: #İşçi ekleme Çıkartma
            while True:
                isim = input("Eklemek istediğiniz kişinin ismini giriniz: ").title()
                soyIsim = input("Eklemek istediğiniz kişinin soyismini giriniz: ").title()
                tamIsim = isim + " " + soyIsim
                maas = float(input("Yeni maaşı giriniz: "))
                if type(maas) == float:
                    IK[tamIsim] = maas
                else:
                    print("Lütfen bir sayı giriniz.")
                    continue
                # cinsiyet = input("Erkek ise E kadın ise K yazınız: ").upper()
                IK[tamIsim] = 0
                # IK[tamIsim][1] = cinsiyet
                devamMi = input("Yine eklemek istiyor musunuz?(E/H): ").upper()
                if devamMi == "E":
                    pass
                elif devamMi == "H":
                    anaEkran()



        elif secim2 == 2: #Maas Güncelleme
            while True:
                isim = input("Eklemek istediğiniz kişinin ismini giriniz: ").title()
                soyIsim = input("Eklemek istediğiniz kişinin soyismini giriniz: ").title()
                tamIsim = isim + " " + soyIsim

                while True:
                    maas = float(input("Yeni maaşı giriniz: "))
                    if type(maas) == float:
                        IK[tamIsim] = maas
                        break
                    else:
                        print("Lütfen bir sayı giriniz.")
                        continue
                devamMi = input("Yine eklemek istiyor musunuz?(E/H): ").upper()
                if devamMi == "E":
                    pass
                elif devamMi == "H":
                    anaEkran()
        elif secim2 == 3:#Çalışanları Listele
            print(IK)
        elif secim2 == 4: #Ana Ekran
            anaEkran()
        else:
            print("Hatalı bir girşi yaptınız.")
            yoneticiPaneli()


    elif secim == 2: #IT
        print("1-İşçi Ekleme-Çıkarma\n2-Maaş Güncelleme\n3-Çalışanları Listele\nGeri gelmek icin '4' e basınız.\n")
        secim2 = int(input("Bir secim yapınız: "))
        if secim2 == 1: #İşci Ekleme Çıkarma
            while True:
                isim = input("Eklemek istediğiniz kişinin ismini giriniz: ").title()
                soyIsim = input("Eklemek istediğiniz kişinin soyismini giriniz: ").title()
                tamIsim = isim + " " + soyIsim
                # cinsiyet = input("Erkek ise E kadın ise K yazınız: ").upper()
                IT[tamIsim] = 0
                maas = float(input("Yeni maaşı giriniz: "))
                if type(maas) == float:
                    IK[tamIsim] = maas
                else:
                    print("Lütfen bir sayı giriniz.")
                    continue
                # IK[tamIsim][1] = cinsiyet
                devamMi = input("Yine eklemek istiyor musunuz?(E/H): ").upper()
                if devamMi == "E":
                    pass
                elif devamMi == "H":
                    anaEkran()


        elif secim2 == 2: # Maaş Güncelleme
            while True:
                isim = input("Eklemek istediğiniz kişinin ismini giriniz: ").title()
                soyIsim = input("Eklemek istediğiniz kişinin soyismini giriniz: ").title()
                tamIsim = isim + " " +soyIsim

                while True:
                    maas = float(input("Yeni maaşı giriniz: "))
                    if type(maas) == float:
                        IT[tamIsim] = maas
                        break
                    else:
                        print("Lütfen bir sayı giriniz.")
                        continue
                devamMi = input("Yine eklemek istiyor musunuz?(E/H): ").upper()
                if devamMi == "E":
                    pass
                elif devamMi == "H":
                    anaEkran()
        elif secim2 == 3: #İşçileri Listeleme
            print(IT)
        elif secim2 == 4:
            anaEkran()
        else:
            print("Hatalı bir girşi yaptınız.")
            yoneticiPaneli()


    elif secim == 3:#MUH
        print("1-İşçi Ekleme-Çıkarma\n2-Maaş Güncelleme\n3-Çalışanları Listele\nGeri gelmek icin '4' e basınız.\n")
        secim2 = int(input("Bir secim yapınız: "))
        if secim2 == 1:
            while True:
                isim = input("Eklemek istediğiniz kişinin ismini giriniz: ").title()
                soyIsim = input("Eklemek istediğiniz kişinin soyismini giriniz: ").title()
                tamIsim = isim + " " + soyIsim
                maas = float(input("Yeni maaşı giriniz: "))
                # cinsiyet = input("Erkek ise E kadın ise K yazınız: ").upper()
                MUH[tamIsim] = 0
                if type(maas) == float:
                    MUH[tamIsim] = maas
                else:
                    print("Lütfen bir sayı giriniz.")
                    continue
                # IK[tamIsim][1] = cinsiyet
                devamMi = input("Yine eklemek istiyor musunuz?(E/H): ").upper()
                if devamMi == "E":
                    continue
                elif devamMi == "H":
                    anaEkran()


        elif secim2 == 2: #Maas Güncelleme
            while True:
                isim = input("Eklemek istediğiniz kişinin ismini giriniz: ").title()
                soyIsim = input("Eklemek istediğiniz kişinin soyismini giriniz: ").title()
                tamIsim = isim + " " + soyIsim

                while True:
                    maas = float(input("Yeni maaşı giriniz: "))
                    if type(maas) == float:
                        MUH[tamIsim] = maas
                        break
                    else:
                        print("Lütfen bir sayı giriniz.")
                        continue
                devamMi = input("Yine eklemek istiyor musunuz?(E/H): ").upper()
                if devamMi == "E":
                    pass
                elif devamMi == "H":
                    anaEkran()
        elif secim2 == 3:
            print(MUH)
        elif secim2 == 4:
            anaEkran()
        else:
            print("Hatalı bir girşi yaptınız.")
            yoneticiPaneli()

    elif type(secim) != int:
        print("Hatalı bir girşi yaptınız.")
        yoneticiPaneli()
    else:
        print("Hatalı bir giriş yaptınız.")
        yoneticiPaneli()
def anaEkran():
    secim = int(input("1-Calisan Listesi\n2-Yonetici Paneli\nSecim: "))
    if secim == 1:
        print("Hangi departmanda çalışan çalışanların listesini istersiniz?\n1-IK\n2-IT\n3-MUH")
        secim2 = int(input("Seciminiz:"))
        if secim2 == 1:
            print(IK)
        elif secim2 == 2:
            print(IT)
        elif secim2 == 3:
            print(MUH)
    elif secim == 2:
        yoneticiPaneli()

anaEkran()