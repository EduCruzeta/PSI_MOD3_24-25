# Eduardo Cruz N5 10T

def menu():
    pergunta = input("Consultar Taxas? (S/N): ")
    preco_do_produto = float(input("Preço do produto (Euros): "))
    convercao = input("Divisa (R/D/L/T): ")

    if pergunta in "Ss":
        print("""Taxas:
R -> 4,05
D -> 1,23
L -> 0,89
T -> 4,67""")
        
    preco_final = taxas(preco_do_produto,convercao)
    Nome_extenso(preco_final,convercao)


def taxas(preco_do_produto,convercao):
    if convercao in "Rr":
        preco_taxa = preco_do_produto * 4.05
        alfandega = preco_taxa * 0.10
        preco_final = preco_taxa + alfandega
        return preco_final

    if convercao in "Dd":
        preco_taxa = preco_do_produto * 1.23
        alfandega = preco_taxa * 0.10
        preco_final = preco_taxa + alfandega
        return preco_final

    if convercao in "Ll":
        preco_final = preco_do_produto * 0.89
        return preco_final

    if convercao in "Tt":
        preco_final = preco_do_produto * 4.67
        return preco_final
    
def Nome_extenso(preco_final,convercao):
    if convercao in "Rr":
        print(f"{round(preco_final,2)} Reais [Brasil]")
    if convercao in "Dd":
        print(f"{round(preco_final,2)} Dólares [EUA]")
    if convercao in "Ll":
        print(f"{round(preco_final,2)} Libras Esterlinas [UK]")
    if convercao in "Tt":
        print(f"{round(preco_final,2)} Turcas [Turquia]")


menu()