# Ülesanne 2
nimi1 = input("Sisesta esimese inimese nimi: ")
nimi2 = input("Sisesta teise inimese nimi: ")
if nimi1 == 'Mark' or 'Roma' and nimi2 == 'Roma' and 'Mark':
    print("Tana olete pinginaabrid")
else:
    print("Tana ei ole pinginaabrid")
#--------------------------------------------------I
if nimi1.isalpha() and nimi2.isalpha():
    print("Tana olete pinginaabrid")
else:
    print("Tana ei ole pinginaabrid")