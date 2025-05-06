from random import randint
from time import sleep
tentativas = 0
jogador = 0
acerto = False
a = "*"*20
computador = randint(0,2)
print("*"*77)
print("{} Vamos jogar o jogo da adivinhação ? {} \n          Eu penso em 1 número de 1 a 5 e você joga até acertar!".format(a,a))
print("*"*77)
while not acerto: 
    jogadro = int(input("Digite um número inteiro de 0 a 5: "))
    tentativas = tentativas + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print("Menos!Tente mais uma vez!")
        elif jogador < computador:
            print("Mais! Tente mais uma vez")
print("Acertou com {}. Parabéns! ".format(tentativas))

