print("RECEBA! É hoje que eu me torno o melhor dos melhores.")

numero_sessoes = int(input())
habilidade_inicial = int(input())

if habilidade_inicial <= 5:
    print("A gente tem que começar de algum lugar, né? RECEBA")

elif habilidade_inicial <= 15:
    print("Não tem jeito, vou ser o melhor do mundo!")
    
else:
    print("O Pai tá estourado! RECEBA!")

meta = (100 - habilidade_inicial) / numero_sessoes
print(f"Meta por Partida: {meta}")

treinos_e_goleiros = input()

treinos = treinos_e_goleiros.split("-")
goleiros_especiais = ["Rokenedy", "IShowSpeed", "Sérgio Soares", "Neymar Jr", "Gabriel Vasconcelos"]

sessoes_ativas = True

while habilidade_inicial <= 100 and sessoes_ativas:
    for batida, goleiro, sessao in zip(range(0, len(treinos), 2), range(1, len(treinos), 2), range(numero_sessoes)):
        tipo_batida = treinos[batida] 
        goleiro = treinos[goleiro]

        goleiro_especial = True

        print(f"TIPO DE PARTIDA: {tipo_batida}")
        print(f"Nome do Goleiro: {goleiro}")

        if goleiro not in goleiros_especiais:
            habilidade_goleiro = int(input())
            goleiro_especial = False  
        
        campo = input()
        campo_matriz = eval(campo)

        x = int(input())
        y = int(input())

        if goleiro_especial:
            if goleiro == "Rokenedy":
                print("Aí não dá, impossível de fazer gol no maior do mundo.")
                print("A jornada ainda não acabou!")
                print("Dá pra recuperar depois! Vamo seguindo!")

            elif goleiro == "IShowSpeed":
                print(f"REBECA? Is that you?\nIspidi mai friand, recieve!")

                if campo_matriz[x][y] != 0:
                    habilidade_inicial += meta * 1.5
                    print("RECEBA! GOLAÇO! É O MELHOR DO MUNDO!")

                    if habilidade_inicial <= 100:
                        print(f"VAMO! PARTIDA {sessao + 1} DE {numero_sessoes}!")

                else:
                    print("A jornada ainda não acabou!")
                    print("Dá pra recuperar depois! Vamo seguindo!")

            elif goleiro == "Sérgio Soares":
                print("DALE DALE, PROFESSOR! Quero ver se esse tal de Python é bom mesmo…")

                if campo_matriz[x][y] != 0 and tipo_batida == "Batida de Pênalti":
                    habilidade_inicial += meta
                    print("RECEBA! GOLAÇO! É O MELHOR DO MUNDO!")

                    if habilidade_inicial <= 100:
                        print(f"VAMO! PARTIDA {sessao + 1} DE {numero_sessoes}!")

                else:
                    print("A jornada ainda não acabou!")
                    print("Dá pra recuperar depois! Vamo seguindo!")
            
            elif goleiro == "Neymar Jr":
                print("Ele nem sabe agarrar! A arma dele é a sua fragilidade…")

                if campo_matriz[x][y] != 0:
                    habilidade_inicial += meta // 2
                    print("RECEBA! GOLAÇO! É O MELHOR DO MUNDO!")

                else:
                    print("A jornada ainda não acabou!")
                    print("Dá pra recuperar depois! Vamo seguindo!")

            elif goleiro == "Gabriel Vasconcelos":
                print("HAHAHA! Eu pedi um desafio, não uma barra sem goleiro…")

                if campo_matriz[x][y] != 0:
                    habilidade_inicial += meta * 2
                    print("RECEBA! GOLAÇO! É O MELHOR DO MUNDO!")

                    if habilidade_inicial <= 100:
                        print(f"VAMO! PARTIDA {sessao + 1} DE {numero_sessoes}!")

                else:
                    print("A jornada ainda não acabou!")
                    print("Dá pra recuperar depois! Vamo seguindo!")

        else:
            if campo_matriz[x][y] != 0:
                print("RECEBA! GOLAÇO! É O MELHOR DO MUNDO!")

                if habilidade_inicial > habilidade_goleiro:
                    habilidade_inicial += (habilidade_inicial - habilidade_goleiro)

                if (habilidade_inicial - habilidade_goleiro) > meta:
                    print(f"VAMO! PARTIDA {sessao + 1} DE {numero_sessoes}!")
                
                else:
                    print("Dá pra recuperar depois! Vamo seguindo!")

            else:
                print("A jornada ainda não acabou!")
                print("Dá pra recuperar depois! Vamo seguindo!")

    sessoes_ativas = False

if habilidade_inicial > 100:
    print("NÃO TEM JEITO! EU SEMPRE SOUBE QUE IA SER O MELHOR DO MUNDO! RECEBA!")            

elif habilidade_inicial == 100:
    print("O trono do futebol hoje tem dois reis. Eu e Pelé! Não podia estar com alguém melhor!")

else:
    print("Ano que vem tem InterCIn de novo! É só eu treinar mais…")