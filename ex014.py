
nota = float(input("Digite a sua nota para verificar sua situação: "))

def estudos():
    if nota >= 90:
        print(f"Sua nota é excelente! Está aprovado.")
    elif nota >= 70 or nota < 90:
        print(f"Está aprovado!")
    elif nota < 70:
        print(f"Está reprovado!")

estudos()



