from random import *
print("Vali tase: ")
valik = int(input("Vali tase 1, 2, 3: "))

if valik in [1, 2, 3]:
    if valik == 1:
        tehed = ["+", "-"]
        valitud_tehe = choice(tehed)
        print(valitud_tehe)
        if valitud_tehe == "+":
            print("Oli valitud summa")
        elif valitud_tehe == "-":
            print("Oli valitud minus")
    elif valik == 2:
        tehed = ["+", "-", "*", "/"]
        valitud_tehe = choice(tehed)
        print(valitud_tehe)
        if valitud_tehe == "+":
            print("Oli valitud summa")
        elif valitud_tehe == "-":
            print("Oli valitud minus")
        elif valitud_tehe == "*":
            print("Oli valitud umnozenie")
        elif valitud_tehe == "/":
            print("Oli valitud delenie")
    elif valik == 3:
        tehed = ["+", "-", "*", "/", "**"]
        valitud_tehe = choice(tehed)
        print(valitud_tehe)
        if valitud_tehe == "+":
            print("Oli valitud summa")
        elif valitud_tehe == "-":
            print("Oli valitud minus")
        elif valitud_tehe == "*":
            print("Oli valitud umnozenie")
        elif valitud_tehe == "/":
            print("Oli valitud delenie")
        elif valitud_tehe == "**":
            print("Oli valitud stepen")
else:
    print("On vaja valida ainult 1, 2 või 3!")

a = randint(0, 5)
b = randint(0, 5)
print(f"Millega võrdub {a} {valitud_tehe} {b} = ?")
vastus = int(input("Anna vastus: "))
if vastus == eval(str(a) + valitud_tehe + str(b)):
    print("Tore!")
else:
    print("Vale!")
