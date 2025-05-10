
carteira = float(input("Quantos reais você tem?"))

dolar = 5.85
total = carteira / dolar

print(f"\n Você tem exatos R$ {carteira} em carteira, e na cotação atual do dolar ${dolar}, você poderá comprar exatos $ {total:.2f}")