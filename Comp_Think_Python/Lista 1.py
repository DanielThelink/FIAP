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

Huguinho = 0
Zezinho = 0
Luizinho = 0

contador = "s"
while contador == "s":
        urna = int(input("Em quem vc deseja votar?[1, 2, 3]"))

        if urna == 1:
            Huguinho +=1

            if urna == 2:
                Zezinho +=1

                if urna == 3:
                    Luizinho +=1

        contador = input("Deseja continuar votando?")
        while not contador == "s" or contador == "S" or contador == "n" or contador == "N":
            print("Digite Sim ou Não corretamente.")
            contador = input("Deseja continuar? digite Sim ou Não?")

else:
    print("FIM DA VOTACAO")
    print(f"Huguinho tem {Huguinho} votos")
    print(f"Zezinho tem {Zezinho} votos")
    print(f"Luizinho tem {Luizinho} votos")
