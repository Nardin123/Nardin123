def valida_string(pergunta, min, max):
    s1 = input(pergunta)
    tam = len(s1)
    while ((tam < min) or (tam > max)):
        s1 = input(pergunta)
        tam = len(s1)
        return s1
# programa main

x = valida_string('Digite uma string: ', 10, 30)
print("Você digitou a string {x}. \n Dado válido. Close system.")


calc = lambda a, b: (a * 2) * b
print(calc(5, 2))