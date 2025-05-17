
print("Bem vindo à Livraria do Felippe Nardin")
print("-" * 56)

# Lista de livros (cada livro será um dicionário dentro dessa lista)
lista_livro = []

# Variável global para controlar o ID dos livros
id_global = 0

# Função para cadastrar um novo livro
def cadastrar_livro(id):
    print("-" * 20, "MENU PRINCIPAL", "-" * 20)
    print("MENU CADASTRAR LIVRO")
    print(f"Id do livro: {id}")
    nome = input("Por favor entre com o nome do livro: ")
    autor = input("Por favor entre com o autor do livro: ")
    editora = input("Por favor entre com a editora do livro: ")

    # Dicionário com as infos do livro
    livro = {
        "id": id,
        "nome": nome,
        "autor": autor,
        "editora": editora
    }

    # Adiciona o livro na lista
    lista_livro.append(livro)
    print("Livro cadastrado com sucesso!")

# Função para consultar livros
def consultar_livro():
    while True:
        print("-" * 20, "MENU PRINCIPAL", "-" * 20)
        print("MENU CONSULTAR LIVRO")
        print("1 - Consultar Todos os Livros")
        print("2 - Consultar por Id")
        print("3 - Consultar por Autor")
        print("4 - Retornar ao menu")
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            # Consulta todos os livros
            for livro in lista_livro:
                print(f"id: {livro['id']}")
                print(f"nome: {livro['nome']}")
                print(f"autor: {livro['autor']}")
                print(f"editora: {livro['editora']}")
                print("-" * 40)

        elif opcao == "2":

            # Consulta por ID
            try:
                id_livro = int(input("Digite o ID do livro: "))
                encontrado = False
                for livro in lista_livro:
                    print("-" * 40)

                    if livro["id"] == id_livro:
                        print(f"id: {livro['id']}")
                        print(f"nome: {livro['nome']}")
                        print(f"autor: {livro['autor']}")
                        print(f"editora: {livro['editora']}")
                        print("-" * 40)

                        encontrado = True
                if not encontrado:
                    print("Livro não encontrado.")
            except:
                print("ID inválido.")

        elif opcao == "3":

            # Consulta por autor
            autor = input("Digite o nome do autor: ")
            encontrados = [livro for livro in lista_livro if livro["autor"].lower() == autor.lower()]
            if encontrados:
                print("-" * 40)
                for livro in encontrados:
                    print(f"id: {livro['id']}")
                    print(f"nome: {livro['nome']}")
                    print(f"autor: {livro['autor']}")
                    print(f"editora: {livro['editora']}")
                    print("-" * 40)
            else:
                print("Nenhum livro encontrado com esse autor.")

        elif opcao == "4":
            break
        else:
            print("Opção inválida.")

# Função para remover livro pelo ID
def remover_livro():
    while True:
        try:
            id_livro = int(input("Digite o ID do livro a remover: "))
            for livro in lista_livro:
                if livro["id"] == id_livro:
                    lista_livro.remove(livro)
                    print("Livro removido com sucesso!")
                    return
            print("ID inválido.")
        except:
            print("Entrada inválida. Digite um número.")

# Menu principal (LEMBRETE: USUÁRIO NARDIN // PARA O LAYOUT EU TESTEI SOMENTE COM 20 '-'. PROJETO INTERESSANTE PARA TENTAR APLICAR PySider6 (tentar depois))
while True:
    print("-" * 20, "MENU PRINCIPAL", "-" * 20)
    print("MENU PRINCIPAL")
    print("1 - Cadastrar Livro")
    print("2 - Consultar Livro(s)")
    print("3 - Remover Livro")
    print("4 - Sair")

    opcao = input("Escolha a opção desejada: ")

    if opcao == "1":
        id_global += 1
        cadastrar_livro(id_global)

    elif opcao == "2":
        consultar_livro()

    elif opcao == "3":
        remover_livro()

    elif opcao == "4":
        print("Encerrando o programa... Até logo!")
        break

    else:
        print("Opção inválida.")
