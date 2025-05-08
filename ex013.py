print(f"\n Bem-Vindo ao AlugueCar\n")

def km():
    percorrido = float(input("Quantos kms foram percorridos com o carro alugado?"))
    dias = int(input("Por quantos dias você alugou?"))
    calculo_1 = dias * 60
    calculo_2 = percorrido * 0.15
    print(f"O valor que você nos deve é de R$ {calculo_1 + calculo_2}")

km()
