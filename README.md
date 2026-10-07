# while ile şifre kontrol
ifre = "1234"
kalan_hak = 3
while kalan_hak > 0:
    gsifre = input("şifrenizi giriniz ")
    if gsifre == sifre:
        print("doğru şifre ")
        break
    else:
        kalan_hak -= 1
        print("yanlış şifre, kalan hak ", kalan_hak)
    if kalan_hak == 0:
     print("hakkınız bitti, çıkış yapılıyor")
    
