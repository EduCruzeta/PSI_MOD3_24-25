# Para testar a nossa função usamos o assert Ex:

from maior_de_2 import maior_dois

assert maior_dois(10,5) == 10, "A função devia devolver 10"
assert maior_dois(10,10) == None, "A função devia devolver None porque os Nº são iguais"

print("A função passou todos os testes")