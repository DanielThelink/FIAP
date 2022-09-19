'''
listas      = list()    | lista       = []
tupla       = tuple()   | tuple       = ()
dicionario  = dict()    | dicionario  = {}
'''

# ------- Definindo um dicionário préviamente preenchido
'''
dados = {
    'nome' : 'Edson de Oliveira',
    'idade': 48,
    'email':'edson@fiap.com.br',
    'fone' : '45645-6546'
}
'''
# print(dados)

# -------- Adicionando campos
# dados['fone'] = "(11) 94533-9345"
# print(dados)

# -------- Excluir campo
# del dados['idade']
# print(dados)

# -------- Exibindo o conteúdo dos campos do dicionário
'''
print(f"Nome..........: {dados['nome']}")
print(f"Idade.........: {dados['idade']}")
print(f"E-mail........: {dados['email']}")
print(f"Fone..........: {dados['fone']}")
'''

# --------- manipulando dicionarios
'''
# -------- Exibir o conteudo
# print(dados.values())

# -------- Exibir os campos
# print(dados.keys())

# -------- Exibir tudo
#print(dados.items())


# for k, v in dados.items():
#     print(f"O campo '{k}' tem o valor '{v}'")

# ----- Considerando o dicionario criado, fazer com que o usuario digite valores nos campos
'''
'''
# ------ Inserindo dados nos campos via usuário
def preencherDados(d):
    d['nome'] = str(input("Digite o seu nome: "))
    d['idade'] = int(input("Digite a idade: "))
    d['E-mail'] = str(input("Digite o seu email: "))
    d['fone'] = str(input("Digite o seu fone: "))


def exibirDados(d):
    print(f"Nome..........: {d['nome']}")
    print(f"Idade.........: {d['idade']}")
    print(f"E-mail........: {d['email']}")
    print(f"Fone..........: {d['fone']}")

# --------- PROGRAMA PRINCIPAL
preencherDados(dados)
exibirDados(dados)

#####################################################
# D E S A F I O :
# Consistir os dados antes de inserir nos campos
# - Se int, verificar se é numerico
# - Se vazio, obrigar o usuário a digitar algo
#####################################################
'''
# --------- Define a tabela (dicionario + lista)
pessoa = dict()
cadastro = list()

# --------- Insere linhas até que seja digitado '.'
while True:
    pessoa['nome'] = str(input('Nome: '))
    if pessoa['nome'] == '.': break
    pessoa['idade']= int(input('Idade: '))
    cadastro.append(pessoa.copy())

print("--------- Início da Listagem -------")
# --------- Exibir as linhas
for i in range(0, len(cadastro), 1):
    print(f"Nome....: {cadastro[i]['nome']}")
    print(f"Idade...: {cadastro[i]['idade']}\n")
print("--------- Final da Listagem -------")

############### D E S A F I O
# CRIE UM DICIONARIO COM 5 CAMPOS E ENVOLVA-O EM UMA LISTA (TABELA)
# - FAZER A CONSISTENCIA DOS DADOS
# - PREENCHER
# - EXIBIR

'''
# Replace (edita uma string
frase = "O Python é legal. mas meio doidão."
print(frase)
frase2 = frase.replace('.','!', 1)
print(frase)
print(frase2)
'''

"""
# Escolha (switch)
x = 33
match x:
    case 1:
        print("um")
    case 2:
        print("dois")
    case 3:
        print("tres")
    case 4:
        print("quatro")
    case _:
        print("Inválido")
"""

"""
# Operador or
# nome = input("Digite um nome: ")
# print(nome or "Digite algo")

v1 = 10
v2 = False
v3 = "eu"
v4 = "Achou!"
print(v1 or v2 or v3 or v4)
"""

"""
# Operador ternario
# EXEMPLO 1 - Sem atribuir a variáveis
idade = 19
#[var = ]<bloco True> if <condicao> else <bloco falso>

# exemplo 1 - Sem utilizar variavel
print("Maior de idade") if idade >= 18 else print("menor de idade")

if idade >= 18:
    print("Maior de idade")
else:
    print("menor de idade")

# utilizando variavel. Se uma venda for maior do que 1000 dar 10% de desconto, senao 5%
#[var = ]<bloco True> if <condicao> else <bloco falso>
venda = 3000

desconto = venda * 0.1 if venda > 1000 else venda * 0.05

print(desconto)

# utilizando variavel. Se uma venda for maior do que 1000 dar 10% de desconto, senao 5%.
# considerar o cupom de desconto
#[var = ]<bloco True> if <condicao> else <bloco falso>
venda = 3000
cupom = 50

desconto = cupom + (venda * 0.1 if venda > 1000 else venda * 0.05)
print(desconto)

venda = 3000
cupom = 50
if venda > 1000:
    desconto = venda * 0.1
else:
    desconto = venda * 0.05
desconto = desconto + cupom

# unário:   x++ | x+=4
# binario:  x + y
# ternário: .V. <cond> .F.
"""

# numero = input("Digite um numero: ")
# if numero.isnumeric():
#     numero = int(numero)
#
# else:
#     print("não corresponde a um numero")

# numero = input("Digite um numero: ")
# if numero.isdecimal():
#     print("Corresponde a um numero")
#
# else:
#     print("não corresponde a um numero")
