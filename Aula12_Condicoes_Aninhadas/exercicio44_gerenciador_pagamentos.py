print("{} Lojas Lelis {}".format("="*13,"="*13))
n = float(input("Qual o preço da compra: "))
print("Formas de pagamento: \n[ 1 ] à vista do pix \n[ 2 ] à vista no crédito \n[ 3 ] parcelado 2x no crédito \n[ 4 ] parcelado 3x no crédito ")
n1 = int(input("Escolha uma opção: "))
if n1 == 1:
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final!".format(n,n-n*10/100))
elif n1 == 2:
    print("Sua compra de R${:.2f} vai custar R${:,2f} no final".format(n,n-n*5/100))
elif n1 == 3:
    print("Sua compra ficou no valor de R${} em 2x sem Juros".format(n))
elif n1 == 4:
    n2 = str(input("Quantas parcelas: "))
    print()
