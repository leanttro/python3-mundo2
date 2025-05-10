r = "S"
cont = soma = maior = menor = media = 0
while r in "Ss":
    num = int(input("Digite um número: "))
    cont = cont + 1
    soma = soma + num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    r = str(input("Deseja continuar? [S/N]: ")).upper().strip()[0]
media = soma / cont
print("A quantidade de números digitados foi {} e a média deles é {}".format(cont,media))
print("O maior número é o {} e o menor é o {}".format(maior,menor))
    
