# Eduardo Cruz nº5 10ªT
# Exercício de Funções em Python
# Complete cada função conforme indicado na docstring.
from datetime import datetime
import math
import time


def imprimir_dobro(valor):
    """Recebe um número e imprime o seu dobro."""
    
    valor_dobro = valor * 2
    print(valor_dobro)
	
def calcular_media_tres_numeros(n1, n2, n3):
    """
    Calcule a média aritmética de três números.
    Retorne o valor da média.
    """
    media = n1 + n2 + n3
    media = media / 3
    return media
	
def calcular_fatorial(numero):
    """Recebe um número inteiro positivo e retorna o seu fatorial.
	    Fatorial de 5 (5!) = 5 * 4 * 3 * 2 * 1
	"""
    fatorial = 1
    for i in range(1,numero+1):
        fatorial = fatorial * i
    return fatorial
        
def converter_celsius_para_fahrenheit(celsius):
    """
    Converta a temperatura de Celsius para Fahrenheit.
    Fórmula: (°C × 9/5) + 32 = °F
    """
    fah = (celsius * 9/5) + 32
    print(fah)

def calcular_area_circulo(raio):
    """
    Calcule a área de um círculo dado o raio.
    Use pi = 3.14159
    """
    if raio > 0:
        area = math.pi * raio ** 2
        area = round(area,2)
        return area
    else:
        return None 

def exibir_contagem_regressiva(inicio):
    """Recebe um número e imprime uma contagem regressiva até 0."""
    for i in range(inicio,-1,-1):
        time.sleep(1)
        print (i)
    
def inverter_string(texto):
    """
    Receba uma string e retorne ela invertida.
    Exemplo: "python" -> "nohtyp"
    """
    invertido = ""

    for i in range(len(texto)-1,-1,-1):
        invertido = invertido + texto[i]
        return invertido

def verificar_divisibilidade(a, b):
    """Recebe dois números e imprime se o primeiro é divisível pelo segundo."""
    resto = a % b
    if resto > 0:
        print("É divisivel")
    else:
        print("Não é divisivel")

def calcular_perimetro_circulo(raio):
    """Recebe o raio de um círculo e retorna o seu perímetro."""
    perimetro = 2 * math.pi * raio
    return perimetro

def converter_segundos_para_minutos(segundos):
    """Recebe um valor em segundos e retorna o correspondente em minutos."""
    minutos = segundos //  60
    segundos_rest = segundos % 60
    return f"{minutos}:{segundos_rest}"
    
def gerar_saudacao_periodo():
    """
    Retorne uma saudação baseada no período do dia.
    Se for antes de 12h: "Bom dia!"
    Entre 12h e 18h: "Boa tarde!"
    Após 18h: "Boa noite!"
    """
    hora_atual = datetime.now().strftime("%H")
    
    if hora_atual < "12":
        return ("bom dia!")
    elif hora_atual > "12" and hora_atual < "18":
        return ("boa tarde!")
    elif hora_atual > "18":
        return ("boa noite!")
	
def calcular_desconto(preco, percentual):
    """Recebe um preço e um percentual de desconto e retorna o preço com desconto."""
    percentual = percentual / 100
    preco_desconto = preco * percentual
    return preco_desconto
    
def calcular_velocidade_media(distancia, tempo):
    """Recebe a distância percorrida e o tempo gasto e retorna a velocidade média."""
    media = distancia / tempo
    return media

def verificar_palindromo(palavra):
    """
    Verifique se a palavra recebida é um palíndromo.
    Palíndromo é uma palavra que pode ser lida igual de trás para frente.
    Exemplo: "radar" é um palíndromo.
    """
    pinvertida =""

    for i in range(len(palavra)-1,-1,-1):
        pinvertida = pinvertida + palavra[i] 

    if palavra == pinvertida:
        return("É um palindromo")
    else:
        return("Não é um palindromo")
    



