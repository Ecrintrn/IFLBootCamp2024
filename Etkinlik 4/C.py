with open("ogrenciPuanBilgileri.csv", "r") as dosya:
    arananOgrenci = input("Ortalamasını öğrenmek istediğiniz öğrencinin adını ve soyadını yazınız: ")
    ogrenciBulundu = False

    for satir in dosya:
        girdi = satir.strip().split(',')
        isim = girdi[0].strip()

        if arananOgrenci.lower().replace(' ', '') == isim.lower().replace(' ', ''):
            ogrenciBulundu = True
            notlar = list(map(int, girdi[1:5]))
            ortalama = sum(notlar) / len(notlar)
            print(f"{isim} isimli öğrencinin puanları: {', '.join(map(str, notlar))}")
            print(f"{isim} isimli öğrencinin ortalaması: {ortalama:.2f}")

    if not ogrenciBulundu:
        print(f"{arananOgrenci} adlı kişi bulunamadı.")
