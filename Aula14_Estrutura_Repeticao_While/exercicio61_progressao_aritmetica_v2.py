from time import sleep
print("Gerador de PA")
print("*"*14)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
termo = primeiro
c = 1
print("GERANDO...")
sleep(1)
while c <= 10:
    print("{} -> ".format(termo), end=" ")
    termo = termo + razao
    c = c + 1
print("Fim", end=" ")