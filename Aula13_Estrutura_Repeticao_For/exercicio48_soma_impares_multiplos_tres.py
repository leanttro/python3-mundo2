s = 0
c = 0
for n in range (1,501,2):
    if n  % 3 == 0:
        s = s + n
        c = c + 1
        print(n, end= " ")
print("\nA soma de todos os {} entre os múltiplos de 3 entre 1 e 500 é {}".format(c,s))