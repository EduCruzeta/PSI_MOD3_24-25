"""
Este programa vai fazer de restaurante com um menu 1. Entrada 2. Saída 3. Estado 4.Terminar 
cada vez que entrar alguem pergunta quantas pessoas sao e quantas mesas ocupam cada vez que sai pergunta o preço 
"""
from utils import ler_numero_inteiro
from utils import ler_numero_decimal

def Menu():
    op = 0
    while op != 4:
        print("""
        1. Entrada
        2. Saída
        3. Estado
        4. Terminar
        """)

        escolha = ler_numero_inteiro("escolha: ")
        if escolha == 1:
            Entrada()
        elif escolha == 2:
            Sair()
        elif escolha == 3:
            Estado()
        elif escolha == 4:
            op = 4
        else:
            print("Erro: Escolha inválida tente novamente")
def configurar():
    """
    Função para definir a configuração do restaurante (nº mesas e nº de clientes)
    """
    global mesas
    global clientes

    mesas = ler_numero_inteiro("Insira o número de mesas do restaurante: ")
    clientes = ler_numero_inteiro("Insira o número de clientes que o restaurante pode acomudar: ")


def Entrada():
    """
    Esta função vai perguntar o número de pessoas que entram e o numero de mesas ocupadas
    """
    global mesas
    global clientes
    global mesas_ocupadas
    global n_clientes

    mesas_ocupadas = ler_numero_inteiro("Insira o número de mesas que vão ser ocupadas: ")
    n_clientes = ler_numero_inteiro("Insira o número de clientes que vão entrar: ")

    if mesas_ocupadas < mesas:
        mesas = mesas - mesas_ocupadas
    if n_clientes < clientes:
        clientes = clientes - n_clientes

def Sair():
    """
    Resposável por registar a saída dos clientes e atualizar o custo total das refeições
    """
    global mesas
    global clientes
    global saldo
    global mesas_ocupadas
    global n_clientes

    temp = 1
    if temp == 1:
        saldo = 0
        temp == 2

    while True:
        mesas_desocupadas = ler_numero_inteiro("Insira as mesas que foram desocupadas: ")
        if mesas_desocupadas > mesas_ocupadas:
            print("Valor inválido.")
            continue
        saida_clientes = ler_numero_inteiro("Insira o numero de clientes que sairam: ")
        if saida_clientes > n_clientes:
            print("Valor inválido.")
            continue
        pagar = ler_numero_decimal("Insira o preço a pagar pelas pessoas que sairam: ")

        mesas = mesas + mesas_desocupadas
        clientes = clientes + saida_clientes
        saldo = saldo + pagar
        break

def Estado():
    """
    Calcula e mostra os dados estatísticos do restaurante
    """
    global mesas
    global clientes
    global saldo

    print("Tem cerca de",mesas,"mesas livres.")
    print("Tem cerca de",clientes,"lugares livres.")
    print("O saldo atual é de", saldo,"€")



configurar()
Menu()

