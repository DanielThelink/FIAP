#1 - zoas

def BOMDIAAA_BOMDIAAA(nome):
    print(f"BOM DIAA BOM DIAA {nome}, a tropa do serrão te chamou para a piscina!")

BOMDIAAA_BOMDIAAA("Daniel")


# EXERCÍCIOS:
# 1. Crie um procedimento chamado "saudacao3" que passe como parâmetro uma MSG: "Bom dia", "Boa Tarde" ou "Boa noite"
# e um NOME e exiba a mensagem na tela:
# protótipo: saudacao3(msg, nome)
# Tela: Boa noite Edson, seja bem vindo a FIAP

def saudacao3 (msg,nome):
    print(f"{msg},{nome}, seja bem vindo a FIAP")

saudacao3("Boa noite","Daniel")


# 2. Crie um procedimento chamado "saudacao4" que passe como parâmetro uma HORA e um NOME e exiba a mensagem na tela:
# protótipo: saudacao4(16, nome)
# Tela: <Boa TARDE> <Edson>, seja bem vindo a FIAP
def saudacao4 (hora , nome):
    print(f" {hora}, {nome}, seja bem vindo a FIAP")


# 3. Crie um procedimento chamado "saudacao5" que passe como parâmetro uma HORA e um NOME deixando como padrão
# "Boa Noite" e "Edson" e exiba a mensagem na tela:
# protótipo 1: saudacao5(11, "Maria")
# Bom dia Maria, seja bem vindo a FIAP

# protótipo 2: saudacao5()
# Tela: Bom dia Maria, seja bem vindo a FIAP

# 4. Crie uma função que retorne o proximo número ao passado por parâmetro.
# protótipo: prox_num(5)
# Retorno: 6

def proxnum (num1):
    print(num1 + 1)

proxnum(5)

# 5. Crie uma função que retorne o maior entre dois números passados por parâmetro
# protótipo: maior_2n(15,98)
# Retorno: 98

def maiornum2 (num1,num2):
    print(max(num1,num2))

maiornum2(10,11)

# 6. Crie uma função que retorne o maior entre três números passados por parâmetro
# protótipo: maior_3n(115,23,8)
# Retorno: 115

def maiornum3 (num1,num2,num3):
    print(max(num1,num2,num3))

maiornum3(10,11,12)

# 7. Crie uma função que retorne o próximo numero multiplo 5 tomando como base o que foi passado por parâmetro.
# protótipo: prox_mult5(13)
# Retorno: 15

def calc (n):
    for i in range (1,n+1):
        if n % 5 == 0:
            print(n)

    else:
        return

calc(13)