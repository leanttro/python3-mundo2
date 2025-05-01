n = float(input("Digita a primeira nota: "))
n1 = float(input("Digite a segunda nota: "))
m = (n + n1) / 2

if m < 5:
    print("A média do aluno foi {} e ele está REPROVADO".format(m))
elif m >= 5 and m <= 6.9:
    print("A média do aluno foi {} e ele está de RECUPERAÇAÇÃO".format(m))
else:
    print("A média do aluno foi {} e ele está APROVADO! Parabéns!!!".format(m))

