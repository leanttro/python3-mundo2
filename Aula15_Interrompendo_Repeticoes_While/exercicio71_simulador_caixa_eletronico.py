for m in range(0, 10, 3):
    print(m)
for c in range (0,5):
    print(c)

print("="*30)
print("{:^30}".format("BANCO LELIS"))
print("="*30)

valor = int(input("Quanto você deseja sacar:R$ "))
total = valor
ced50 = 50
totalced50 = 0

while True:
    if total >= ced50:
        total = total - ced50
        totalced50 += 1
    else:
        print(f"Total de {totalced50} de {ced50} reais")
        if ced50 == 50:
            ced50 = 20
        elif ced50 == 20:
            ced50 = 10 
        elif ced50 == 10:
            ced50 = 1
        totalced50 = 0
        if total == 0:
            break
