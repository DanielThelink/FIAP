num1 = int(input("Digite o primeiro numero:"))
num2 = int(input("Digite o segundo numero:"))
escolhacres = input("Digite [c]rescente ou [d]ecrescente:")
abertof = input("Digite o tipo de intervalo ([a]berto ou [f]echado:")
maior = num2

if num1 > maior:
    maior = num1

if escolhacres == "c" and abertof == "a"and maior == num1:
    for i in range(num2, maior + 1, 1):
         print(i)

elif escolhacres == "c" and abertof == "a":
    for i in range(num1,num2 + 1, 1):
         print(i)

if escolhacres == "c" and abertof == "f"and maior == num1:
    for i in range(num2 +1, maior, 1):
         print(i)

elif escolhacres == "c" and abertof == "f":
    for i in range(num1+1,num2, 1):
         print(i)

if escolhacres =="d" and abertof == "a" and maior == num1:
    for i in range(maior,num2 -1,-1):
         print(i)

elif escolhacres == "d" and abertof == "a":
    for i in range(num2,num1-1, -1):
         print(i)

if escolhacres == "d" and abertof == "f"and maior == num1:
    for i in range(maior-1, num2, -1):
         print(i)

elif escolhacres == "d" and abertof == "f":
    for i in range(num2-1,num1, -1):
         print(i)