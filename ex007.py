import random

comput = random.randint(1, 20)

contador = 3

print(f"Bem vindo ao game de hoje. Chute se o número é par ou ímpar")

while contador > 0:
    var = input("Adivinhe se o número é par ou ímpar").lower()

    if comput % 2 == 0 and var == "par":
        print("Você acertou!! ")
        break

    elif comput % 2 == 1 and (var == "ímpar") or (var == "impar"):
        print("Parabéns você acertou!!")
        break

    else:
        contador -= 1
        if contador > 1:
            print(f"Você errou!! Tente novamente, restam {contador} chances")
        else:
            print(f"Você errou todas as vezes, infelizmente acabaram suas chances, o número era {comput} e ele é {'par' if comput % 2 == 0 else 'impar'}")        