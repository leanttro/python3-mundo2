n = float(input("Qual o peso:(kg) "))
n1 = float(input("Qual a altura:(m) "))
imc = n / (n1**2)
print(" O IMC dessa pessoa é {:.1f}".format(imc))
if imc < 18.5:
    print("PESO BAIXO")
elif 18.5 <= imc < 25:
    print("PESO NORMAL, PARABÉNS!") 
elif 25 <= imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 40:
    print("Obesidade")
else: 
    print("Obesidade Mórbida")