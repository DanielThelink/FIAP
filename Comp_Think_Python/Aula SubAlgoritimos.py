def Saudacao ():
    print ("Seja bem-vindo à FIAP")


# Exemplo 2 - Procedimento com parâmetro
def saudacao2(nome):
    print (f"{nome},seja bem-vndo à FIAP")

# Exemplo 3 - Procedimento com mais de um parâmetro
def flor(tipo, cor):
    print (f"A cor da {tipo} é {cor}")

# Exemplo 4 - Procedimento com parâmetros padrões
def flor2(tipo = "Rosa", cor = "Vermelha"):
    print (f"A cor da {tipo} é {cor}")


# PROGRAMA PRINCIPAL
Saudacao()
saudacao2("Maria")

flor("Rosa","Vermelha")
flor2("margarida")