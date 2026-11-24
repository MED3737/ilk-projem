#Muhammet Ensar Dökel present 
#Oyunun tüm hakları saklıdır

can = 100
iksir =3
dusmanlar =[("goblin",20),("Ork",30),("ejderha",50)]
oyunbitti = False
for dusman, hasar in dusmanlar:
    print()
    print("karşına",dusman,"çıktı!" ,"kalan can",can)
    secim = input(" 1 savaş 2 iksir iç (+30 can) 3 kaç")
    if secim == "1":
        can =can-hasar
        print("savaştın! kalan can",can)
        if can <=0:
         print("kaybettin... görüşürüz")
        break
    elif secim == "2":
        if iksir > 0:
            iksir -=1
            can += 20
            print("iksir içtin kalan canın",can,"kalan iksirin",iksir)
        else:
            print("iksirin kalmadı!")
    elif secim == "3":
        print("kaçtın, oyun bitti görüşürüz")
        oyunbitti=True
        break
    else:
        print("gecersiz seçim")
if can > 0 and not oyunbitti:
 for dusman,hasar in dusmanlar:
        print()
        print("karşına",dusman,"çıktı, canın",can,"iksir sayın",iksir)
        secim = input("1 savaş 2 iksir iç 3 kaç")
        if secim == "1":
                can=can-hasar
                print(dusman,"düşman öşdü kalan canın",can)
                if can<=hasar:
                 print("Öldün! kaynrttin, görüsürüz")
                 break
        elif secim=="2":
                if iksir > 0:
                        iksir-=1
                        can+=20
                        print("iksir içtin kalan can", can,"kalan iksir" ,iksir)
                else:
                                print("iksirin yok")
        elif secim =="3":
                print("oyun bitti")
                oyunbitti=True
                break