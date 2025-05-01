n = int(input("Digite o ano do seu nascimento: "))
n1 = 2025 - n
n2 = 18 - n1
n3 = 18-(2025-n)
n6 = (2025-n)-18
n4 = 2025 + n3
n5 = 2025 - n6

print("Quem nasceu em {} terá {} anos em 2025".format(n,n1))
if n1 < 18:
    print("Ainda faltam {} anos para o seu alistamento militar!".format(n3))
    print("Seu alistamento será em {}.".format(n4))
elif n1 > 18:
    print("Você deveria ter se alistado há {} anos!".format(n6))
    print("Seu alistamento foi em {}".format(n5))
else: 
    print("Seu alistamento precisa ser ese ano!")