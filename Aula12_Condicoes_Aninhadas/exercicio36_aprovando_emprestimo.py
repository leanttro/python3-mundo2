n = float(input("Valor da casa: "))
n1 = float(input("Salário do usuário: "))
n2 = int(input("Anos para quitação: "))
n3 = n / (n2*12)
print("Para pagar uma casa de R${:.2F} em {} anos, a prestação será no valor de {:.2F}".format(n,n2,n3))
if n3 <= n1*30/100:
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print("Empréstimo NÃO pode ser CONCEDIDO!")