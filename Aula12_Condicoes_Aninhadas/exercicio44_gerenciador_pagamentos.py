print("{} Lojas Lelis {}".format("="*13,"="*13))
n = float(input("Qual o preço da compra: "))
print("Formas de pagamento: \n[ 1 ] à vista do pix \n[ 2 ] à vista no crédito \n[ 3 ] parcelado 2x no crédito \n[ 4 ] parcelado 3x no crédito ")
n1 = int(input("Escolha uma opção: "))
if n1 == 1:
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final!".format(n,n-n*10/100))
elif n1 == 2:
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(n,n-n*5/100))
elif n1 == 3:
    print("Sua compra ficou no valor de R${:.2f} em 2x sem Juros".format(n))
elif n1 == 4:
    n2 = int(input("Quantas parcelas: "))
    if  2 < n2 <= 10:
        n3 = (n + (n*20/100))/n2
        print("Sua compra será parcelada em {}x de {}. Sua compra vai de {} para {} no final.".format(n2,n3,n,n+n*20/100))
