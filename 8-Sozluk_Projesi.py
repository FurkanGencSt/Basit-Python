

sozluk = {'Siyah':"Black",'Beyaz':'White',"Mor":"Purble"}




def anaMenu():
    secim = int(input("1-Arama\n2-Çıkarma\n3-Listeleme\n4-Cıkış\n\nBir secim yapınız: "))
    if secim == 1:
        while True:
            arama = input("Anlamına bakmak istediğiniz kelimeyi yazınız(Cıkmak icin --esc--): ").title()
            if arama == 'esc':
                anaMenu()
            if arama in sozluk:
                print(sozluk[arama])
                continue
            elif arama not in sozluk:
                secim = input("Maalesef o kelime sözlükte yok.\nUygulamayı gelistirmek ister misiniz(E/H)").upper()
                if secim == "E":
                    yeniKelime = input("O kelimenin anlamını yazınız: ").title()
                    sozluk[arama] = yeniKelime
                elif secim == "H":
                    anaMenu()

    elif secim == 2:
        while True:
            cikarma = input("Çıkarmak istediğiniz kelimeyi yazınız(Cıkmak icin '*'): ").title()
            if cikarma == '*':
                print("Başarılı bir şekilde çıkılıyor... Bekleyiniz.")
                time.sleep(2)
                anaMenu()
            else:
                sozluk.pop(cikarma)
                print(sozluk)
                print("Başarılı bir şekilde silinmiştir... Bekleyiniz.")
                continue
    elif secim == 3:
        for key in sozluk:
            print(key.title())
    elif secim == 4:
        print("Uygulamayı kullandığınız için teşekkürler :*")
    else:
        print("Hatalı bir secim yaptınız. Lütfen tekrak seciniz.")
        anaMenu()

anaMenu()