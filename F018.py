print(f"\nSeja bem-vindo ao caixa\n")

a = float(input("Qual o valor total da compra?\nR$ "))
b = float(input("Qual o valor que você pagou?\nR$ "))

troco_total = round(b - a, 2)

print(f"\nValor da compra: R$ {a:.2f}")
print(f"Valor pago: R$ {b:.2f}")
print(f"Troco total: R$ {troco_total:.2f}\n")

troco_inteiro = int(troco_total)
centavos = round((troco_total - troco_inteiro) * 100)

cedulas = [100, 50, 20, 10, 5, 2, 1]
for c in cedulas:
    qtd = troco_inteiro // c
    if qtd > 0:
        print(f"{qtd} nota(s) de R$ {c}")
        troco_inteiro %= c


moedas = [50, 25, 10, 5, 1]
for m in moedas:
    qtd = centavos // m
    if qtd > 0:
        print(f"{qtd} moeda(s) de {m} centavo(s)")
        centavos %= m