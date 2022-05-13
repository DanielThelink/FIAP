# Teoria dos comandos

n1 = input("Digite o primeiro numero:")
n2 = input("Digite o segundo numero:")
n3 = input("Digite o terceiro numero:")
#
# if n1 < n2 and n1 < n3:
#     print(n1)
#
# elif n2 < n1 and n2 < n3:
#
#     print(f"{n2}")
#
# else:
#     print(n3)

#-----------------------------

# maior = n1
#
# if n2 > maior:
#     maior = n2
#
# if n3 > maior:
#     maior = n3

# print (maior)

if n1<n2:
    if n1<n3:
        print(n1)
    else:
        print(n3)
else:
    if n2<n3:
        print(n2)
    else:
        print(n3)