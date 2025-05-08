
def sistema():

    while True:
        try:
            num = int(input("Diga um número entre 1 e 10"))

            if num in range(0,11):
                print(f"Seu número é {num}")
                break
           
        except ValueError:
            print("Isso não é um número entre 1 e 10 moço")


sistema()