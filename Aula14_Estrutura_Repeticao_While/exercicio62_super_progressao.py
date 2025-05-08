from time import sleep
print("*"*14)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
termo = primeiro
c = 1
total = 0
mais = 10
print("GERANDO...")
sleep(1)
while mais != 0:
    total = total + mais
    while c <= total:
        print("{} -> ".format(termo), end=" ")
        termo = termo + razao
        c = c + 1
    print("PAUSA", end=" ")
    mais = int(input("\nQuantos termos você quer mostrar a mais ? "))
print("Progressão finalizada com {} termos mostrados".format(total), end="")