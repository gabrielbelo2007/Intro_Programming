fraquezas_resistencias = [
    # Tipo | Efetivo | Fraco
    ["fogo", "grama", "agua"],
    ["agua", "fogo", "grama", "eletrico"],
    ["grama", "agua", "fogo"],
    ["eletrico", "agua", "N/D"]
]

def calculo_multiplicador(tipo_atacante, tipo_defensor, guia_vantagens):

    for vantagens in guia_vantagens:

        if tipo_atacante == vantagens[0]:

            if tipo_defensor == vantagens[1]:
                return 2.0
            
            if tipo_defensor == vantagens[2]:
                return 0.5
            
            if tipo_atacante == "agua":

                if tipo_defensor == vantagens[3]:
                    return 0.5
    
    return 1.0 # Tipo Neutro

def calculo_dano(atacante, defensor, quem_ataca, guia_vantagens):

    if quem_ataca == "Aliado":

        print(f"{atacante[0]} usa {atacante[4]}!")

    elif quem_ataca == "Oponente":

        print(f"{atacante[0]} do oponente usa {atacante[4]}!")

    multiplicador = calculo_multiplicador(atacante[1], defensor[1], guia_vantagens)

    if multiplicador == 2.0:
        print(f"{atacante[4]} é super efetivo!")

    elif multiplicador == 0.5:
        print(f"{atacante[4]} não é muito efetivo...")

    poder_ataque = int(atacante[5])
    defesa = int(defensor[3])

    dano = int((poder_ataque - (defesa/2)) * multiplicador)
    dano = dano if dano > 1 else 1

    return dano

def mais_rapido(velocidade_aliado, velocidade_oponente):
    
    if int(velocidade_aliado) >= velocidade_oponente:
        return True

    return False

def definir_oponente(nome):
    
    if nome == "lorelei":
        return 0
    
    if nome == "bruno":
        return 1
    
    if nome == "agatha":
        return 2
    
    if nome == "lance":
        return 3

time_adversario = [
    # Lorelei
    [
        ["Lapras", "agua", 220, 50, "Raio de Gelo", 60, "agua", 60],
        ["Blastoise", "agua", 180, 55, "Hidro Bomba", 65, "agua", 78],
        ["Victreebel", "grama", 160, 40, "Folha Navalha", 55, "grama", 70],
        ["Ninetales", "fogo", 170, 45, "Lança-chamas", 60, "fogo", 100]
    ],

    # Bruno
    [
        ["Charizard", "fogo", 190, 40, "Presa de Fogo", 70, "fogo", 100],
        ["Arcanine", "fogo", 180, 50, "Velocidade Extrema", 60, "fogo", 95],
        ["Kingler", "agua", 170, 60, "Caranguejo Martelo", 65, "agua", 75],
        ["Jolteon", "eletrico", 150, 35, "Choque do Trovão", 55, "eletrico", 130]
    ],

    # Agatha
    [
        ["Venusaur", "grama", 180, 50, "Raio Solar", 70, "grama", 80],
        ["Vileplume", "grama", 160, 45, "Pó do Sono", 50, "grama", 50],
        ["Raichu", "eletrico", 160, 40, "Investida Trovão", 65, "eletrico", 110],
        ["Poliwrath", "agua", 190, 55, "Soco Dinâmico", 60, "agua", 70]
    ],

    # Lance
    [
        ["Electabuzz", "eletrico", 180, 45, "Soco de Trovão", 75, "eletrico", 105],
        ["Jolteon", "eletrico", 170, 35, "Onda de Trovão", 60, "eletrico", 130],
        ["Exeggutor", "grama", 160, 40, "Bomba de Semente", 65, "grama", 55],
        ["Magmar", "fogo", 175, 40, "Giro de Fogo", 55, "fogo", 93]
    ]
]

def preparar_times(equipe_adversaria):
    print("Hora de montar seu time Pokémon!")

    time = []
    vida_aliados = []
    vida_adversarios = []
    
    for pokemon in range(4):

        dados_pokemon = input().split(" - ")
        time.append(dados_pokemon)

        vida_aliados.append(int(dados_pokemon[2]))
    
    for equipe in equipe_adversaria:

        equipe_vida = []

        for dados_pokemon in equipe:
            equipe_vida.append(dados_pokemon[2])
        
        vida_adversarios.append(equipe_vida)

    return time, vida_aliados, vida_adversarios


def batalha_turnos(aliados, time_oponente, vida_total, vidas_oponentes):
    
    print()
    print("Qual membro da Elite Four você deseja enfrentar?")
    nome_oponente = input()
    print()

    index_oponente = definir_oponente(nome_oponente)

    oponentes = time_oponente[index_oponente]
    vida_oponente = vidas_oponentes[index_oponente]
    
    print("====================")
    print("A BATALHA VAI COMEÇAR!")
    print("====================")

    rodada = 1
    pk_atual_aliado = 0
    pk_atual_adversario = 0

    while sum(vida_total) > 0 and sum(vida_oponente) > 0:
        
        print()
        print(f"--- Rodada {rodada} ---")
        print(f"{aliados[pk_atual_aliado][0]}, eu escolho você!")
        print(f"{oponentes[pk_atual_adversario][0]}, vai!")
        print("--------------------")

        vida_pk_aliado = vida_total[pk_atual_aliado]
        vida_pk_oponente = vida_oponente[pk_atual_adversario]
        
        turno = 1
        while vida_pk_aliado > 0 and vida_pk_oponente > 0:
            
            print()
            print(f"-- Turno {turno} --")
            print()

            aliado_veloz = mais_rapido(aliados[pk_atual_aliado][7], oponentes[pk_atual_adversario][7])

            if aliado_veloz:

                dano = calculo_dano(aliados[pk_atual_aliado], oponentes[pk_atual_adversario], "Aliado", fraquezas_resistencias)
                vida_pk_oponente -= dano
                vida_pk_oponente = 0 if vida_pk_oponente < 0 else vida_pk_oponente

                print(f"Causou {dano} de dano. HP de {oponentes[pk_atual_adversario][0]} agora é {vida_pk_oponente}/{oponentes[pk_atual_adversario][2]}.")
                
                if vida_pk_oponente > 0:

                    print()

                    dano = calculo_dano(oponentes[pk_atual_adversario], aliados[pk_atual_aliado], "Oponente", fraquezas_resistencias)
                    vida_pk_aliado -= dano
                    vida_pk_aliado = 0 if vida_pk_aliado < 0 else vida_pk_aliado

                    print(f"Causou {dano} de dano. HP de {aliados[pk_atual_aliado][0]} agora é {vida_pk_aliado}/{aliados[pk_atual_aliado][2]}.")

            else:

                dano = calculo_dano(oponentes[pk_atual_adversario], aliados[pk_atual_aliado], "Oponente", fraquezas_resistencias)
                vida_pk_aliado -= dano
                vida_pk_aliado = 0 if vida_pk_aliado < 0 else vida_pk_aliado

                print(f"Causou {dano} de dano. HP de {aliados[pk_atual_aliado][0]} agora é {vida_pk_aliado}/{aliados[pk_atual_aliado][2]}.")

                if vida_pk_aliado > 0:

                    print()

                    dano = calculo_dano(aliados[pk_atual_aliado], oponentes[pk_atual_adversario], "Aliado", fraquezas_resistencias)
                    vida_pk_oponente -= dano
                    vida_pk_oponente = 0 if vida_pk_oponente < 0 else vida_pk_oponente

                    print(f"Causou {dano} de dano. HP de {oponentes[pk_atual_adversario][0]} agora é {vida_pk_oponente}/{oponentes[pk_atual_adversario][2]}.")

            turno += 1
        
        if vida_pk_aliado > 0:

            print()
            print(f"{oponentes[pk_atual_adversario][0]} do oponente foi derrotado!")

            vida_oponente[pk_atual_adversario] = 0
            vida_total[pk_atual_aliado] = vida_pk_aliado

            pk_atual_adversario += 1
        
        else:
            
            print()
            print(f"{aliados[pk_atual_aliado][0]} foi derrotado!")

            vida_total[pk_atual_aliado] = 0
            vida_oponente[pk_atual_adversario] = vida_pk_oponente

            pk_atual_aliado += 1

        rodada += 1

        print()
        print("--------------------")
        print()
        print(f"Placar: {pk_atual_adversario} X {pk_atual_aliado}")

    return pk_atual_adversario, pk_atual_aliado

time, vida_aliados, vida_adversarios = preparar_times(time_adversario)

oponentes_derrotados, aliados_derrotados = batalha_turnos(time, time_adversario, vida_aliados, vida_adversarios)

print()
print("========================================")
if oponentes_derrotados > aliados_derrotados:
    print("Parabéns! Você venceu a batalha Pokémon!")
else:
    print("Que pena! Você foi derrotado.")
print("========================================")