def makoto_acao(acao, makoto, ajudas_disponiveis, persona):
    
    # Flag para pedir input | Flag para print | Dano  
    resultado_acao = [False, "", 0]

    if acao == "junpei" and ajudas_disponiveis[1] > 0:
        ajudas_disponiveis[1] -= 1
        resultado_acao[0] = True

        dano = 100
        
    elif acao == "yukari" and ajudas_disponiveis[0] > 0:
        ajudas_disponiveis[0] -= 1
        resultado_acao[0] = True
    
    elif acao == "persona":
        
        # Checar se tem mana
        if makoto[1] - persona[3] > 0:
            lista_desordenada = input().split(" ")
            trocas = resultado_golpe(lista_desordenada)

            dano = calculo_dano(persona[4], persona[1])
            
            if trocas == 0:
                dano *= 1.5
                resultado_acao[1] = "golpe forte" 

            if trocas > 5:
                resultado_acao[1] = "errou"
                dano = 0 

            resultado_acao[2] = dano

        else:
            resultado_acao[1] = "sem mana"       

    elif acao == "atacar":
        dano = calculo_dano(2, makoto[2])
        resultado_acao[0] = True
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
    
    n_cres = len(ordenar_crescente)
    for i in range(n_cres - 1):
        for j in range(n_cres - i - 1):
            if ordenar_crescente[j] > ordenar_crescente[j + 1]:
               ordenar_crescente[j], ordenar_crescente[j + 1] = ordenar_crescente[j + 1], ordenar_crescente[j]
               contagem_crescente += 1

    n_decres = len(ordenar_decrescente)
    for i in range(n_decres - 1):
        for j in range(n_decres - i - 1):
            if ordenar_decrescente[j] < ordenar_decrescente[j + 1]:
               ordenar_decrescente[j], ordenar_decrescente[j + 1] = ordenar_decrescente[j + 1], ordenar_decrescente[j]
               contagem_decrescente += 1
    
    return min(contagem_crescente, contagem_decrescente)


def turno_makoto(acao, sombra_atual, makoto, vida_sombras, indice_sombra):

    if acao_turno == "persona":
        if acao[1] == "acerto fraqueza":   
            print(f"Makoto: Venha {persona_status[0]}!")

            sombra_atual[3] = "Derrubado"

            return True

        elif acao[1] == "golpe forte":
            print(f"Makoto: Persona!")

        elif acao[1] == "errou":
            print(f"'Makoto: O quê?!")
        
        elif acao[1] == "sem mana":
            print(f"Makoto: Estou cansado...")


    elif acao_turno == "yukari":
        if acao[1] == "yukari ajudou":
            print("Yukari: Aguenta ai, líder!")
            print("Mitsuru: Bom trabalho, Yukari! Makoto se sente mais revigorado")
            
            makoto[0] += 100 if makoto[0] + 100 <= 300 else (300 - makoto[0])
        
        elif acao[1] == "sem ajuda":
            print("Yukari: Estou exausta, foi mal!")


    elif acao_turno == "junpei":
        if acao[1] == "junpei ajudou":
            print("Junpei: HOOOOOME RUUUUN!!")
            print(f"Mitsuru: Acerto CRÍTICO de Junpei! {sombra_atual[0]} sofreu 100 de dano!")
            
            vida_sombras[indice_sombra] -= acao[2]

            if vida_sombras[indice_sombra] <= 0:
                vida_sombras[indice_sombra] = 0
                sombra_atual[3] = "Derrotado"
                return True

            else:
                sombra_atual[3] = "Derrubado"

        if acao[1] == "sem ajuda":
            print("Junpei: Cara, tô cansado!")

    return False


def turno_sombra(sombra):
    pass

# Golpes:  dano, nomes...
golpes = [
    [3, "zio", "garu", "agi", "bufu"], # magico_leve
    [4, "corte", "perfuração", "pancada"], # fisico_leve
    [5, "zionga", "garula", "agilao", "bufula"] # magico_medio 
]

# Vida, Mana
makoto_status = [300, 70]

# Yukari, Junpei
ajudas_total = [2, 1]

vida_sombras = []
sombras = []
num_sombras = input()

print("Mitsuru: Vamos iniciar nossa exploração, tomem cuidado.")

persona_status = input().split(" - ")
persona_status = [int(valor) for valor in persona_status]

for i in range(3):
    if persona_status[3] in golpes[i]:
        persona_status.append(golpes[i][0])

print(f"{persona_status[0]}: Eu sou tu e tu és eu...")

# Adicionando valor de atk de makoto
makoto_status.append(persona_status[1])

for _ in range(num_sombras):
    sombra_status = input().split(" - ")

    sombra_status.append("Ativo")
    sombras.append(sombra_status)

    vida_sombras.append(sombra_status[1])

print("Mitsuru: Inimigos detectados, se preparem!")

vez_atual = "Makoto"
sombra_atual = 0
turnos = 0

while sum(vida_sombras) > 0 and makoto_status[0] > 0:

    if vez_atual == "Makoto":
        print("Makoto: O que fazer...")

        resultado_acao = [True]

        while resultado_acao[0]:
            acao_turno = input()
            resultado_acao = makoto_acao(acao_turno, ajudas_total, makoto_status[1])

            mais_um = turno_makoto(resultado_acao)

    elif vez_atual == "Sombras":
        pass 
    
    vez_atual = "Makoto" if vez_atual == "Sombras" or mais_um else "Sombras"