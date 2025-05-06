n = str(input("Informe seu sexo [M/F]: ")).upper().strip()[0]
while n not in "FfMm":
    n = str(input("Código inválido, por favor, digite seu sexo [M/F]: ")).upper()
print("Sexo {} registrado com sucesso!".format(n))