s = 0
cont = 0
for c in range(0,6):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        s = s + n
        cont = cont + 1
print("A soma de todos os {} números PARES é {}".format(cont,s))
