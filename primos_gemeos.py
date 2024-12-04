"""
Dois numeros primos gemeos são dois nº primos que distam em 2 unidades um do outro
p.ex:
    3 e 5
    5 e 7
Fazer um programa que lê dois nº inteiros positivos do utilizador e diz se são primos e primos gémeos
"""
from função_primos import Numero_primos
from utils import ler_numero_inteiro

n1 = int(input("insira o numero: "))
n2 = int(input("insira o numero: "))

if Numero_primos(n1) and Numero_primos(n2):
    diferenca = n1 - n2
    if abs(diferenca) == 2:
        print(f"Os valores {n1} e {n2} são primos gémeos")
    else:
        print(f"Os valores {n1} e {n2} são primos apenas")
else:
    if Numero_primos(n1):
        print(f"O valor {n1} é primo")
    elif Numero_primos(n2):
        print(f"O valor {n2} é primo")
    else:
        print ("Nenhum dos valores é primo")