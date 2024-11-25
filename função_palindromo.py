
def palindromo(nome) -> bool:
    pinvertida =""
    nome = nome.lower() 

    for i in range(len(nome)-1,-1,-1):
        pinvertida = pinvertida + nome[i] 

    if nome == pinvertida:
        return True
    return False
    
def main():
    nome = input("insira o nome: ")
    palindromo(nome)
    if palindromo(nome) == True:
        print("É um palindromo")
    else:
        print("Não é palindromo")

if __name__=="__main__":
    main()