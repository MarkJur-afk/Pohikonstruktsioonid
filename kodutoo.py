import random
# #1
# taisarvud = 0
# for i in range (5):
#      while True:
#          try:
#              arv=float(input(f"siseta {i+1}. arv"))
#              break
#          except:
#              print("Kirjuta ainult numbrid")
#              if arv==int(arv):
#                  taisarvud+=1
# print(f"Taisarvude kogus: {taisarvud}")



# #  #2
# summa=0
# while True:
#      try:    
#          A = int(input("siseta number A: "))
#          if A>1:
#            for i in range(1, A+1):
#                  summa +=1    
#            print(summa)
#            break
#          else:
#              print("A peab olla rohkem kui 1")
#      except:
#          print("vale format")
# #3
# summa = 0
# while True:
#      try:
#          if arv>1:
#              for i in range(8):
#                  arv = int(input("siseta number"))
#                  summa += arv   
#              print(summa)
#          else:
#              print("arv peab olla suurem kui 1")       
#          break
#      except:
#          print("vale format")



# #4
# # for i in range(10,21):
# #   print(i**2)  

# #5
# summa = 0
# while True:
#      try:
#          N=int(input("sisseta oma - number: "))
#          if N>0:
#              for i in range(N, 0):
#                  arv = float(input(f"siseta {i}. arv"))
#                  if arv < 0:
#                      summa+=arv
#              print(f"Summa vordub {summa}-ga")
#              break
#          else:
#              print("ainult otritsatelnqe")
#      except:
#          print("vale format")


# #6
# summa = 0
# N=int(input("siseta numbrid"))
# for i in range(1, N):
#     summa = i
#     print(summa)


# #7
# A = int(input("siseta esimene number: "))
# B = int(input("siseta teine number: "))
# K = int(input("siseta oma number: "))
# for i in range (A, B + 1):
#     if i % K == 0:
#         print(i)

#8
# for inches in range(1, 21):
#     cm = inches * 2.5
#     print(cm)



#9
# S = int(input("Kui plaju raha te panite: "))
# N = int(input(f"Kui palju aastat te panite {S} eurot: "))
# if S < 10000 and N < 10:
#     foryear = S * 0.03
#     vklad = foryear * N
#     print(f"Parast {N} aastat, sina saad {vklad} eurot!")
# else:
#     print("Bankis meil ei ole niimodi")



# #10
# for j in range(10):
#     a1=float(input("Esimene arv: "))
#     a2=float(input("Teine arv: "))
#     if a1>a2:
#         print(f"Suurme on {a1}")
#     elif a2>a1:
#         print(f"Suurem on {a2}")
# print()


#11
K = random.randint(1, 9)
print(f"random number: {K}")

product = 1
found = False

for num in range(11, 100, 2):
    if num % K == 0:
        product *= num
        found = True

if found:
    print(f"Arvude korrutis: {product}")
else:
    print("Sobivaid numbreid pole.")






# #15
# for j in range(10):
#     for i in range (10):
#         print(i, end=" ")
#     print()
    
# #16
# for j in range(10):
#     for i in range (10, 0):
#         print(i, end=" ")
#     print()