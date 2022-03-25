#Escreva um programa que converta uma temperatura digitada em ºC em ºF.
#A fórmula para essa conversão é F = ((9 x C) / 5) + 32

temperatura_c = float(input("temperatura °C:"))

valor_f = 9 * temperatura_c / 5 + 32
print(f"a conversao de {temperatura_c}°C para Fahrenheit é {valor_f}°F")
