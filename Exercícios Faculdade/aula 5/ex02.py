def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while x < min or x > max:
        x = int(input(pergunta))

    return x    
    
def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação')
    else:
        print(f'{nomeArquivo} criado com sucesso. \n')


def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir arquivo')
    else:
        a.write(f'{nomeJogo}; {nomeVideogame}')
    finally:
        a.close()


def listarArquivo(nomeARquivo):
    try:
        a = open(nomeARquivo, 'rt')
    except:
        print('Erro ao ler')
    else:
        print(a.read())
    finally:
        a.close()



#Programa principal
arquivo = 'gamex.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo não encontrado.')
    criarArquivo(arquivo)



while True:
    print('Menu')
    print('1 - cadastrar um novo item')
    print('2 - listar os cadastros')
    print('3 - sair')

    op = valida_int('Escolha a opção desejada: ', 1, 3)
    if (op == 1): #Novo item:
        print('Opção de cadastrar novo item selecionado')
        nomeJogo = input('Nome do jogo: ')
        nomeVideogame = input('Nome do videogame: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)

    elif (op == 2): #Listar
        print('Opção de Listar')
        listarArquivo(arquivo)

    elif (op == 3):
        print('Encerrando o programa....')
        break