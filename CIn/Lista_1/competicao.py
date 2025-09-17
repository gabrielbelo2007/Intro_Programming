part_1 = input()
part_2 = input()
part_3 = input()
part_4 = input()

print("Bem-vindos ao Jimmy Jab!")
participantes = part_1 + part_2 + part_3 + part_4
if("Holt" in participantes or "Terry" in participantes):
    print("Jimmy Jab CANCELADO!")
else:
    print("Nosso primeiro evento é...")
    print("A Bocatona!")

    # BOCATONA
    if("Scully" not in participantes):
        vencedor_bocatona = input()
        perdedor_bocatona = input()
        print(f"{vencedor_bocatona} levou a melhor na Bocatona!")
    else:
        print("Scully leva a melhor, não tem como competir com ele.")
        perdedor_bocatona = input()
    print(f"{perdedor_bocatona} não avançou para a próxima fase!")

    if(perdedor_bocatona == part_1):
        eliminado = 1
    elif(perdedor_bocatona == part_2):
        eliminado = 2
    elif(perdedor_bocatona == part_3):
        eliminado = 3
    
    print("O segundo evento é A corrida volumosa!")
    # CORRIDA VOLUMOSA
    tempo_1 = int(input())
    tempo_2 = int(input())
    tempo_3 = int(input())

    menor_tempo = min(tempo_1, tempo_2, tempo_3)
    maior_tempo = max(tempo_1, tempo_2, tempo_3)

    # GANHADOR
    if(menor_tempo == tempo_1):
        if(eliminado == 1):
            ganhador_corrida = part_2
        else:
            ganhador_corrida = part_1
    elif(menor_tempo == tempo_2):
        if(eliminado == 2):
            ganhador_corrida = part_3
        else:
            ganhador_corrida = part_2
    else:
        if(eliminado == 3):
            ganhador_corrida = part_4
        else:
            ganhador_corrida = part_3

    # PERDEDOR
    if(maior_tempo == tempo_1):
        if(eliminado == 1):
            perdedor_corrida = part_2
        else:
            perdedor_corrida = part_1
    elif(maior_tempo == tempo_2):
        if(eliminado == 2):
            perdedor_corrida = part_3
        else:
            perdedor_corrida = part_2
    else:
        if(eliminado == 3):
            perdedor_corrida = part_4
        else:
            perdedor_corrida = part_3

    print(f"{ganhador_corrida} levou a melhor na Corrida Volumosa!")
    print(f"{perdedor_corrida} não avançou para a próxima fase!")

    perdedores = perdedor_bocatona + perdedor_corrida
    if(ganhador_corrida == "Amy" and "Jake" not in perdedores or ganhador_corrida == "Jake" and "Amy" not in perdedores):
        print("Jake ficou com o 2º lugar!")
        print("Amy VENCEU O JIMMY JABS!")

    else:
        ganhador_final = input()

        verificar_segundo = ganhador_final + perdedor_bocatona + perdedor_corrida
        if(part_1 not in verificar_segundo):
            segundo_lugar = part_1
        elif(part_2 not in verificar_segundo):
            segundo_lugar = part_2
        elif(part_3 not in verificar_segundo):
            segundo_lugar = part_3
        else:
            segundo_lugar = part_4

        print(f"{segundo_lugar} ficou com o 2º lugar!")
        print(f"{ganhador_final} VENCEU O JIMMY JABS!")
    