n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
print("="*20)
n3 = 0
while n3 != 5: 
    n3 = int(input("\nSomar [1] \nMultiplicar [2] \nMaior [3] \nNovos Números [4] \nEncerrar programa [5] \n>>>>> Qual a sua opção: "))
    if n3 == 1:
        print("\nA soma entre {} e {} é {}. ".format(n1, n2, n1+n2))
    elif n3 == 2:
        print("\nA multiplicação entre {} e {} é {}".format(n1,n2,n1*n2))
    elif n3 == 3:
        if n1 > n2:
            print("\nO maior número entre {} e {} é {}".format(n1,n2,n1))
        elif n1 < n2:
            print("\nO maior número entre {} e {} é {}".format(n1,n2,n2))
        else:
            print("\nOs números são iguais!")
    elif n3 == 4:
        print("\n")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
        print("="*20)
    elif n3 == 5:
        print("Fim")
    else:
        print("Por favor, {} não é um número válido. Selecione entre 1 e 5".format(n3))

