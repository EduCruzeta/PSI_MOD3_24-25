#esta funcao vai devolver o maior numero deles os dois

def maior_dois(v1,v2) -> bool:
    """A função vai receber dois números e dizer qual deles é o maior"""
    if v1 < v2:
        return v2
    elif v2 < v1:
        return v1
    
    return None
    


def main():
    v1 = float(input("insira o primeiro valor: "))
    v2 = float(input("insira o primeiro valor: "))
    maior_dois(v1,v2)
    print(maior_dois(v1,v2))

if __name__=="__main__":
    main()