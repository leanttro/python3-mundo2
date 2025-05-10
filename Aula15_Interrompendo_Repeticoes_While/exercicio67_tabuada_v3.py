while True:
    n = int(input("Qual número você gostaria de saber a tabuada: "))
    print("="*30)
    for c in range(1,11):
        print(f"A tabuada de {n} x {c} vale {n*c}")
    print("="*30)
    v = str(input("Gostaria de continuar [S/N]: ")).upper().strip()[0]
    if v not in "Ss":
        break
print("Fim ")

