print(f"Don't sleep, don't eat, just do it on repeat! Keep bumpin' that!!!\n")

atos = {}

musica = ""
ato = 0

limites_duracoes = [10, 8, 12]
duracoes_atos = [0, 0, 0]

while musica != "FIM_SHOW":
    
    if ato == 0:
        generos = "Hyperpop e Pop"

    elif ato == 1:
        generos = "Sentimental e Ballad"

    elif ato == 2:
        generos = "Hyperpop e Banger"

    print(f"Iniciando montagem do Ato {ato} ({generos}):\n")

    musicas_adicionadas = []
    while musica != f"FIM_ATO_{ato}":
        musica = input()

        if musica != f"FIM_ATO_{ato}":
            nome, genero, duracao = musica.split(", ")

            print(f"Música em análise: {nome}")

            if nome == "Actually Romantic":

                print("Já não basta ter exposto a Charli nessa música, agora a Taylor quer que a própria cante? GOLPE BAIXÍSSIMO!!!")

            else:

                if genero in generos:

                    if duracoes_atos[ato] + duracao <= limites_duracoes[ato]:
                        duracoes_atos[ato] += duracao
                        musicas_adicionadas.append()

                        print("{nome_musica} adicionada ao Ato {numero_do_ato} ;).")

                    else:
                        segundos = duracoes_atos[ato] * 60
                        print(f"Muito longa! O Ato {ato} já está com {segundos} segundos e essa música tem {segundos} segundos.")
                
                else:
                    print("Gênero errado para esse ato! Cuidado, uma música deslocada mata a vibe de um show…")

        print()

    ato += 1