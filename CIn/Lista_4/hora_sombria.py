def makoto_acao(acao, makoto, ajudas_disponiveis, persona):
    
    # Flag para pedir input | Flag para print | Dano  
    resultado_acao = [False, "", 0]

    if acao == "junpei":

        if ajudas_disponiveis[1] > 0:
            ajudas_disponiveis[1] -= 1
            resultado_acao[0] = True
            resultado_acao[1] = "junpei ajudou"
            resultado_acao[2] = 100

        else:
            resultado_acao[1] = "sem ajuda"
        
    elif acao == "yukari":

        if ajudas_disponiveis[0] > 0: 
            ajudas_disponiveis[0] -= 1
            resultado_acao[0] = True
            resultado_acao[1] = "yukari ajudou"

        else:
            resultado_acao[1] = "sem ajuda"
    
    elif acao == "persona":
        
        # Checar se tem mana (mana - custo >= 0)
        if makoto[1] - persona[3] >= 0:
            resultado_acao[0] = True
            makoto[1] -= persona[3]

            lista_desordenada = input().split(" ")
            lista_desordenada = [int(valor) for valor in lista_desordenada]
            trocas = resultado_golpe(lista_desordenada)

            dano = calculo_dano(persona[4], persona[1])
            
            if trocas == 0:
                dano = round(dano * 1.5)
                resultado_acao[1] = "acerto fraqueza" 
                print(f"Makoto: Venha {persona[0]}!")

            elif trocas > 5:
                resultado_acao[1] = "errou"
                dano = 0 
            
            else:
                resultado_acao[1] = "acertou"
                print("Makoto: Persona!")

            resultado_acao[2] = dano

        else:
            resultado_acao[1] = "sem mana"       

    elif acao == "atacar":

        dano = calculo_dano(2, makoto[2])
        resultado_acao[0] = True
        resultado_acao[1] = "golpe basico"
        resultado_acao[2] = dano

    return resultado_acao


def calculo_dano(poder_base, atk_usuario):
    
    dano = int(((poder_base * 15) ** 0.5) * (atk_usuario / 2))

    return dano


# Função Bubblesort
def resultado_golpe(lista):

    # listas copiadas
    ordenar_crescente = lista.copy()
    ordenar_decrescente = lista.copy()

    contagem_crescente = 0
    contagem_decrescente = 0
    
    tam_lista = len(ordenar_crescente)
    for i in range(tam_lista - 1):
        for j in range(tam_lista - i - 1):
            if ordenar_crescente[j] > ordenar_crescente[j + 1]:
               ordenar_crescente[j], ordenar_crescente[j + 1] = ordenar_crescente[j + 1], ordenar_crescente[j]
               contagem_crescente += 1

    for i in range(tam_lista - 1):
        for j in range(tam_lista - i - 1):
            if ordenar_decrescente[j] < ordenar_decrescente[j + 1]:
               ordenar_decrescente[j], ordenar_decrescente[j + 1] = ordenar_decrescente[j + 1], ordenar_decrescente[j]
               contagem_decrescente += 1
    
    return min(contagem_crescente, contagem_decrescente)


def turno_makoto(acao_turno,resultado_acao, sombra_atual, makoto, vida_sombras, indice_sombra):

    if acao_turno == "persona":
        if resultado_acao[1] == "acerto fraqueza":   
            sombra_atual[4] = "Derrubado"
            vida_sombras[indice_sombra] -= resultado_acao[2]

            if vida_sombras[indice_sombra] <= 0:
                vida_sombras[indice_sombra] = 0
                sombra_atual[4] = "Derrotado"

                print(f"Mitsuru: {sombra_atual[0]} foi derrotado!")

            return True  # Recebeu o "mais_um"

        elif resultado_acao[1] == "acertou":
            vida_sombras[indice_sombra] -= resultado_acao[2]

            if vida_sombras[indice_sombra] <= 0:
                vida_sombras[indice_sombra] = 0
                sombra_atual[4] = "Derrotado"

                print(f"Mitsuru: {sombra_atual[0]} foi derrotado!")
        
        elif resultado_acao[1] == "sem mana":
            print(f"Makoto: Estou cansado...")


    elif acao_turno == "yukari":
        if resultado_acao[1] == "yukari ajudou":
            print("Yukari: Aguenta ai, líder!")
            print("Mitsuru: Bom trabalho, Yukari! Makoto se sente mais revigorado")
            
            makoto[0] += 100 if makoto[0] + 100 <= 300 else (300 - makoto[0])
        
        elif resultado_acao[1] == "sem ajuda":
            print("Yukari: Estou exausta, foi mal!")


    elif acao_turno == "junpei":
        if resultado_acao[1] == "junpei ajudou":
            print("Junpei: HOOOOOME RUUUUN!!")
            print(f"Mitsuru: Acerto CRÍTICO de Junpei! {sombra_atual[0]} sofreu 100 de dano!")
            
            vida_sombras[indice_sombra] -= resultado_acao[2]

            if vida_sombras[indice_sombra] <= 0:
                vida_sombras[indice_sombra] = 0
                sombra_atual[4] = "Derrotado"

                print(f"Mitsuru: {sombra_atual[0]} foi derrotado!")

            else:
                sombra_atual[4] = "Derrubado"

            return True # Recebeu o "mais_um"

        elif resultado_acao[1] == "sem ajuda":
            print("Junpei: Cara, tô cansado!")

    elif acao_turno == "atacar":

        vida_sombras[indice_sombra] -= resultado_acao[2]

        if vida_sombras[indice_sombra] <= 0:
            vida_sombras[indice_sombra] = 0
            sombra_atual[4] = "Derrotado"

            print(f"Mitsuru: {sombra_atual[0]} foi derrotado!")

    return False 


def turno_sombra(sombra, makoto):

    sombra[4] == "Ativo"
    
    dano = calculo_dano(sombra[5], sombra[2])

    makoto[0] -= dano if makoto[0] - dano >= 0 else makoto[0]

    return dano


def registrar_persona(golpes):
    persona_status = input().split(" - ")

    persona_status[1] = int(persona_status[1])
    persona_status[3] = int(persona_status[3])
    
    # Adicionando dano do golpe
    for i in range(3):
        if persona_status[2].lower() in golpes[i]:
            persona_status.append(golpes[i][0])

    print(f"{persona_status[0]}: Eu sou tu e tu és eu...")

    return persona_status


def registrar_sombras(num_sombras, sombras, vida_sombras, golpes):
    
    for _ in range(num_sombras):
        sombra_status = input().split(" - ")

        sombra_status[1] = int(sombra_status[1])
        sombra_status[2] = int(sombra_status[2])
            
        sombra_status.append("Ativo")
        
        # Adicionando dano do golpe
        for i in range(3):
            if sombra_status[3].lower() in golpes[i]:
                sombra_status.append(golpes[i][0])

        sombras.append(sombra_status)
        vida_sombras.append(sombra_status[1])

    print("Mitsuru: Inimigos detectados, se preparem!")


# Golpes:  dano, nomes...
golpes = [
    [3, "zio", "garu", "agi", "bufu"], # magico_leve
    [4, "corte", "perfuração", "pancada"], # fisico_leve
    [5, "zionga", "garula", "agilao", "bufula"] # magico_medio 
]

# Vida, Mana
makoto_status = [300, 70, 0]

# Yukari, Junpei
ajudas_total = [2, 1]

print("Mitsuru: Vamos iniciar nossa exploração, tomem cuidado.")

persona_status = registrar_persona(golpes)

# Adicionando valor de atk de makoto
makoto_status[2] = persona_status[1]

# Sombras 1 Andar
num_sombras = int(input())
vida_sombras = []
sombras = []
registrar_sombras(num_sombras, sombras, vida_sombras, golpes)

sombra_atual_atacante = 0
sombra_atual_alvo = 0

vez_atual = "Makoto"
turnos = 1
ganhou = False
andares_explorados = 0

sombra_alvo = sombras[sombra_atual_alvo]
sombra_atacante = sombras[sombra_atual_atacante]

mais_um = False

while makoto_status[0] > 0:

    if vez_atual == "Makoto":
        print("Makoto: O que fazer...")

        resultado_acao = [False] # Flag temporária

        if not mais_um:
            sombra_atual_alvo = 0
            sombra_alvo = sombras[sombra_atual_alvo]

            while sombra_alvo[4] == "Derrotado":
                sombra_atual_alvo = (sombra_atual_alvo + 1) % num_sombras
                sombra_alvo = sombras[sombra_atual_alvo]

        while not resultado_acao[0]:
            acao_turno = input()
            resultado_acao = makoto_acao(acao_turno, makoto_status, ajudas_total, persona_status)

            if resultado_acao[0] or resultado_acao[1] in ["sem ajuda", "sem mana"]:
                
                if resultado_acao[2] > 0 and acao_turno not in ["junpei", "yukari"]:
                    print(f"Mitsuru: Makoto acertou {sombra_alvo[0]} causando {resultado_acao[2]} de dano!")

                elif resultado_acao[1] == "errou":
                    print("Makoto: O quê?!")
                    print("Mitsuru: Mais foco, Makoto!")

                mais_um = turno_makoto(acao_turno, resultado_acao, sombra_alvo, makoto_status, vida_sombras, sombra_atual_alvo)

                if sum(vida_sombras) > 0: # Verifica se não estão todas derrubadas
                    
                    sombras_derrubadas = 0
                    sombras_derrotadas = 0

                    for sombra in range(num_sombras):
                        
                        sombra_estado = sombras[sombra][4]

                        if sombra_estado == "Derrubado":
                            sombras_derrubadas += 1
                        
                        elif sombra_estado == "Derrotado":
                            sombras_derrotadas += 1
                    
                    if sombras_derrubadas == (num_sombras - sombras_derrotadas):
                        print("Mitsuru: Todos os inimigos cairam! Avancem com tudo!")
                        print("MASS DESTRUCTION!")
                        ganhou = True

                    elif (sombras_derrubadas + sombras_derrotadas) == num_sombras:
                        ganhou = True
                    
                    elif resultado_acao[1] == 'acerto fraqueza' or resultado_acao[1] == "junpei ajudou":
                        print("MAIS UM!")
                        print("Mitsuru: Você acertou uma fraqueza! Continue no ataque!")
                
                elif sum(vida_sombras) == 0:
                    ganhou = True

        if not ganhou and (sombra_alvo[4] == "Derrotado" or mais_um): 
            
            sombra_atual_alvo = (sombra_atual_alvo + 1) % num_sombras
            sombra_alvo = sombras[sombra_atual_alvo]

            while sombra_alvo[4] == "Derrotado":
                sombra_atual_alvo = (sombra_atual_alvo + 1) % num_sombras
                sombra_alvo = sombras[sombra_atual_alvo]
        
        vez_atual = "Makoto" if mais_um else "Sombras"

    if vez_atual == "Sombras" and not ganhou:

        while sombra_atacante[4] == "Derrotado":
            sombra_atual_atacante = (sombra_atual_atacante + 1) % num_sombras
            sombra_atacante = sombras[sombra_atual_atacante]

        if sombra_atacante[4] == "Derrubado":
            sombra_atacante[4] = "Ativo"

        dano_causado = turno_sombra(sombra_atacante, makoto_status)

        print(f"Mitsuru: Makoto foi atacado por {sombra_atacante[0]} e recebeu {dano_causado} de dano!")

        sombra_atual_atacante = (sombra_atual_atacante + 1)  % num_sombras
        sombra_atacante = sombras[sombra_atual_atacante]

        vez_atual = "Makoto"

    # Relatório
    if makoto_status[0] > 0 and not ganhou:
        
        print(f"TURNO {turnos}:")
        turnos += 1
        print(f"HP Makoto: {makoto_status[0]} / 300")

        for sombra in range(num_sombras):

            sombra_estado = sombras[sombra][4]

            if sombra_estado != "Derrotado":
                print(f"HP {sombras[sombra][0]}: {vida_sombras[sombra]} pontos de vida restantes")


    if ganhou:
        ganhou = False
        print("Mitsuru: Muito bem! Continuem a exploração.")

        # Receber nova Persona e Sombras
        persona_status = registrar_persona(golpes)
        makoto_status[2] = persona_status[1] # Alterar atk basico
        
        vida_sombras = []
        sombras = []
        num_sombras = int(input())
        registrar_sombras(num_sombras, sombras, vida_sombras, golpes)

        # Recuperar vida e mana
        makoto_status[0] += 50 if (makoto_status[0] + 50) <= 300 else (300 - makoto_status[0])
        makoto_status[1] += 15 if (makoto_status[1] + 15) <= 70 else (70 - makoto_status[1])

        # Yukari, Junpei
        ajudas_total = [2, 1]

        vez_atual = "Makoto"
        andares_explorados += 1
        turnos = 1

        sombra_atual_alvo = 0
        sombra_atual_atacante = 0
        
        sombra_alvo = sombras[sombra_atual_alvo]
        sombra_atacante = sombras[sombra_atual_atacante]

else:
    print("Makoto: Argh...")
    print(f"Mitsuru: Líder? Aconteceu algo? Responda!\n")
    print("FIM DE JOGO")
    print(f"Andares explorados: {andares_explorados}")