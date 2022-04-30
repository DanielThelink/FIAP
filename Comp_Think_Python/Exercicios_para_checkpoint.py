# Calculo de media de 3 alunos:
aluno = 1
continuar = "s"
while continuar == "s":
    print(f"ALUNO {aluno}----------------------------------")
    aluno + 1
    n1 = float(input("Digite a nota 1: "))
    if n1 >= 0 and n1 <= 10:
        n2 = float(input("Digite a nota 2: "))
        if n2 >= 0 and n2 <= 10:
            n3 = float(input("Digite a nota 3: "))
            if n3 >= 0 and n3 <= 10:
                menor = n1
                if n2 < menor:
                    menor = n2
                if n3 < menor:
                    menor = n3
                med = (n1 + n2 + n3 - menor) / 2
                if med >= 6:
                    print(f"Aprovado com media {med}")
                else:
                    if med < 4:
                        print(f"Reprovado direto com a media {med}")
                    else:
                        rec = float(input("Digite a nota de recuperação: "))
                        if rec >= 0 and rec <= 10:
                            media_final = (med + rec) / 2
                            if media_final >= 5:
                                print(f"Aprovado em recuperacao com a media {media_final}")
                            else:
                                print(f"Reprovado em recuperacao com a media {media_final}")
                        else:
                            print("Nota de recuperacao invalida")
            else:
                print("Nota 3 inválida")
        else:
            print("Nota 2 inválida")
    else:
        print("Nota 1 inválida")
    aluno += 1
    print("\n")

    continuar = input("Deseja continuar [s]im ou [n]ão ?")

    while not continuar == "s" or continuar == "S" or continuar == "n" or continuar == "N":
        print("Digite corretamente! S ou N")
        continuar = input("Deseja continuar [s]im ou [n]ão ?")

