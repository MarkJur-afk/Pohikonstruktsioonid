print("*** MÄNG NUMBRITEGA ***")  
print()


while True:
    try:
        a = abs(int(input("Sisestage täisarv => ")))  
        break
    except ValueError:
        print("See ei ole täisarv") 

if a == 0:
    print("Nulliga pole mõtet midagi teha")  
else:
    print("Määrame, kui palju on paaris ja paarituid numbreid")
    print()

    c = b = a  
    paaris = 0  
    paaritu = 0

    while b > 0:
        if b % 2 == 0: 
            paaris += 1
        else:
            paaritu += 1
        b = b // 10 

    print("Paaris numbrid:", paaris)
    print("Paaritud numbrid:", paaritu)
    print()

    print("*Pöörame* sisestatud numbri")
    print()

    b = 0  
    while a > 0:
        number = a % 10  
        a = a // 10 
        b = b * 10 + number  

    print("*Pööratud* number", b)
    print()

    print("Kontrollime Syracuse'i hüpoteesi") 
    print()

    if c % 2 == 0:
        print("c - paarisarv. Jagame kahega.")
    else:
        print("c - paaritu arv. Korrutame 3-ga, lisame 1 ja jagame kahega.")

    while c != 1:
        if c % 2 == 0:
            c = c // 2  
        else:
            c = (3 * c + 1) // 2 
        print(c, end=" ")

    print()
    print("Hüpotees on õige!")
