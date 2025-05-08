

def payday():
    ask = float(input("Qual é o seu salário?"))
    calc = ask * 0.15
    print(f"O seu salário com reajuste é de R${ask + calc:.2f}")

payday()