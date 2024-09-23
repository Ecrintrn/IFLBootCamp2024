import os

def ogrenci_kaydet(dosya_adi):
    if not os.path.exists(dosya_adi):
        with open(dosya_adi, "w") as dosya:
            pass

    with open(dosya_adi, "at") as dosya:
        devam = 'e'
        while devam.lower() == 'e':
            ogrencininAdiveSoyadi = input("Öğrencinin adını ve soyadını giriniz: ")
            ogrenciYY1 = input("Öğrencinin birinci yazılı yoklama puanını giriniz: ")
            ogrenciYY2 = input("Öğrencinin ikinci yazılı yoklama puanını giriniz: ")
            ogrenciP1 = input("Öğrencinin birinci performans puanını giriniz: ")
            ogrenciP2 = input("Öğrencinin ikinci performans puanını giriniz: ")
            
            kayit = f"{ogrencininAdiveSoyadi},{ogrenciYY1},{ogrenciYY2},{ogrenciP1},{ogrenciP2}\n"
            dosya.write(kayit)
            
            devam = input("Başka kayıt eklemek ister misiniz? [e/h]: ")

def main():
    dosya_adi = "ogrenciPuanBilgileri.csv"
    ogrenci_kaydet(dosya_adi)

if __name__ == "__main__":
    main()
