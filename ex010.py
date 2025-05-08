
def desconto():
    item = float(input("Qual é o preço do produto?"))
    total2 = item * 0.05
    total3 = new_func(item, total2)
    print(f"O valor total aplicando 5% de desconto é: {total3}")

def new_func(item, total2):
    total3 = item - total2
    return total3

desconto()                                                                                              