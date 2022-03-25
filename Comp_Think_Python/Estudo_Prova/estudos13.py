#Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
#Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.

distancia_percorrida = float(input("Distancia:"))

if distancia_percorrida <= 200:

    preco_menor = 0.50 * distancia_percorrida
    print(f"sua distancia é menor que 200km/h entao voce irá pagar R${preco_menor}")
else:
    preco_maior = 0.45 * distancia_percorrida
    print(f"sua distancia é maior que 200hm/h entao voce irá pagar R${preco_maior}")