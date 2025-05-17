
def escolha_servico(): # função que verifica o tipo de serviço.
        while True:
            print('DIG - Digitalização')
            print('ICO - Impressão colorida')
            print('IPB - Impressão Preto e Branco')
            print('FOT - Fotocópia')
            servico = input(">>").lower()

            if servico == "dig":
                  return 1.10
            elif servico == 'ico':
                  return 1.00
            elif servico == 'ipb':
                  return 0.40
            elif servico == 'fot':
                  return 0.20
            else:
                  print("Escolha inválida, entre com o tipo do serviço novamente. \n")

def num_pagina(): # função que verifica a quantidade de página
    while True:
        try:
            num = int(input("Entre com o número de páginas: "))
            if num >= 20000:
                print("Não aceitamos tantas páginas de uma vez.")
                print("Por favor, entre com o número de páginas novamente.\n")
            elif num >= 2000:
                return num * 0.75
            elif num >= 200:
                return num * 0.80
            elif num >= 20:
                return num * 0.85
            elif num > 0:
                return num
            else:
                print("Digite um número positivo de páginas.")
        except ValueError: # tratativa caso não caisa nas condições acima
            print("Valor inválido! Digite um número inteiro.\n")

def servico_extra():
    while True:
        print("Deseja adicionar algum serviço?")
        print("1 - Encadernação Simples - R$ 15.00")
        print("2 - Encadernação Capa Dura - R$ 40.00")
        print("0 - Não desejo mais nada")
        escolha = input(">>")

        if escolha == "1":
            return 15.00
        elif escolha == "2":
            return 40.00
        elif escolha == "0":
            return 0.00
        else:
            print("Opção inválida! Tente novamente.\n")

# Código main
print("Bem vindo a Copiadora do Felippe Nardin\n")

# "Puxa" o valor da função do serviço escolhido
valor_servico = escolha_servico()

# "Puxa" o número de páginas com desconto já aplicado
num_paginas_com_desconto = num_pagina()

# "Puxa" o valor extra (encadernação)
valor_extra = servico_extra()

# Calcula o total
total = (valor_servico * num_paginas_com_desconto) + valor_extra

# Mostra o resultado
print(f"\nTotal: R$ {total:.2f} (serviço: {valor_servico:.2f} * páginas: {num_paginas_com_desconto:.0f} + extra: {valor_extra:.2f})")