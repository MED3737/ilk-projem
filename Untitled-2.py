#Muhammet Ensar Dökel present 
#Oyunun tüm hakları saklıdır



bitti = False
can = 100
iksir = 3
iksird = 20
dusmanlar = [("goblin", 20),("ork",30),("boss",30)]

for dusman, hasar in dusmanlar:
    if bitti:
        break
    while True:
     print("karşına" ,dusman,"çıktı! ne yapacacaksın?")
     secim = input("1 savaş 2 iksir iç 3 kaç" )
     if secim == "1":
         if can > hasar:
             can = can-hasar
             print(dusman,"Öldü! kalan canın" ,can)
             break
         if can <= hasar:
             print("canın yetmedi, öldün")
             bitti = True
             break
     elif secim == "2":
         if iksir>0:
            can = can + iksird
            iksir = iksir - 1
            print("iksir içtin, yeni canın",can,"kalan iksirin",iksir)
         elif iksir <=0:
            print("iksirin yok!")
     elif secim == "3":
        bitti = True
        print("kaçtın!")
        break
     else:
        print("geçersiz seçim")
if not bitti:
    print("tebrikler")