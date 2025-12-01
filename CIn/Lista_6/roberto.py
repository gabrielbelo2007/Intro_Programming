divas_estadunidenses = (
    'Olivia Rodrigo',
    'Sabrina Carpenter',
    'Beyoncé', 
    'Taylor Swift', 
    'Lady Gaga', 
    'Azealia Banks', 
    'Katy Perry', 
    'Madonna',
    'Ariana Grande',
    'Mariah Carey',
    'Whitney Houston',
    'Britney Spears',
    'Christina Aguilera',
    'Janet Jackson',
    'Cher',
    'Nicki Minaj',
    'Cardi B',
    'Doja Cat',
    'Billie Eilish'
)

conflitos = {
    'Katy Perry': ('Taylor Swift',),
    'Taylor Swift': ('Katy Perry', 'Ariana Grande', 'Olivia Rodrigo', 'Dua Lipa'),
    'Madonna': ('Lady Gaga',),
    'Lady Gaga': ('Madonna',),
    'Mariah Carey': ('Jennifer Lopez',),
    'Jennifer Lopez': ('Mariah Carey',),
    'Christina Aguilera': ('Britney Spears',),
    'Britney Spears': ('Christina Aguilera',),
    'Nicki Minaj': ('Doja Cat',),
    'Anitta': ('Ludmilla',),
    'Ludmilla': ('Anitta',),
    'Ariana Grande': ('Taylor Swift', 'Cynthia Erivo'),
    'Sabrina Carpenter': ('Camila Cabello', 'Olivia Rodrigo', 'Doja Cat'),
    'Camila Cabello': ('Sabrina Carpenter',),
    'Olivia Rodrigo': ('Taylor Swift', 'Sabrina Carpenter'),
    'Dua Lipa': ('Taylor Swift',),
    'Doja Cat': ('Nicki Minaj', 'Sabrina Carpenter'),
}

def contagem_frequencia(tupla_valores):

    frequencia = {}

    for valor in tupla_valores:
        frequencia[valor] = frequencia.get(valor, 0) + 1

    return frequencia

def verificar_permutacao(letras_candidata, letras_diva):

    return contagem_frequencia(letras_candidata) == contagem_frequencia(letras_diva)

def ordernar_candidatas(candidatas_pontuacoes, candidatas_popularidade):

    pontuacoes_desordenadas = candidatas_pontuacoes.copy()
    pontuacoes_ordenadas = {}

    for _ in candidatas_pontuacoes:

        divas_empatadas_pontucao = ()
        divas_empatadas_popularidade = ()

        # Critério Principal (Maior Pontuação)
        maior_pontuacao = 0
        for candidata in pontuacoes_desordenadas:

            if pontuacoes_desordenadas[candidata] >= maior_pontuacao:
                divas_empatadas_pontucao = divas_empatadas_pontucao + (candidata,) if pontuacoes_desordenadas[candidata] == maior_pontuacao else (candidata,)
                maior_pontuacao = pontuacoes_desordenadas[candidata]

        diva = divas_empatadas_pontucao[0]

        # Desempate de Popularidade
        if len(divas_empatadas_pontucao) > 1:
            maior_popularidade = 0

            for candidata in divas_empatadas_pontucao:
                
                if candidatas_popularidade[candidata] >= maior_popularidade:
                    divas_empatadas_popularidade = divas_empatadas_popularidade + (candidata,) if candidatas_popularidade[candidata] == maior_popularidade else (candidata,)
                    maior_popularidade = candidatas_popularidade[candidata]

            diva = divas_empatadas_popularidade[0]

            if len(divas_empatadas_popularidade) > 1:
                diva = min(divas_empatadas_popularidade)
        
        pontuacoes_ordenadas[diva] = pontuacoes_desordenadas[diva]
        pontuacoes_desordenadas.pop(diva)

    return pontuacoes_ordenadas

def mostrar_placar(candidatas_pontuacoes, fase):
    print()
    print(f"=== PLACAR DA {fase}ª FASE ===")

    for candidata in candidatas_pontuacoes:

        print(f"{candidata} --- {candidatas_pontuacoes[candidata]}")


desc_candidata = ""
candidatas_pontuacao = {}
candidatas_popularidade = {}

# FASE 1

print(f"A BATALHA DAS DIVAS começa... AGORA!\n")
desc_candidata = input()

while desc_candidata != "FIM DAS INSCRIÇÕES":

    candidata, pais, grammys, popularidade, shows = desc_candidata.split(" - ")

    if candidata not in divas_estadunidenses and candidata not in candidatas_pontuacao:

        # Verificando candidata escondida
        letras_candidata = ()
        for letra in candidata:
            if letra != " ":
                letras_candidata = letras_candidata + (letra.lower(),)

        for diva in divas_estadunidenses:

            letras_diva = ()
            for letra in diva:
                if letra != " ":
                    letras_diva = letras_diva + (letra.lower(),)

            if verificar_permutacao(letras_candidata, letras_diva):
                candidata = diva
                penalidade = -100
                bonus = 0

    if candidata not in candidatas_pontuacao:

        penalidade = 0 if candidata not in divas_estadunidenses else -50
        bonus = 50 if pais == "Brasil" else 0
        
        if candidata in divas_estadunidenses and pais != "EUA":
            penalidade = -100
            bonus = 0
        
        # Adicionando candidatas no dicionário de candidatas
        if candidata != "Azealia Banks":

            pontuacao_candidata = (int(grammys) * 15) + (int(popularidade) * 10) + (int(shows) * 5) + penalidade + bonus
            candidatas_pontuacao[candidata] = pontuacao_candidata

            candidatas_popularidade[candidata] = int(popularidade)

            print(f"{candidata} acaba de entrar na Batalha das Divas!")

            if pais == "Brasil" and penalidade == 0:
                print(f"ESSA TEM O TEMPERO BRASILEIRO! Por jogar em casa, {candidata} já larga com 50 pontos de vantagem.")

            elif penalidade == -50:
                print(f'Por excesso de "estrelas e listras", {candidata} recebe uma penalidade de 50 pontos.')

            elif penalidade == -100:
                print(f"A CASA CAIU! A produção pegou {candidata} no pulo do gato tentando se livrar da penalidade! Por essa tentativa de malandragem, o preço veio dobrado.")

        else:
            print(f"Eita, climão! Parece que o histórico de polêmicas de {candidata} falou mais alto. A produção barrou a entrada e aqui no Brasil ela não canta!")

    else:
        print(f"Só pode ter uma {candidata} na arena. Inscrição duplicada negada!")
    
    desc_candidata = input()

if len(candidatas_pontuacao) > 1:

    candidatas_pontuacao = ordernar_candidatas(candidatas_pontuacao, candidatas_popularidade)

    mostrar_placar(candidatas_pontuacao, 1)

# FASE 2

    duelo_iniciado = False
    nome_eliminadas = ()

    for candidata in candidatas_pontuacao:

        if candidata not in nome_eliminadas and candidata in conflitos:
            
            rivais = conflitos[candidata]

            for rival in rivais:

                if rival in candidatas_pontuacao and rival not in nome_eliminadas and candidata not in nome_eliminadas:

                    if not duelo_iniciado:
                        print()
                        print("SALTO ALTO NO TABLADO! HORA DO DUELO!")
                        duelo_iniciado = True

                    conflito = (candidata, rival)

                    print(f"DRAMA! A rivalidade entre {conflito[0]} e {conflito[1]} vai ser resolvida no palco, AGORA!")

                    if candidatas_pontuacao[conflito[0]] > candidatas_pontuacao[conflito[1]]:
                        nome_eliminadas = nome_eliminadas + (conflito[1],)

                        print(f"Eliminada(s): {conflito[1]}")

                    elif candidatas_pontuacao[conflito[0]] < candidatas_pontuacao[conflito[1]]:
                        nome_eliminadas = nome_eliminadas + (conflito[0],)
                    
                        print(f"Eliminada(s): {conflito[0]}")  

                    elif candidatas_pontuacao[conflito[0]] == candidatas_pontuacao[conflito[1]]:
                        nome_eliminadas = nome_eliminadas + (conflito[0], conflito[1])

                        print(f"Eliminada(s): {conflito[0]} e {conflito[1]}")
    
    if not duelo_iniciado:
        print()
        print("O palco estava montado. Os holofotes, ligados. Mas o conflito não apareceu. Fase 2 cancelada: as divas escolheram reinar em paz.")

    else:

        for eliminada in nome_eliminadas:
            candidatas_pontuacao.pop(eliminada)

        if len(candidatas_pontuacao) > 0:
            candidatas_pontuacao = ordernar_candidatas(candidatas_pontuacao, candidatas_popularidade)
            mostrar_placar(candidatas_pontuacao, 2)

# FASE 3
if len(candidatas_pontuacao) > 1:
  
    divas_com_habilidades = ("Lady Gaga", "Beyoncé", "Anitta")

    sem_jogada_especial = True
    
    qtd_candidatas = len(candidatas_pontuacao)
    posicao_gaga = 0
    posicao_beyonce = 0 

    posicao_candidata = 1
    for candidata in candidatas_pontuacao:

        if candidata in divas_com_habilidades:
            sem_jogada_especial = False

        if candidata == "Lady Gaga":
            posicao_gaga = posicao_candidata

        if candidata == "Beyoncé":
            posicao_beyonce = posicao_candidata

        if posicao_candidata == 1:
            primeiro_lugar = candidata

        if posicao_candidata == qtd_candidatas - 2:
            penultimo_lugar = candidata

        if posicao_candidata == qtd_candidatas - 1:
            ultimo_lugar = candidata

        posicao_candidata += 1

    if sem_jogada_especial:
        print()
        print("Silêncio no palco... Nenhuma habilidade especial foi ativada.")

    else:
        print()
        print("O PALCO VAI TREMER! HORA DAS JOGADAS ESPECIAIS!")

        # Lady Gaga
        if posicao_gaga > 3:

            candidata_alvo = ultimo_lugar if ultimo_lugar != "Lady Gaga" else penultimo_lugar

            if candidatas_popularidade[candidata_alvo] <= (candidatas_popularidade["Lady Gaga"] * 1.25):
                
                candidatas_pontuacao["Lady Gaga"] = candidatas_pontuacao["Lady Gaga"] + candidatas_pontuacao[candidata_alvo]

                print(f'ARRASOU! O blefe de Lady Gaga funcionou! Ela enganou os jurados com seu "Poker Face" e roubou a cena de {candidata_alvo}!')

                candidatas_pontuacao.pop(candidata_alvo)

            else:
                print('QUE REVIRAVOLTA! O público não caiu no "Poker Face" de Lady Gaga! A farsa foi descoberta e ela está eliminada!')

                candidatas_pontuacao.pop("Lady Gaga")

        candidatas_pontuacao = ordernar_candidatas(candidatas_pontuacao, candidatas_popularidade)

        # Beyoncé
        if posicao_beyonce > 0:
            
            if qtd_candidatas > 2:

                candidatas_fracas = ()
                pontuacao_candidatas = 0

                for posicao_alvo in range(len(candidatas_pontuacao), 1, -1):

                    if posicao_alvo != posicao_beyonce and len(candidatas_fracas) < 2:
                        
                        posicao_candidata = len(candidatas_pontuacao)
                        for candidata in candidatas_pontuacao:

                            if posicao_candidata == posicao_alvo:
                                
                                candidatas_fracas = candidatas_fracas + (candidata,)
                                pontuacao_candidatas += candidatas_pontuacao[candidata]
                            
                            posicao_candidata -= 1

                if pontuacao_candidatas <= candidatas_pontuacao["Beyoncé"]:
                    
                    adicao_total = 0
                    for candidata in candidatas_fracas:

                        adicao_pontuacao = int(candidatas_pontuacao[candidata] * 0.10)
                        candidatas_pontuacao[candidata] = candidatas_pontuacao[candidata] + adicao_pontuacao
                        
                        adicao_total += adicao_pontuacao

                    candidatas_pontuacao["Beyoncé"] = candidatas_pontuacao["Beyoncé"] + adicao_total
                    print('PAREM TUDO! Queen Bey ativou a "Formation"! Ela reorganizou o jogo, elevou as novatas e saiu ainda mais forte!')

                else:
                    print('CHOQUE! A estratégia de Beyoncé foi ousada demais! A "Formation" não convenceu e ela foi desclassificada por manipulação!')
                    candidatas_pontuacao.pop("Beyoncé")
            
            candidatas_pontuacao = ordernar_candidatas(candidatas_pontuacao, candidatas_popularidade)


        # Anitta
        if primeiro_lugar != "Anitta" and "Anitta" in candidatas_pontuacao:
            
            if candidatas_popularidade["Anitta"] >= (candidatas_popularidade[primeiro_lugar] * 0.9):

                print(f'A PATROA TÁ ON! Anitta usou "Envolver" e fez {primeiro_lugar} dançar conforme sua música, virando o placar a seu favor!')
                pontos_roubados = (candidatas_pontuacao[primeiro_lugar] - candidatas_pontuacao["Anitta"]) * 0.25

                # Atualizar pontuação do primeiro lugar
                candidatas_pontuacao[primeiro_lugar] = int(candidatas_pontuacao[primeiro_lugar] - pontos_roubados)

                # Atualizar pontuação da Anitta
                candidatas_pontuacao["Anitta"] = int(candidatas_pontuacao["Anitta"] + pontos_roubados)

            else:

                print('DEU RUIM! A tentativa de "Envolver" de Anitta não funcionou! A jogada foi arriscada e o público não comprou a ideia.')
                candidatas_pontuacao["Anitta"] = candidatas_pontuacao["Anitta"] - 75
        
        candidatas_pontuacao = ordernar_candidatas(candidatas_pontuacao, candidatas_popularidade)
        mostrar_placar(candidatas_pontuacao, 3)

# RESULTADO FINAL
if len(candidatas_pontuacao) == 0:
    print()
    print("INACREDITÁVEL! A Batalha das Divas terminou em caos, sem nenhuma vencedora! O palco está vazio... MAS O CALOR DA BRIGA FEZ O IMPOSSÍVEL! O Rei descongelou, subiu ao palco, olhou para a confusão e disse:")
    print("Obrigado pela ajuda, meninas, mas o show já tem atração... e Esse Cara Sou Eu.")
    print("O RÉVEILLON ESTÁ SALVO!")

else:
    print()
    print("=== HABEMUS DIVAM! ===")
    print("A GUERRA ACABOU! A nova dona do palco, a chefe do Réveillon, a única... é ELA!")

    posicao_candidata = 1
    for candidata in candidatas_pontuacao:

        if posicao_candidata == 1:
            nome_vencedora = candidata

        if candidata == "Taylor Swift":
            posicao_taylor = posicao_candidata

        posicao_candidata += 1

    if "Taylor Swift" in candidatas_pontuacao:

        if posicao_taylor in [2, 3]:
            
            print(f"PARABÉNS, {nome_vencedora[:3].upper()}... TAYLOR SWIFT!!!")
            print('MAS O QUE É ISSO?! Uma reviravolta de última hora! O conselheiro Filipe Moreira acaba de invadir a sala de controle! Alegando fazer parte de uma "comissão cinterna" de Swifties, ele anulou o resultado final e declarou que a verdadeira Era do Réveillon pertence à Taylor Swift! O show está garantido... e a rainha dele também!')

        else:
            print(f"PARABÉNS, {nome_vencedora.upper()}!!! O Rei pode descansar em paz (no gelo), pois o show está garantido!")

    else:
        print(f"PARABÉNS, {nome_vencedora.upper()}!!! O Rei pode descansar em paz (no gelo), pois o show está garantido!")