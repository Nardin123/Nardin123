print(f"Bem-vindo à loja do Felippe M. M. Nardin") # Nome da minha loja

def desconto_calc():
    unit_value = float(input(f"Entre com o valor do produto: ")) # variáveis que solicitam a informação do usuário referente ao valor do produto.
    prod_quan = int(input(f"Entre com a quantidade do produto: ")) # variáveis que solicitam a informação do usuário a quantidade do produto. 

    total_s_desconto = unit_value * prod_quan 

    if total_s_desconto < 2500: # condição que verifica se é menor que 2500 
        desconto = 0 # variável que recebe 0 % 
    elif 2500 <= total_s_desconto < 6000: # condição que verifica se é maior ou igual a 2500 e menor que 6000
        desconto = 4 # variável que recebe 4 % 
    elif 6000 <= total_s_desconto < 10000: # condição que verifica se é maior ou igual a 6000 e menor que 10000
        desconto = 7
    else:
        desconto = 11 # se não enquadrar nas demais, entra nela

    valor_desconto = total_s_desconto * desconto / 100 # calcula a % 
    total_c_desconto = total_s_desconto - valor_desconto # calcula o total com desconto

    print(f"O valor SEM desconto: R${total_s_desconto:.2f}") # resultados.
    print(f"O Valor COM desconto: R${total_c_desconto:.2f}") # resultados. 

desconto_calc()
