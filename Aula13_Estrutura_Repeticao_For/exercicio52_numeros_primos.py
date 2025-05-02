n = int(input("Digite um número: "))
for c in range(1,n+1):
    if n % c ==0:
        print("\033[:35m{}".format(c), end=" ")
    else:
        print("\033[m{}".format(c), end = " ")
    