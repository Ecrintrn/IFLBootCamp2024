def ortalama_hesapla(notlar):
    return sum(notlar) / len(notlar)

def dosyadan_oku(dosya_adi):
    with open(dosya_adi, "r") as dosya:
        for satir in dosya:
            yield satir.strip().split(',')

def main():
    dosya_adi = "ogrenciPuanBilgileri.csv"
    for girdi in dosyadan_oku(dosya_adi):
        isim = girdi[0]
        notlar = list(map(int, girdi[1:5]))
        ortalama = ortalama_hesapla(notlar)
        print(f"{isim} isimli öğrencinin ortalaması: {ortalama:.2f}")

if __name__ == "__main__":
    main()