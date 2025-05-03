from datetime import date 
atual = date.today().year
tmaior = 0
tmenor = 0
for pess in range(1,8):
    nasc = int(input("Em que ano a {} pessoa nasceu: ".format(pess)))
    idade = atual - nasc
    if idade >= 18:
        tmaior = tmaior + 1
    else:
        tmenor = tmenor + 1
print("Ao todo tivemos {} pessoas Maiores de idade.".format(tmaior))
print("Ao todo tivemos {} pessoas Menores de idade.".format(tmenor))