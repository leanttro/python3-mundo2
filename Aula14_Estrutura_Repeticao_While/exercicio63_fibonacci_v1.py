print("="*30)
print("Sequência de Fibonacci")
print("="*30)
n = int(input("Quantos termos você quer mostrar? "))
t1 = 0
t2 = 1
print("{} -> {}".format(t1,t2), end="")
cont = 3

while cont <= 3:
    t3 = t1 + t2
    print("-> {}".format(t3), end="")
    cont = cont + 1
print("Fim")