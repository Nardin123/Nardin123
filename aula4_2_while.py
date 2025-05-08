while True:
    nome = input('Login: ')
    if nome != 'Felippe':
        continue 

    senha = input('Senha: ')
    if senha == '1234':
        break
        

print("Seja bem vindo") 


name = ''

while not name:
    name = input(f"Digite o seu nome: ")