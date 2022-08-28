
def Menu():

    print("################################# MENU #################################")
    
def peganumero(lista):
    for valor in range(0,3,1):

        numero = float(input(f"Digite o numero {valor+1} aqui:"))
        lista.append(numero)
    return lista
    
def verificaTriangulo (lista):

    if len(set(lista)) == 1:
        
        return print("O triangulo é Equilatero")

    elif len(set(lista)) == 2:
        return print("O triangulo é Isósceles")

    else:
        return print("O triangulo é Escaleno")


while True:
    Menu()
    opcao = int(input("Digite 1 para continuar e 2 para parar:"))
    if opcao == 1:
        listanum = []
        print(peganumero(listanum))        
        verificaTriangulo(listanum)
            
    elif opcao == 2:
        break  

    else:
        print ("opcao errada, por favor digite a opcao correta")
        
