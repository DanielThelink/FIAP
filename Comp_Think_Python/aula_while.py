'''
x= 0

while x<100:
    x=x+1
    print(x)
'''
'''
x= 49

while x < 100:

    x = x + 1
    print(x)
'''

'''
contagem = 11

while contagem >= 1:
    contagem = contagem - 1
    print(contagem)

else:

    print("FOGO!")
'''
'''
fim = int(input("Digite o numero:"))


x= 0

while x <= fim:
    x += 1
    print(x)
'''


'''
NUMERO IMPAR

num_usuario = int(input("Digite seu numero impar:"))

x = 1
while num_usuario>x:
    x = x + 2
    print(x)
'''
'''
x = 3

while x <= 30:
    print(x)
    x+= 3
'''
'''
#Tabuada

num = int(input("Tavuada do:"))

contador = 1

while contador <=10:

    tabuada = num * contador

    print(tabuada)

    contador += 1
'''
'''
# TABUADA BONITA

num = int(input("Tabuada do:"))

contador = 1

while contador <=10:

    tabuada = num * contador

    print(f"{num} X {contador}=",tabuada)

    contador += 1
'''
'''
# USUARIO DIGITA O INICIO E O FIM DA TABUADA

num = int(input("Tabuada do:"))

contador = int(input("inicio de tabuada:"))
final = int(input("fim:"))

while contador <=final:

    tabuada = num * contador
    print(f"{num} X {contador}=", tabuada)
    contador += 1
'''
#8
'''
deposito_inicial = float(input("Digite o valor do deposito no mes:"))
taxa_juros = float(input("Taxa de Juros %:"))
mes = 1

saldo = deposito_inicial

while mes <= 24:
    saldo = saldo + saldo * (taxa_juros/100)
    print(f"saldo do mes {mes} é igual a R$ {saldo:.2f}")
    mes += 1
print(f"O ganho total dos meses é: {saldo:.2f} ")
'''

#9 alterando para perguntar o deposito mensal
'''
deposito_inicial = float(input("Digite o valor do deposito no mes:"))
deposito_mensal = float(input("Digite o valor do deposito mensal:"))
taxa_juros = float(input("Taxa de Juros %:"))
mes = 1

saldo = deposito_inicial

while mes <= 12:
    saldo = saldo + (saldo + deposito_mensal) * (taxa_juros/100)
    print(f"saldo do mes {mes} é igual a R$ {saldo:.2f}")
    mes += 1
print(f"O ganho total dos meses é: {saldo:.2f} ")
'''

# funcao Break
'''
soma = 0
while True:
    num = int(input("Digite um numero para somar ou 0 para sair:"))
    if num == 0:
        break
    soma += num # apos digitar 0 ele para o codigo e faz a soma da variavel "num"
print(f"Soma ={soma}")
'''
#POSICAO  0 1 2 ...
'''
Lista1 = [1,2,3]

print(Lista1) #printa a lista inteira

print(Lista1[2]) #printa o terceiro elemento da lista

Lista1[0] = 10 #muda o valor do primeiro elemento da lista para 10

'''
'''
notas = [6,7,5,8,9]
soma = 0
x = 0 # 0 porque comeca na posicao 0 da lista que seria a do "6"

while x < 5: # na ultima rodagem ele entra como valor 4
    soma += notas[x]
    x += 1 # e aqui ele soma o valor 4 com 1 e ele sai 5

print(f"Media = {(soma/x):.2f}") #aqui ele ja soma o valor 5 de x
'''

notas = [0,0,0,0,0]
posicao_lista = ["Primera","Segunda","Terceira","Quarta","Quinta"]
soma = 0
x = 0

while x < 5:
    notas[x] = float(input(f"{posicao_lista[x]} Nota ="))
    soma = soma + notas[x]
    x += 1

print(f"Media = {(soma/x):.2f}")



