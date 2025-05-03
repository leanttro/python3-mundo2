frase = str(input("Digite uma frase: ")).strip().upper()
palavra = frase.split()
junto = "".join(palavra)
inverso = "" 
inverso = junto[::-1]
"""for letra in range(len(junto) - 1, -1,-1):
    inverso = inverso + junto[letra]"""
if inverso == junto :
    print("Temos um palíndromo!")
else:
    print("Não temos um palíndromo!")