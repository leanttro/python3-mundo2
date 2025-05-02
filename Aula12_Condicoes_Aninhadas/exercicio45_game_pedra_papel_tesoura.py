import time
from random import randint
print("PEDRA [ 0 ]")
print("PAPEL [ 1 ]")
print("TESOURA [ 2 ]")
n = int(input("Escolha uma opção para jogar: "))
time.sleep(0.7)
print("CARREGANDO...")
time.sleep(0.5)
print("JO")
time.sleep(0.5)
print("KEN")
time.sleep(0.5)
print("PO")
time.sleep(0.5)

lista = ["Pedra","Papel","Tesoura"]
pc = randint(0,2)
print("="*15)
print("O computador escolheu {}.".format(lista[pc]))
print("O jogador escolheu {}.".format(lista[n]))
print("="*15)
if pc == 0:
    if n == 0:
        print("EMPATE")
    elif n == 1:
        print("JOGADOR VENCE")
    elif n == 2:
        print("COMPUTADOR VENCE!")
    else:
        print("JOGADA INVÁLIDA!")
elif pc == 1:
    if n == 1:
        print("EMPATE!")
    elif n == 0:
        print("COMPUTADOR VENCE")
    elif n == 2:
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVÁLIDA")
elif pc == 2:
    if n == 2:
        print("EMPATE!!")
    elif n == 1:
        print("COMPUTADOR VENCE")
    elif n == 0:
        print("JOGADOR VENCE")
    else:
        print("Jogada Inválida!") 
else:
    print("Jogada Inválida!")
    
