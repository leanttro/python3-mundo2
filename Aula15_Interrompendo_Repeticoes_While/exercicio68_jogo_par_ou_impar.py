from random import randint
v= 0
print("="*26)
print("Vamos jogar par ou ímpar!")
print("="*26)
while True:
    n = int(input("Digite um valor: "))
    pc = randint(0,10)
    s = n + pc
    t = " "
    while t not in "PI":
        t = str(input("Você quer PAR ou ÍMPAR[P/I]: ")).upper().strip()[0]
    print(f"Você jogou {n} e o computador {pc}. A soma deu {s}.")
    if t == "P":
        if s % 2 == 0:
            print("Você Venceu!")
            v += 1
        else:
            print("Você perdeu!")
            break
    elif t == "I":
        if s % 2 == 1:
            print("Você Venceu!")
            v += 1
        else:
            print("Você perdeu!")
            break
    print("Vamos jogar novamente...")
print(f"Game Over você venceu {v} vezes! ")