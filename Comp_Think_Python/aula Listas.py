'''
L = [1, 2, 3, 4, 5]
V = L[:] # O '[:]' serve para manter a lista antiga mesmo modificando a nova
V[0] = 6

print(V)
print(L)
'''


'''
#    POSICOES NA LISTA
#    0  1  2  3  4  5
L = [1, 2, 3, 4, 5, 6]

print(L[0:6])

if len(L) > 6:       # se o tamanho da lista for maior que 6
    print("deu")
'''

'''
L=[0]       # Lista sem valores

L.append("A")       # "Append" guarda uma informacao na lista
L.append("B")
L.append("C")
L.append("D")
L.append("E")

print(L)
'''

'''
L=[]

while True:
    num = int(input("Digite um numero {se digitar 0 ele para}:"))

    if num == 0:
        break
    L.append(num)

x = 0
while x < len(L):
    print(L[x])
    x += 1

L.sort() # Ordena os elementos da lista em ordem crescente
print(L)

L.sort(reverse=True) # Ordena os elementos da lista em ordem decrescente
print(L)

'''

'''
L = []
L.extend([1,2,3]) #adiciona elementos em uma lista
print(L)

L.append([4,5,6]) #adiciona uma lista dentro da outra lita
print(L)
'''

'''
# Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras

L = []
V = []

while True:
    add_L = int(input("adicione elementos a lista L, fim para terminar:"))

    if add_L == "fim":
        break
    L.append(add_L)



while True:
    add_V = int(input("adicione elementos a lista V, fim para terminar:"))

    if add_V == "fim":
        break
    V.append(add_V)

Z = []
Z.extend(L + V) # Junta duas listas em uma nova lista "Z"
print(Z)
'''
#     0    1    2   3   4   5
L = ["a", "b", "c","d","e","f"]


del L[0] # apaga o elemento "a" que está na posicao 0 da lista.
print(L)

#    0  1  2  3  4  5
V = [1, 2, 3, 4, 5, 6]
del V[2:6] # apaga os elementos da posiçao 2 até a posiçao 6
print(V)





