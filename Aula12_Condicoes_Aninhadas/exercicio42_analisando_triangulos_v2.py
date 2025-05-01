n = int(input("Primeiro segmento: "))
n1 = int(input("Segundo segmento: "))
n2 = int(input("Terceiro segmento: "))
if n + n1 > n and n1 + n2 > n and n2 + n > n1:
    print("É possível formar um triângulo! ")
    if n1 != n != n2 != n1 :
        print("Ele é ESCALENO")
    elif n1 == n2 == n:
        print("Ele é EQUILÁTERO")
    else:
        print("ISÓSCELES")
else:
    print("Não é possível formar um triângulo!")