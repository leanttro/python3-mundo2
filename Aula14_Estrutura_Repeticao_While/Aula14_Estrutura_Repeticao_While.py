
"""for c in range(1,10):
    print(c)
print("Fim")"""

"""c = 1
while c < 10:
    print(c)
    c = c + 1
print("Fim")"""

"""s = 0
for c in range (1,6):
    n = int(input("Digite um número: "))
    s = s + n
print("A soma de todos os números foi {}".format(s))"""

"""s = 0
while s != 10:
    s = int(input("Digite um número: "))
print("FIm")"""

"""r = "S"
while r == "S":
    n = int(input("Digite um valor: "))
    r = str(input("Quer continuar? (S/N) ")).upper()
print("FIM")"""


n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite um número: "))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print("A quantidade de números pares até você digitar 0 foi {} e números ímpares foi {}".format(par, impar))
print("Fim")
