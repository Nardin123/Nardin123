# while

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


    
y = int(input("Digite um número ímpar"))

while y <= 0 or y % 2 == 0:
    y = int(input("Digite um número ímpar"))

print(f"Número ímpar válido: {y}. Programa encerrado.")

# FOR

for i in range(10, 0 - 1, -2):
    print(i)


frase = "Lógica de programção e Algoritmos"
for i in range(0, len(frase),1 ):
    print(frase[i], end=' ')

x = 0
y = 0

for i in range(0, 101):
        if i % 2 == 0:
            x += i
            y += 1 
media = x / y
print(f"A média entre {x} e {y} é {media}")

print(f"\n Bem-vindo a Mercearia\n")
print(f" O que temos hoje é:\n ")

print(f"Coxinha - R$ 5,00 ")
print(f"Pastel - R$ 5,00 ")
print(f"Café - R$ 5,00 ")
print(f"Suco - R$ 5,00\n ")


x = input(f"Qual produto deseja comprar?")
x = True

while x == True:
    
tabuada = 1
while tabuada <= 10:
    print(f'Tabuada do {tabuada}')
    i = 1
    while i <= 10:
        print(f'{tabuada} x {i} = {tabuada * i}')
        i += 1
    tabuada += 1

for tabuada in range(1, 11):
    print(f"Tabuada do {tabuada}")
    for i in range(1, 11):
        print(f"{i} x {tabuada} = {tabuada * i}")


