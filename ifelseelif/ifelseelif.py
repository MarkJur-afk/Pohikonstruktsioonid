#Maidis 1
from random import *
n = randint(1, 10)
print (n)
if n > 5:
    print("*************")
    print(f"Arv {n} suurem kui viis ")
    print("*************")

arv = randint(-10, 10)

if arv > 0:
    print(f"+")
else:
    print("-") #viga null ei ole positiivne

if arv > 0:
    print("+")
elif arv == 0:
    print ("0")
else:
    print("-")
