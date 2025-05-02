print("="*20)
print("10 termos de uma PA")
print("="*20)
n = int(input("Primeiro termo: "))
n1 = int(input("Razão: "))
for c in range(n,n+(n1*10),n1):
    print(c, end=" ")
print("--- Acabou")