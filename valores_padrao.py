def Saudacao(texto="mundo"):
    print(f"olá, {texto}")

def Saudacao2(nome,parte_dia="bom dia"):
    print(f"{parte_dia}, {nome}")


Saudacao()
Saudacao("joaquim")
Saudacao2(parte_dia="bom dia",nome="joaquim")
Saudacao2(parte_dia="boa tarde",nome="Maria")
Saudacao2(nome="joaquim")