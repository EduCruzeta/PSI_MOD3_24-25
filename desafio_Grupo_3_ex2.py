"""
2. Função que recebe 3 valores e devolve o maior, caso sejam todos positivos, 
caso os valores sejam negativos dele devolver o menor. Nas restantes situações devolve None
"""

def funcao2(v1,v2,v3):
    maior = 0
    menor = 0
    if v1 >= 0 and v2 >= 0 and v3 >= 0:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        if v3 > maior:
            maior = v3

        return maior
    elif v1 < 0 and v2 < 0 and v3 < 0:
        if v1 < v2:
            menor = v1
        else:
            menor = v2
        if v3 < menor:
            menor = v3
        
        return menor
    
    else:
        return None
    

print(funcao2(-1,-5,-9))