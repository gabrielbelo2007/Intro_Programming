print(f"Don't sleep, don't eat, just do it on repeat! Keep bumpin' that!!!\n")

atos = {}

musica = ""
ato = 0

limites_duracoes = [600, 480, 720]
duracoes_atos = [0, 0, 0]

qtd_musicas_barradas = 0
qtd_musicas = 0

while musica != "FIM_SHOW":
    
    if ato == 0:
        generos = "Hyperpop e Pop"

    elif ato == 1:
        generos = "Sentimental e Ballad"

    elif ato == 2:
        generos = "Hyperpop e Banger"

    print(f"Iniciando montagem do Ato {ato + 1} ({generos}):\n")

    musicas_adicionadas = []
    while musica != f"FIM_ATO_{ato + 1}" and musica != "FIM_SHOW":
        musica = input()

        if musica != f"FIM_ATO_{ato + 1}" and musica != "FIM_SHOW":
            nome, genero, duracao_str = musica.split(", ")

            minutos_str, segundos_str = duracao_str.split(":")
            duracao = (int(minutos_str) * 60) + int(segundos_str)

            print(f"Música em análise: {nome}")

            if nome == "Actually Romantic":

                print("Já não basta ter exposto a Charli nessa música, agora a Taylor quer que a própria cante? GOLPE BAIXÍSSIMO!!!")
                qtd_musicas_barradas += 1

            else:

                if nome == "Talk Talk featuring troye sivan":
                    print("A MAIOR AMIZADE DO POP NO PALCO? Talk to them in your own made-up language!")

                elif nome == "on dutch a. g. cook remix featuring addison rae":
                    print("‘CAUSE THEY’RE JUST LIVING THAT LIFE! Addison Rae, a maior revelação do pop desde Britney Spears, no palco ao lado da sua amiga Charli XCX!")

                elif nome == "Guess featuring billie eilish":
                    print("Hey, Billie, you there?")

                if genero in generos:

                    if duracoes_atos[ato] + duracao <= limites_duracoes[ato]:
                        duracoes_atos[ato] += duracao

                        musicas_adicionadas.append((nome, genero))
                        qtd_musicas += 1

                        print(f"{nome} adicionada ao Ato {ato + 1} ;).")

                    else:
                        segundos = duracoes_atos[ato] * 60
                        print(f"Muito longa! O Ato {ato + 1} já está com {segundos} segundos e essa música tem {segundos} segundos.")
                        qtd_musicas_barradas += 1
                
                else:
                    print("Gênero errado para esse ato! Cuidado, uma música deslocada mata a vibe de um show…")
                    qtd_musicas_barradas += 1

    atos[ato + 1] = musicas_adicionadas
    print()

    ato += 1

# SHOW RAPIDO

uma_vez = True
for index_duracao in range(len(duracoes_atos)):
    if duracoes_atos[index_duracao] < (limites_duracoes[index_duracao] * 0.7) and uma_vez:
        print(f"\nTem certeza que isso é um show? Rápido desse jeito, a Charli XCX deve estar pensando nos doces do backstage…")
        uma_vez = False
    
# SETLIST

def imprimir_musicas(lista_musicas, ato):
    if len(lista_musicas) > 0:
        for nome, estilo in lista_musicas:
            print(f"{nome} ({estilo})")

    else:
        print("Nenhuma música adicionada a este Ato.")

    print(f"Duração total do ato: {duracoes_atos[ato]} segundos.")
    print()


print("--- Ato 1 (Abertura) ---")
imprimir_musicas(atos[1], 0)

print("--- Ato 2 (Sentimental) ---")
imprimir_musicas(atos[2], 1)

print("--- Ato 3 (Encerramento) ---")
imprimir_musicas(atos[3], 2)

print("=== RESUMO DO SHOW (BRAT APPROVED) ===")
print(f"Total de músicas na setlist: {qtd_musicas}")
print(f"Total de músicas barradas: {qtd_musicas_barradas}")