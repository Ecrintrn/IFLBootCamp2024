import math

def cift_sayi_mi(liste, kucuk=True):
    for i in liste:
        if i % 2 != 0:
            return False
    cift = cift_sirali_mi(liste, kucuk)
    return cift

def tek_sayi_mi(liste, kucuk=True):
    for i in liste:
        if i % 2 == 0:
            return False
    tek = cift_sirali_mi(liste, kucuk)
    return tek
    
def cift_sirali_mi(liste, kucuk=True):
    num = liste[0]
    for i in liste[1:]:
        if num+2 != i:
            return False
        num = i
    return True

def ciftTek_hesaplama(liste, kucuk):
    if kucuk == False:
        return (liste[0] - 2)
    liste[2] + 2

def asal_sayi_hesaplama(liste, kucuk=True):
    if kucuk == False:
        if liste[0] <=2:
            return False
        num = liste[0] -1
        """is_prime = True
        for i in range(num, 1):
            for k in range(2, int(math.sqrt(i)) + 1):
                print("girdi")
                if i % k == 0:
                    is_prime= False
                    break
            if is_prime:
                return i
            i -= 1"""
        while True:
            if asal_sayi_mi([num]):
                return num
            num -= 1
    else:
        num = liste[2] + 1
        while True:
            if asal_sayi_mi([num]):
                return num
            num += 1

def asal_sayi_mi(liste, kucuk=True):
    for i in liste:
        if i < 2:
            return False
        for k in range(2, int(math.sqrt(i)) + 1):
            if i % k == 0:
                return False
    return asal_sirali_mi(liste, kucuk)

def asal_sirali_mi(liste, kucuk=True):
    num = liste[0]
    for i in liste[1:]:
        if i != asal_mi(num, liste, liste.index(i)):
            return False
        num = i 
    return True

def asal_mi(num, liste, index, kucuk=True):
    n = num + 1
    while True:
        is_prime = True
        for k in range(2, int(math.sqrt(liste[index])) + 1):
            if n % k == 0:
                is_prime = False
                break
        if is_prime:
            return n
        else:
            n+=1

def fibonacci_mi(liste, kucuk=True):
    for i in liste:
        if not fibonacci_kontrol(i):
            return False
    fibonacci = fibonacci_sirali_mi(liste)
    if fibonacci:
        return True
    return False

def fibonacci_kontrol(n):
    return karekök_hesaplama(5 * (n * n) + 4) or karekök_hesaplama(5 * (n * n) - 4)

def fibonacci_sirali_mi(liste, kucuk=True):
    if liste[0] + liste[1] == liste[2]:
        return True
    return False

def fibonacci_hesaplama(liste, kucuk=True):
    if kucuk == True:
        return liste[1] + liste[2]
    return liste[1] - liste[0]

def karesel_sayi_dizisi(liste, kucuk=True):
    for i in liste:
        if not karekök_hesaplama(i):
            return False
    karesel = karesel_sirali_mi(liste, kucuk)
    if karesel:
        return True
    return False

def karekök_hesaplama(num):
    return int(math.sqrt(num)) ** 2 == num

def karesel_sayi_hesaplama(liste, kucuk=True):
    if kucuk == False:
        ücüncüSayi = int(math.sqrt(liste[0]))
        return (ücüncüSayi-1) ** 2
    ücüncüSayi = int(math.sqrt(liste[2]))
    return (ücüncüSayi+1) ** 2

def karesel_sirali_mi(liste, kucuk=True):
    if int(math.sqrt(liste[0])) + 2 ==  int(math.sqrt(liste[1])) + 1  == int(math.sqrt(liste[2])):
        return True
    return False

def palindrom_sayi_mi(sayi):
    sayi_str = str(sayi)
    return sayi_str == sayi_str[::-1]

def palindrom_sayi_hesaplama(liste, kucuk=True):
    if kucuk == False:
        for i in range(liste[0]-1, liste[0] - 100, -1):
            if palindrom_sayi_mi(i):
                return i
    for i in range(liste[2] + 1, liste[2] + 100):
        if palindrom_sayi_mi(i):
            return i  

def palindrom_sirali_mi(liste):
    for sayi in liste:
        if not palindrom_sayi_mi(sayi):
            return False
    return True

def ucgensel_dizi_mi(liste, kucuk=True):
    for i in liste:
        ture = False
        for x in range(0, i+1):
            if x**2 + x == 2 * i:
                ture = True
                break
        if ture != True:
            return False
    ucgensel = ucgensel_sirali_mi(liste, kucuk)
    if ucgensel:
        return True
    return False

def ucgensel_sirali_mi(liste, kucuk=True):
    num = liste[0]
    for i in liste[1:]:
        if i != ucgensel_mi(num, i, kucuk):
            return False
        num = i
    return True

def ucgensel_mi(num, i, kucuk=True):
    ucgen = 0
    for x in range(0, i + 1):
            if x**2 + x == 2 * i:
                ucgen = x
    num += ucgen
    return num

def ucgensel_hesaplama(liste, kucuk=True):
    if kucuk == False:
        num = liste[1] - liste[0]
        ucgen = liste[0] - num + 1
        return ucgen
        
    num = liste[2]
    ucgen = 0
    for x in range(0, num + 1):
            if x**2 + x == 2 * num:
                ucgen = x
    num += ucgen + 1
    return num

def aritmetrik_dizi(liste):
    if liste[2] - liste[1] == liste[1] - liste[0]:
        return ( liste[1] - liste[0]) + liste[2]

def geometrik_dizi(liste):
    if liste[2] / liste[1] == liste[1] / liste[0]:
        return int((liste[1] / liste[0]) * liste[2])

def hepsi():
    while True:
        liste = input("Örüntünün 3 tane sayısını sırayla giriniz: ")
        s1, s2, s3 = liste.split(", ")
        kucuk = True
        if int(s1)>int(s3):
            kucuk = False
            liste = [int(s3), int(s2), int(s1)]
        else:
            liste = [int(s1), int(s2), int(s3)]

        cift_mi = cift_sayi_mi(liste, kucuk)
        tek_mi = tek_sayi_mi(liste, kucuk)
        asal_mi = asal_sayi_mi(liste, kucuk)
        fibonacci = fibonacci_mi(liste, kucuk)
        karesel_mi = karesel_sayi_dizisi(liste, kucuk)
        palindrom = palindrom_sirali_mi(liste)
        ucgensel = ucgensel_dizi_mi(liste, kucuk)
        if kucuk == False:
            liste1 = liste[::-1]
            aritmetrik = aritmetrik_dizi(liste1)
            geometrik = geometrik_dizi(liste1)
        else:
            aritmetrik = aritmetrik_dizi(liste)
            geometrik = geometrik_dizi(liste)
    
        print(f"Çift Sayı Dizisi: {ciftTek_hesaplama(liste, kucuk) if cift_mi else '-'}")
        print(f"Tek Sayı Dizisi: {ciftTek_hesaplama(liste, kucuk) if tek_mi else '-'}")
        print(f"Asal Sayı Dizisi: {asal_sayi_hesaplama(liste, kucuk) if asal_mi else '-'}")
        print(f"Palindrom Sayı Dizisi: {palindrom_sayi_hesaplama(liste, kucuk) if palindrom else '-'}")
        print(f"Fibonacci Sayı Dizisi: {fibonacci_hesaplama(liste, kucuk) if fibonacci else '-'}")
        print(f"Karesel Sayı Dizisi: {karesel_sayi_hesaplama(liste, kucuk) if karesel_mi else '-'}")
        print(f"Uçgensel Sayı Dizisi: {ucgensel_hesaplama(liste, kucuk) if ucgensel else '-'}")
        print(f"Aritmetrik Sayı Dizisi: {aritmetrik if aritmetrik else '-'}")
        print(f"Geometrik Sayı Dizisi: {geometrik if geometrik else '-'}")
        baska = input("Başka örüntü inceleyecek misiniz? [e/h] : ")
        if baska.lower() == "h":
            print("Matematik örüntüleri kapsamında çalışmamız sona ermiştir. Güle güle… :)")
            break

hepsi()