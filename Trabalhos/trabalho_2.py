# Bem-vindo e cardápio formatado
print("Bem-vindo à Loja de Gelados do Felippe Nardin")
print("----------------------Cardápio------------------------")
print("---| Tamanho |  Cupuaçu (CP)  |  Açaí (AC)   |---")
print("---|   P     |   R$  9.00     |  R$ 11.00    |---")
print("---|   M     |   R$ 14.00     |  R$ 16.00    |---")
print("---|   G     |   R$ 18.00     |  R$ 20.00    |---")
print("-----------------------------------------------------")

#Lista de preços dos itens.
precos = {
    'CP': {'P': 9.00, 'M': 14.00, 'G': 18.00},
    'AC': {'P': 11.00, 'M': 16.00, 'G': 20.00}
}

# Acumulador do total
total = 0.0

while True:
    sabor = input("Entre com o sabor desejado (CP/AC): ").upper()
    if sabor not in ['CP', 'AC']:
        print("Sabor inválido. Tente novamente.")
        continue  # Verifica se o que usuário colocou é o que eu queria. Se sim ele continua.

    tamanho = input("Entre com o tamanho desejado (P/M/G): ").upper()
    if tamanho not in ['P', 'M', 'G']:
        print("Tamanho inválido. Tente novamente.")
        continue  # Verifica se o que usuário colocou é o que eu queria. Se sim ele continua.

    # Verificação do que o usuário respondeu. 
    if sabor == 'CP':
        if tamanho == 'P':
            preco = 9.00
        elif tamanho == 'M':
            preco = 14.00
        else:
            preco = 18.00
        print(f"Você pediu um Cupuaçu no tamanho {tamanho}: R$ {preco:.2f}")
    elif sabor == 'AC':
        if tamanho == 'P':
            preco = 11.00
        elif tamanho == 'M':
            preco = 16.00
        else:
            preco = 20.00
        print(f"Você pediu um Açaí no tamanho {tamanho}: R$ {preco:.2f}")

    total += preco


    # End do programa.
    mais = input("Deseja mais alguma coisa? (S/N): ").upper()
    if mais == 'S':
        continue  # vai direto para o próximo pedido
    elif mais == 'N':
        break  # sai do loop principal
    else:
        print("Resposta inválida. Encerrando por segurança.")
        break

# Exibe o total
print(f"\nO valor total a ser pago: R$ {total:.2f}")
