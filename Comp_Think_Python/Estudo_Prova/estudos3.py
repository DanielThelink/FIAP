#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
#Calcule o total em segundos.
dias = int(input("Dias:"))
horas = int(input("horas:"))
minutos = int(input("minutos:"))
segundos = float(input("segundos:"))

total_segundos = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos

print(f"o valor total em segundos é de: {total_segundos}")