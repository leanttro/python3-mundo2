compra = maismil = cont = 0
maisbarato = ''
menorvalor = 0

print("=" * 30)
print("LOJA SUPER BARATÃO")
print("=" * 30)

while True:
    produto = str(input("Digite o nome do produto: ")).strip()
    valor = float(input("Qual o valor: R$ "))

    compra += valor
    cont += 1

    if valor > 1000:
        maismil += 1

    if cont == 1:
        menorvalor = valor
        maisbarato = produto
    else:
        if valor < menorvalor:
            menorvalor = valor
            maisbarato = produto

    cond = str(input("Quer continuar [S/N]: ")).strip().upper()[0]
    if cond in "Nn":
        break

print("=" * 30)
print(f"O total da compra foi R${compra:.2f}.")
print(f"O total de compras com mais de R$1000 foi {maismil}.")
print(f"O produto mais barato foi {maisbarato}, custando R${menorvalor:.2f}.")
