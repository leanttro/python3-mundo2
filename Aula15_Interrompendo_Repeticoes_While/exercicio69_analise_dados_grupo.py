tot18 = totalmasc = totalmulher = 0
while True:
    idade = int(input("Digite a idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Digito o sexo [M/F]: ")).upper().strip()[0]
    if idade >= 18:
        tot18 += 1
    if sexo in "Mm":
        totalmasc += 1
    if sexo in "Ff" and idade >= 20:
        totalmulher +=1

    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continuar [S/N]: ")).upper().strip()[0]
    if resp == "N":
        break
print(f"O total de pessoas maior de 18 anos é: {tot18}. \nO total de homens é {totalmasc}.\nO total de mulheres com mais de 20 anos é {totalmulher}.")
print("Acabou")
