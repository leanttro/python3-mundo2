import math
n = int(input("Digite um número inteiro: "))
print("Escolha uma das bases para conversão: \n[1] Converta para número BINÁRIO \n [2] Converta para número OCTAL \n[3] Converta para número HEXAGONAL")
n1 = int(input("Opção Escolhida: "))
if n1 == 1:
    print('{} convertido para Binário é {}'.format(n,bin(n)[2:]))
elif n1 == 2:
    print('{} convertido para Octal é {}'.format(n, oct(n)))
elif n1 == 3:
    print('{} convertido para Hexagonal é {}'.format(n,hex(n)))
elif n1 != 1 and n1 != 2 and n1 !=3:
    print("Por favor, escolha as opções entre: [1][2][3]!")

