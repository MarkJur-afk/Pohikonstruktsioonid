print( "Tere! Olen sinu uus sõber - Python!")
nimi = input("Mis su nimi on?")
print(f"{nimi} oi kui ilus nimi!")
while 1:
    try:
        soov =int(input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
        if soov== 1:
           print("indeksi leidmine")
           while True:
               try:
                   pikkus =int(input("mis on sinu pikkus?"))
                   break
                   while True:
                       try:
                           mass= float(input("mis on sinu mass"))
                           indeks = round(mass//(0.01*pikkus)**2,2)
                           if indeks < 16:
                                print("Tervisele ohtlik alakaal")
                           elif 16 <= indeks < 19:
                                print("Alakaal")
                           elif 19 <= indeks < 25:
                                print("Normaalkaal")
                           elif 25 <= indeks < 30:
                                print("Ülekaal")
                           elif 30 <= indeks < 35:
                                print("Rasvumine")
                           elif 35 <= indeks < 40:
                                print("Tugev rasvumine")

                           break
                       except:
                            print("kirjuta õige mass")
               except: 
                   print("kirjuta õige pikkus")
        elif soov == 0:
            print("kahju! see on väga kasulik info")
        else:
            print("vale valik. Saab valida ainult 1 või 0")

    except:
        print("vale soov!")