#TABUADA

# mandante = int(input("Digite um numero para saber a tabuada:"))
#
# for multiplo in range (1,11,1):
#
#     conta = mandante * multiplo
#     print(f"{mandante}X{multiplo}=",conta)

# SOMA (NAO TERMINEI....F)
# contador = 1
# numeroSoma = int(input("Digite um numero:"))
#
#
# while contador ==  1:
#
#     novoNumero = int(input("Digite um novo numero ou digite [0] para terminar:"))
#     soma = novoNumero + numeroSoma
#     print(soma)

#Urna eletronica

# Huguinho = 0
# Zezinho = 0
# Luizinho = 0

# contador = "s"
# while contador == "s":
#         urna = int(input("Em quem vc deseja votar?[1, 2, 3]"))
#
#         if urna == 1:
#             Huguinho +=1
#
#         elif urna == 2:
#             Zezinho +=1
#
#         elif urna == 3:
#             Luizinho +=1
#
#         contador = input("Deseja continuar votando?")
#
# else:
#     print("FIM DA VOTACAO")
#     print(f"Huguinho tem {Huguinho} votos")
#     print(f"Zezinho tem {Zezinho} votos")
#     print(f"Luizinho tem {Luizinho} votos")

# Treinamento Perceptron (formula).
    #entradas
x1 = 25
x2 = -19
x3 = 4
x4 = -3

    #pesos
w1 = 0.8
w2 = 0.3
w3 = -1.1
w4 = -0.9

b = 0.1

conta = x1 * w1 + x2 * w2 + x3 * w3 + x4 * w4 + b

print(conta)