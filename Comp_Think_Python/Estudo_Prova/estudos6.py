#Escreva um programa que calcule o tempo de uma viagem de carro.
#Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia_percorrer = float(input("distancia em km:"))
velocidade_media = float(input("velocidade media km/h:"))

tempo =  distancia_percorrer / velocidade_media

print(f"com a distancia de {distancia_percorrer}km, o tempo de viagem será de {tempo}h" )
