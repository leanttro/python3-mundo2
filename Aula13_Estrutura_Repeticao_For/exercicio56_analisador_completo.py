somaidade = 0
nomehomem = ""
mediaidade = 0
idadehomem = 0
totalmulher = 0
for p in range(1,5):
    print("-------- {p} = Pessoa --------")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo (H/M): ")).strip().lower()
    somaidade = somaidade + idade

    if sexo == "h" and (p == 1 or idade > idadehomem):
        idadehomem = idade
        nomehomem = nome
    if sexo == "m" and idade < 20:
        totalmulher = totalmulher + 1

mediaidade = somaidade / 4
print("A média de idade do grupo é de {}".format(mediaidade))
print("O homem mais velho tem {} anos e o nome dele é {}".format(idadehomem,nomehomem))
print("O total de mulheres com menor de 20 anos é {}".format(totalmulher))