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

# Verificar permutação

def contagem_frequencia(tupla_valores):

    frequencia = {}

    for valor in tupla_valores:
        frequencia[valor] = frequencia.get(valor, 0) + 1

    return frequencia

def verificar_permutacao(letras_candidata, letras_diva):

    return contagem_frequencia(letras_candidata) == contagem_frequencia(letras_diva)


# PLACAR

def mostrar_placar(candidatas_pontuacoes, candidatas_popularidade, fase):

    # Contabilizando quantidade de pontuações
    pontuacoes = ()
    for candidata in candidatas_pontuacoes:
        pontuacoes = pontuacoes + candidatas_pontuacoes[candidata]

    frequencia_pontuacoes = contagem_frequencia(pontuacoes)
    pontuacao_empatada = max(frequencia_pontuacoes, key=frequencia_pontuacoes.get)
    
    # Salvando candidatas com mesma pontuação
    candidatas_empatadas = ()   
    for candidata in candidatas_pontuacoes:

        if candidatas_pontuacoes[candidata] == pontuacao_empatada:
            candidatas_empatadas = candidatas_empatadas + candidata

    # Impressão candidatas
    print(f"=== PLACAR DA {fase}ª FASE ===")

    qtd_candidatas = len(candidatas_pontuacoes)

    candidatas_printadas = ()
    while len(candidatas_printadas) <= qtd_candidatas:

        candidata_maior_pontuacao = ("", 0)
        
        for candidata in candidatas_pontuacoes:

            if candidatas_pontuacoes[candidata] > candidata_maior_pontuacao[1] and candidata not in candidatas_printadas:
                candidata_maior_pontuacao = (candidata, candidatas_pontuacoes[candidata])
        
        if candidata_maior_pontuacao[0] in candidatas_empatadas:
            
            candidatas_desempatadas = 0
            while candidatas_desempatadas <= len(candidatas_empatadas):

                candidata_maior_popularidade = ("", 0)

                for candidata in candidatas_empatadas:
                    
                    if candidatas_popularidade[candidata] > candidata_maior_popularidade[1] and candidata not in candidatas_printadas:
                        candidata_maior_popularidade = (candidata, candidatas_popularidade[candidata])


                    # Desempate lexicográfico
                    elif candidatas_popularidade[candidata] == candidata_maior_popularidade[1]:
                        pass

                # Essa posição do print não está boa, para o caso de ter um empate e desempatar com lexicografia
                print(f"{candidata_maior_popularidade[0]} --- {candidatas_pontuacoes[candidata]}")

        else:
            print(f"{candidata_maior_pontuacao[0]} --- {candidata_maior_pontuacao[1]}")

        candidatas_printadas = candidatas_printadas + candidata_maior_pontuacao[0]



desc_candidata = ""
candidatas_pontuacao = {}
candidatas_popularidade = {}

# FASE 1

print("A BATALHA DAS DIVAS começa... AGORA!")

while desc_candidata != "FIM DAS INSCRIÇÕES":

    desc_candidata = input()

    if desc_candidata != "FIM DAS INSCRIÇÕES":

        candidata, pais, grammys, popularidade, shows = desc_candidata.split("-")

        if candidata not in candidatas_pontuacao:

            penalidade = 0 if candidata not in divas_estadunidenses else -50
            bonus = 50 if pais == "Brasil" else 0
            
            # Verificando candidata escondida
            letras_candidata = ()
            for letra in candidata:
                letras_candidata = letras_candidata + letra
            
            for diva in divas_estadunidenses:
                
                if candidata not in divas_estadunidenses:

                    letras_diva = ()
                    for letra in diva:
                        letras_diva = letras_diva + letra

                    if verificar_permutacao(letras_candidata, letras_diva):
                        candidata = diva
                        penalidade -= 100
                        pais = "EUA"
            
            # Adicionando candidatas no dicionário de candidatas
            if candidata != "Azelia Banks":

                pontuacao_candidata = (int(grammys) * 15) + (int(popularidade) * 10) + (int(shows) * 5) + penalidade + bonus
                candidatas_pontuacao[candidata] = pontuacao_candidata

                candidatas_popularidade[candidata] = popularidade

                print(f"{candidata} acaba de entrar na Batalha das Divas!")

                if pais == "Brasil":
                    print(f"ESSA TEM O TEMPERO BRASILEIRO! Por jogar em casa, {candidata} já larga com 50 pontos de vantagem.")

                elif pais == "EUA" and penalidade == -50:
                    print(f'Por excesso de "estrelas e listras", {candidata} recebe uma penalidade de 50 pontos.')

                elif pais == "EUA" and penalidade == -100:
                    print(f"A CASA CAIU! A produção pegou {candidata} no pulo do gato tentando se livrar da penalidade! Por essa tentativa de malandragem, o preço veio dobrado.")

            else:
                print(f"Eita, climão! Parece que o histórico de polêmicas de {candidata} falou mais alto. A produção barrou a entrada e aqui no Brasil ela não canta!")

        else:
            print(f"Só pode ter uma {candidata} na arena. Inscrição duplicada negada!")

mostrar_placar(candidatas_pontuacao, candidatas_popularidade)

# FASE 2