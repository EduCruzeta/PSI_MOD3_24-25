#Completa a função de acordo com a docstring
def ClassificaAluno(nota):
    """
    Recebe um nº inteiro positivo com a nota do aluno (0 a 20)
    Parâmetro:
        n: nº inteiro positivo
    Devolve:
        string com a palavra Aprovado se a nota é maior ou igual a 10
        string com a palavra Reprovado se a  nota é menor que 10
        None se a nota não é válida
    """
    if nota >= 0 and nota <= 20:
        if nota >= 10:
            return "Aprovado"
        elif nota < 10:
            return "Reprovado"
    else:
        return None   
#Testes
assert ClassificaAluno(2) == "Reprovado","Erro a função devia devolver Reprovado"
assert ClassificaAluno(10) == "Aprovado","Erro a função devia devolver Aprovado"
assert ClassificaAluno(20) == "Aprovado","Erro a função devia devolver Aprovado"
assert ClassificaAluno(0) == "Reprovado","Erro a função devia devolver Reprovado"
assert ClassificaAluno(21) == None,"Erro a função devia devolver None"
assert ClassificaAluno(-21) == None,"Erro a função devia devolver None"

print("Função passou nos testes")