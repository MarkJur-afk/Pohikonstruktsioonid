taisarvud = 0
for i in range (15):
    arv=float(input(f"siseta {i+1}. arv"))
    if arv==int(arv):
        taisarvud+=1
print(f"Taisarvude kogus: {taisarvud}")

