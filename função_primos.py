
def Numero_primos(numero) -> bool:
    """esta função indica se o numero é primo
    true = primo
    false = não é primo"""
    primo = True

    for n in range(2,numero):
        if numero % n == 0:
            primo = False
            break
    
    if primo == True:
        return(primo)
    else:
        return(primo)
    

#def main():
    #numero = int(input("insira o seu numero:"))
    #Numero_primos(numero)
    #resultado = Numero_primos(numero)
    #print(resultado)

#if __name__=="__main__":
    #main()