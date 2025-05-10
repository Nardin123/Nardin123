
# Meu programa
print(f"Essa é venda do Nardin\n")

print(f"Coxinha - R$ 5,00")
print(f"Pastel  - R$ 7,00")
print(f"Café - R$ 4,00")
print(f"Suco - R$ 6,00")

produtos = ['Coxinha', 'Pastel', 'Café', 'Suco']

while True:
    pergunta = input(f"Deseja comprar alguma coisa?")

    if pergunta.lower() == 'sim':
        print(f"{produtos}")

        pergunta_2 = input(f"Qual produto deseja?")

        if pergunta_2.lower() in [p.lower() for p in produtos]:
            qtd = input(f"Qual a quantidade de deseja comprar de {pergunta_2}")
            print(f"Será separado para você {qtd} {pergunta_2} ")
            break
        else:
            print('Infelizmente não conheço esse produto.')          


    elif pergunta == 'nao' :
        print(f"Obrigado, volte sempre")  
        break

    else:
        print(f"Isso não é uma caractere aceitável")

                    


# Programa faculdade:

print(f"Essa é venda do Nardin\n")

print(f"Coxinha - R$ 5,00")
print(f"Pastel  - R$ 7,00")
print(f"Café - R$ 4,00")
print(f"Suco - R$ 6,00")

valor = 0 

while True:
    o = int(input("Qual item deseja comprar?" ))
    a = int(input("Quantas unidades deseja levar? "))
        
    if o == "1":
        total = total + a * o
    elif o == "2":
        total = total + a * o
    elif o == "3":
        total = total + a * o
    elif o == "4":
        total = total + a * o
    elif o == "5":
        break
    else:
        print("Esse comando não é permitido")

print(f"VocÊ comprou {o} ")
