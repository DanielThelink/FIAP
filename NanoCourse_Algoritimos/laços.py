# for i in range (1,11,1):
#     print(i)


p = int(input("Digite o numero final:"))
soma = 0
for n in range (1,p,1):
    print(f"Digite um numero {n}º")
    c = int(input())
    soma = soma + c

print(soma)