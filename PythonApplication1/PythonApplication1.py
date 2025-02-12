nimi=input("Mis on sinu nimi?")
if nimi.isupper() and nimi=="JUKU":
    print ("Lahme kinnose")
    try:
        vanus=int(input("Kui vana oled?"))
        if vanus < 0 or vanus>100:
            pilet = "!!!"
        elif vanus <= 6:
            pilet = "Tasuta"
        elif vanus <= 14:
            pilet = "Lastepilet"
        elif vanus <= 65:
            pilet = "Taospilet"
        elif vanus <= 100:
            pilet = "soodus"
        print(pilet)
    except Exception as e:
        print("Tekkis viga: ", e)
else:
    print("Kinno ei lahme")

