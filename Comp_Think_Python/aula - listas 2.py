#  indice :[  0     1     2    3      4   ]
# lista =   [4.5,   6,  True, "@", "Daniel"]
#  indice :[ -5    -4    -3   -2     -1   ]
# print(lista)
# print(lista[1:4], lista[-4:-1])


# l1 = [1,2,3,4]
# l2 = [5,6,7,8]
# l3 = l1 + l2
#
# print(f"lista1 {l1}\n, lista2 {l2}\n, lista3 {l3}")
#
# "extend" extende a primeira lista com a segunda lista
# l1.extend(l2)
# print(l1)

# append acrescenta um valor e o salva no final da lsita
# lista = [1]
# lista.append(2)
# print(lista)

# o insert permite editar um elemento : l3.insert(indice,conteudo)
# l3 = [1,2,3]
# l3.insert(1,1.5)
# print(l3)

#ex de uso do insert:
# x = input("digite um valor:")
# l3 = [1,4,5]
# l3.insert(1,x)
# print(l3)

# min() e max() retornam o menor e o maior item da lista respectivamente. print (min(1), max(13))
# lista = [4,8,9,13,1]
# print (lista)
# print(f"maior valor:{max(lista)}\nmenor valor:{min(lista)}")

# colocando o maior valor de uma lista em uma variavel
# maior_valor = max(lista)
# print(maior_valor)

# o pop remove o ultimo elemento de uma lista. lista.pop()
# lista =[1,2,3,4]
# lista.pop()
# print(lista)

# o del remove um ou mais elementos da lista. del(lista[elemento])
# lista = [4,8,9,13,5]
# del(lista[1:3]) # remove o "8" e o "9" da lista
# print(lista)

# o clear apaga todos os elementos da lista. lista.clear
# lista = [4,8,9,13,5]
# print(lista)
# lista.clear()
# print(lista)

# EXEMPLOS GERAIS:

# 1 - preencher uma lista com 5 elementos com dados fornecidos pelo usuario

# listanome=[]
# for i in range (0,5):
#
#     nomeadd = input(f"Digite seu {i} nome aqui:")
#     listanome.append(nomeadd)
#
# print(f"{listanome}")

#  indice :[  0     1     2    3     4]
# lista =   [30,  455,  124, 899, 27]
#
# for elem in lista:
#     print(elem)

# 10. Digitar elementos em uma lista até que seja digitado [f]im.
#     Somar os elementos e calcular a media
#         ENTRADA: 5 3 4 9 f  SAÍDA: Soma: 21 media: 4.8
#         REQUISITO: Utilizar o while

lista = []
soma = 0
continuar = "s"
while continuar == "s":

    x = int(input("Digite um valor"))
    lista.append(x)

    continuar = input("Deseja continuar [S]im ou [N]ao")

    if continuar == "s":
        continuar = "s"

    else:
        break

for elem in lista:
    soma += elem
    soma = sum(lista)

print(soma)