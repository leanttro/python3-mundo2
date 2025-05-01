n = int(input("Ano do nascimento: "))
n1 = 2025 - n
if n1 <= 9:
    print("O atleta tem {} anos. \nClassificação Mirim".format(n1))
elif 9 < n1 <= 14:
    print("O atleta tem {} anos. \nClassificação Infantil".format(n1))
elif 14 < n1 <= 19:
    print ("O atleta tem {} anos. \nClassificação Sênior".format(n1))
else:
    print("O atleta tem {} anos. \nClassificação Master".format(n1))