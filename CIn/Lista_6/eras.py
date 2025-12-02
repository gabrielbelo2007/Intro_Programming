eras_divas = {

"Dua Lipa":{

    "Future Nostalgia": ("Future Nostalgia", "Don't Start Now","Cool","Physical","Levitating","Pretty Please","Hallucinate","Love Again","Break My Heart","Good in Bed","Boys Will Be Boys","Fever"),

    "Radical Optimism": ("End of an Era","Houdini","Training Season","These Walls","Whatcha Doing","French Exit","Illusion","Falling Forever","Anything for Love","Maria","Happy for You")
},

"Olivia Rodrigo": {
    
    "SOUR": ("Brutal","Traitor","Drivers License","1 Step Forward, 3 Steps Back","Deja Vu","Good 4 U","Enough For You","Happier","Jealousy, Jealousy","Favorite Crime","Hope Ur Ok"),

    "GUTS": ("All-American Bitch","Bad Idea Right?", "Vampire", "Lacy", "Ballad Of A Homeschooled Girl","Making The Bed", "Logical", "Get Him Back!", "Love Is Embarrassing", "The Grudge", "Pretty Isn't Pretty", "Teenage Dream"),
},

"Katy Perry": {
    
    "Teenage Dream":("Teenage Dream", "Last Friday Night (T.G.I.F.)", "California Gurls", "Firework", "Peacock", "Circle the Drain", "The One That Got Away", "E.T.", "Who Am I Living For?", "Pearl", "Hummingbird Heartbeat", "Not Like the Movies"),

    "Prism": ("Roar", "Legendary Lovers", "Birthday", "Walking on Air",  "Unconditionally",  "Dark Horse",  "This Is How We Do", "International Smile", "Ghost", "Love Me", "This Moment", "Double Rainbow", "By theGrace of God"),
},
}

divas = ("Dua Lipa", "Olivia Rodrigo", "Katy Perry")
eras = ("Future Nostalgia", "Radical Optimism", "SOUR", "GUTS", "Teenage Dream", "Prism")

def musica_valida(diva, era, nome_musica, eras_contagem, musicas_gerais):

    if era not in eras:
        print("Essa Era não esta na disputa, tente novamete!")

    elif diva not in divas:
        print("Diva errada, tente novamente!")

    elif era not in eras_divas[diva]:
        print("Diva errada, tente novamente!")
    
    elif era in eras_divas[diva]:

        eras_contagem[era] = eras_contagem.get(era, 0) + 1

        if nome_musica in eras_divas[diva][era]:
            
            if eras_contagem[era] > 3:
                print("Quantidade maxima de musicas dessa era atingida")
                eras_contagem[era] = eras_contagem.get(era, 0) - 1
            
            elif nome_musica in musicas_gerais[diva]["Músicas"]:
                print("A musica ja foi mencionada")

            else:
                return True

        else:
            print("Essa musica não pertence a essa ERA, tente novamente!")
            eras_contagem[era] = eras_contagem.get(era, 0) - 1

    return False


def ordenar_divas(musicas):
    
    musicas_desordenadas = musicas.copy()
    musicas_ordenadas = {}

    for _ in musicas:

        divas_empatadas_streams = ()

        # Critério Principal (Média de Streams)
        maior_media_streams = 0
        for nome_diva in musicas_desordenadas:

            qtd_musicas = len(musicas_desordenadas[nome_diva]["Músicas"])
            total_streams = musicas_desordenadas[nome_diva]["Streams"]
            media_streams = int(total_streams / qtd_musicas) if qtd_musicas > 0 else 0

            if media_streams >= maior_media_streams:
                divas_empatadas_streams = divas_empatadas_streams + (nome_diva,) if media_streams == maior_media_streams else (nome_diva,)
                maior_media_streams = media_streams

        diva = divas_empatadas_streams[0]
                        
        # 1° Desempate (Quantidade de Músicas)
        if len(divas_empatadas_streams) > 1:

            divas_empatadas_qtd_musicas = ()
            maior_qtd_musicas = 0

            for nome_diva in divas_empatadas_streams:

                qtd_musicas = len(musicas_desordenadas[nome_diva]["Músicas"])

                if qtd_musicas >= maior_qtd_musicas:
                    divas_empatadas_qtd_musicas = divas_empatadas_qtd_musicas + (nome_diva,) if qtd_musicas == maior_qtd_musicas else (nome_diva,)
                    maior_qtd_musicas = qtd_musicas 

            diva = divas_empatadas_qtd_musicas[0]

            # 2° Desempate (Lexicográfico)
            if len(divas_empatadas_qtd_musicas) > 1:
                diva = min(divas_empatadas_qtd_musicas)

        musicas_ordenadas[diva] = {"Músicas": musicas_desordenadas[diva]["Músicas"], "Streams": musicas_desordenadas[diva]["Streams"]}
        del musicas_desordenadas[diva]
    
    return musicas_ordenadas


def mostrar_podio(musicas_ordenadas):
    print("===== Pódio =====")

    posicao = 1
    for diva in musicas_ordenadas:

        if posicao == 1:
            ganhadora = diva
        
        qtd_musicas = len(musicas_ordenadas[diva]["Músicas"])
        total_streams = musicas_ordenadas[diva]["Streams"]
        media_streams = int(total_streams / qtd_musicas) if qtd_musicas > 0 else 0

        print(f"{posicao}° {diva} com {media_streams} Streams por música")

        posicao += 1
    
    if ganhadora == "Katy Perry":
        print("Katy Perry 'ruge'! Os KatyCats provam que 'Teenage Dream' e 'Prism' são eternos!")

    elif ganhadora == "Olivia Rodrigo":
        print("É 'brutal' aqui! Os Livies mostraram a força de 'SOUR' e 'GUTS'.")

    elif ganhadora == "Dua Lipa":
        print("Ela está 'Levitating', se voce não quer me ver ganhando, não aparece, não venha! Dua Lipa e seu 'Future Nostalgia' dominaram o pop.")

    return ganhadora


def encontrar_melhor_musica(melhores_musicas, musicas):
    
    empates_votos = ()

    # Critério Princial (Maior quantidade de votos)
    maior_contagem = 0
    for diva in melhores_musicas:

        for musica in melhores_musicas[diva]:

            contagem = melhores_musicas[diva][musica]

            if contagem == maior_contagem:
                empates_votos += ((diva, musica),)
                
            elif contagem > maior_contagem:
                empates_votos = ((diva, musica),)

                maior_contagem = contagem

    diva_musica = empates_votos[0]

    # 1° Desempate (Média de Streams)
    if len(empates_votos) > 1:

        empates_streams = ()

        maior_media_streams = 0
        for empate in empates_votos:

            nome_diva = empate[0]
            musica = empate[1]

            qtd_musicas = len(musicas[nome_diva]["Músicas"])
            total_streams = musicas[nome_diva]["Streams"]

            media_streams = int(total_streams / qtd_musicas)

            if media_streams >= maior_media_streams:
                empates_streams = empates_streams + ((nome_diva, musica),) if media_streams == maior_media_streams else ((nome_diva, musica),)
                maior_media_streams = media_streams

        diva_musica = empates_streams[0]

        # 2° Desempate (Quantidade de Músicas)
        if len(empates_streams) > 1:

            empates_qtd = ()

            maior_qtd_musicas = 0
    
            for empate in empates_streams:

                nome_diva = empate[0]
                musica = empate[1]

                qtd_musicas = len(musicas[nome_diva]["Músicas"])
                
                if qtd_musicas >= maior_qtd_musicas:
                    empates_qtd = empates_qtd + ((nome_diva, musica),) if qtd_musicas == maior_qtd_musicas else ((nome_diva, musica),)
                    maior_qtd_musicas = qtd_musicas
            
            diva_musica = empates_qtd[0]

            # 3° Desempate (Lexicográfico)
            if len(empates_qtd) > 1:
                diva_musica = min(empates_qtd, key=lambda item: item[0])

    return diva_musica


alfabeto = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
def decifrar(elementos):

    for indice in range(0,4,2):

        descriptografado = ""

        nome_criptografado = elementos[indice].upper()
        chave = elementos[indice + 1]

        for letra in nome_criptografado:
            
            if letra != " ":

                posicao_inicial = alfabeto.index(letra)
                posicao_final = (posicao_inicial - int(chave)) % 26
                
                nova_letra = alfabeto[posicao_final]
                descriptografado += nova_letra

            else:
                descriptografado += " "

        if indice == 0:
            votante = descriptografado
        
        elif indice == 2:
            diva_votada = descriptografado

    if diva_votada != "FIM": 
        return diva_votada.title(), votante.capitalize()
    
    else:
        return diva_votada, votante


def encontrar_fa(fas):

    fas_empatados = ()
    maior_votos = 0

    for fa in fas:
        voto_fa = fas[fa]

        if voto_fa >= maior_votos:
            fas_empatados = fas_empatados + (fa,) if voto_fa == maior_votos else (fa,)
            maior_votos = voto_fa

    return min(fas_empatados)

# Chave -> Divas | Valor_Chave -> Músicas e Streams | Valores finais -> Tupla músicas e Streams total
musicas_divas = {
    "Dua Lipa": {
        "Músicas": (),
        "Streams": 0
    },

    "Katy Perry": {
        "Músicas": (),
        "Streams": 0
    },

    "Olivia Rodrigo": {
        "Músicas": (),
        "Streams": 0
    }
}
eras_contagem = {}

# ------------------  PRIMEIRA FASE
print(f"Vai começar a disputa das DIVAS")

musica_desc = input()
uma_musica_aceita = False


while musica_desc != "FIM":

    musica, cantora, era, streams = musica_desc.split(" - ")

    if musica_valida(cantora, era, musica, eras_contagem, musicas_divas):

        musicas_divas[cantora]["Músicas"] += (musica,)
        musicas_divas[cantora]["Streams"] += int(streams)

        if not uma_musica_aceita:
            uma_musica_aceita = True

    musica_desc = input()

if uma_musica_aceita:

    ## Ordenação e pódio
    musicas_divas = ordenar_divas(musicas_divas)

    diva_ganhadora = mostrar_podio(musicas_divas)

    # ------------------ SEGUNDA FASE
    melhores_musicas = {}

    melhor_musica = input()
    uma_musica_aceita = False

    while melhor_musica != "FIM":

        musica, cantora = melhor_musica.split(" - ")

        if musica in musicas_divas[cantora]["Músicas"]:

            if cantora not in melhores_musicas:
                melhores_musicas[cantora] = {}

            melhores_musicas[cantora][musica] = melhores_musicas[cantora].get(musica, 0) + 1

            if not uma_musica_aceita:
                uma_musica_aceita = True
        
        else:
            print("Essa musica não pertence ao catálogo, tente outra")

        melhor_musica = input()
    
    if uma_musica_aceita: 

        diva_melhor_musica, musica_ganhadora = encontrar_melhor_musica(melhores_musicas, musicas_divas)

        print(f"E a música campeã foi {musica_ganhadora}!")

        ganhou = False

        if musica_ganhadora in musicas_divas[diva_ganhadora]["Músicas"] and diva_melhor_musica == diva_ganhadora:
            ganhou = True
            print(f"Domínio completo! {diva_ganhadora} levou o pódio e a melhor música")


        # ------------------  TERCEIRA FASE
        if not ganhou:
            votos_divas = {}

            print(f"Apesar da {diva_ganhadora} ter vencido no Pódio, a melhor música ficou com {diva_melhor_musica}")
            print(f"Por isso teremos uma segunda chance para {diva_melhor_musica}")
            print(f"A decisão será feita por votação popular, mas aparentemente faltou verba para o Spotify, pois os nomes vieram bagunçados, Quem será a Campeã?")

            diva_votada = ""
            votante = ""

            nenhum_voto = True
            while diva_votada != "FIM" and votante != "FIM":
                
                fa_criptografado, chave_fa, diva_criptografada, chave_diva = input().split(" - ")

                elementos_criptografia = (fa_criptografado, chave_fa, diva_criptografada, chave_diva)

                diva_votada, votante = decifrar(elementos_criptografia)

                if diva_votada == "FIM" and votante == "FIM" and nenhum_voto:
                
                    print("Aparentemente os Streams das duas foram comprados, a vencedora só pode ser a que não comprou nenhum voto")

                    diva_restante = tuple(diva for diva in divas if diva not in (diva_ganhadora, diva_melhor_musica))
                    print(f"Parabéns {diva_restante[0]}, a campeã final!")

                elif diva_votada != "FIM":
                    nenhum_voto = False

                    if diva_votada in musicas_divas:

                        print(f"Voto de {votante} computado para {diva_votada}")

                        if diva_votada not in votos_divas:
                            votos_divas[diva_votada] = {"Total Votos": 0, "Votantes": {}}

                        votos_divas[diva_votada]["Total Votos"] += 1
                        votos_divas[diva_votada]["Votantes"][votante] = votos_divas[diva_votada]["Votantes"].get(votante, 0) + 1
            
            if not nenhum_voto:
                diva_campea = max(votos_divas, key=lambda diva_votada: votos_divas[diva_votada]["Total Votos"])
                votantes_ganhadora = votos_divas[diva_campea]["Votantes"]

                maior_fa = encontrar_fa(votantes_ganhadora)

                print(f"A campeã final é {diva_campea}")
                print(f"E o(A) maior fã da diva {diva_campea} é {maior_fa}")

    else:
        print("Nenhuma música foi mencionada, acho que no fim elas estão sem hype")

else: 
    print("Essa batalha foi 'Houdini', sumiu! Sem músicas, sem disputa.")