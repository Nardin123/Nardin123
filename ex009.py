

print(f"\nSeja bem-vindo ao sistema!!\n")

area_um = float(input("Qual a altura dá área?"))
area_dois = float(input("Qual a largura dá área"))

total = area_um * area_dois

print(f"Nessa área você tem um total de : {total} m² e gastará : {total / 2}L de tinta.")




def calcular_tinta():
        altura = float(input("Qual a altura dá área?"))
        largura = float(input("Qual a largura dá área?"))
        total2 = altura * largura

        return(f"Nessa área você tem um total de : {total2} m² e gastará : {total2 / 2}L de tinta.")

print(calcular_tinta)