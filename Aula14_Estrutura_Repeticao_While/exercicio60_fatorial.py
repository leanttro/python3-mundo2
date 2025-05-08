n = int(input("Digite o número pra saber o fatoria: "))
c =n
from math import factorial
f = factorial(n)
while c > 0:
    print("{}".format(c),end=" ")
    print("x" if c > 1 else "=" " {}".format(f), end=" ")
    c = c - 1


