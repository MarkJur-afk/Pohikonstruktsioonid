import random

print("*** Matemaatika Test ***")

while True:
    try:
        raskusaste = int(input("Valige raskusaste (1 - kerge, 2 - keskmine, 3 - raske): "))
        if raskusaste not in [1, 2, 3]:
            raise ValueError
        break
    except ValueError:
        print("Palun sisestage 1, 2 või 3.")

while True:
    try:
        ulesannete_arv = int(input("Mitu ülesannet soovite lahendada? "))
        if ulesannete_arv <= 0:
            raise ValueError
        break
    except ValueError:
        print("Palun sisestage positiivne arv.")

oiged_vastused = 0

for i in range(ulesannete_arv):
    if raskusaste == 1:
        tehte_tyyp = ['+', '-']
        arv_vahemik = (1, 10)
    elif raskusaste == 2:
        tehte_tyyp = ['+', '-', '*', '/']
        arv_vahemik = (1, 20)
    else:
        tehte_tyyp = ['+', '-', '*', '/', '**']
        arv_vahemik = (1, 50)

    esimene_arv = random.randint(*arv_vahemik)
    teine_arv = random.randint(*arv_vahemik)
    tehtemärk = random.choice(tehte_tyyp)

    if tehtemärk == '/':
        teine_arv = random.randint(1, arv_vahemik[1])
        esimene_arv = teine_arv * random.randint(1, arv_vahemik[1])

    ülesanne = f"{esimene_arv} {tehtemärk} {teine_arv}"
    õige_vastus = eval(ülesanne)

    while True:
        try:
            kasutaja_vastus = float(input(f"Lahenda: {ülesanne} = "))
            break
        except ValueError:
            print("Vale sisestus, palun sisestage number.")

    if abs(kasutaja_vastus - õige_vastus) < 0.01:
        print("Õige vastus!")
        oiged_vastused += 1
    else:
        print(f"Vale! Õige vastus on {õige_vastus}")

skoor = (oiged_vastused / ulesannete_arv) * 100

if skoor < 60:
    hinne = 2
elif skoor < 75:
    hinne = 3
elif skoor < 90:
    hinne = 4
else:
    hinne = 5

print(f"Test läbi! Teie tulemus: {skoor:.2f}% - Hinne {hinne}")
