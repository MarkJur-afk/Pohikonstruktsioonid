print( "Tere! Olen sinu uus s�ber - Python!")
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
                                print("�lekaal")
                           elif 30 <= indeks < 35:
                                print("Rasvumine")
                           elif 35 <= indeks < 40:
                                print("Tugev rasvumine")

                           break
                       except:
                            print("kirjuta �ige mass")
               except: 
                   print("kirjuta �ige pikkus")
        elif soov == 0:
            print("kahju! see on v�ga kasulik info")
        else:
            print("vale valik. Saab valida ainult 1 v�i 0")

    except:
        print("vale soov!")