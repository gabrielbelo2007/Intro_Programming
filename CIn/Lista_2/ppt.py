qtd_doces = int(input())

Jogador1 = input()
Jogador2 = input()
rodadas = qtd_doces // 10

rodadas += 1 if qtd_doces % 10 != 0 else 0

if "Arthur" in (Jogador1 + Jogador2):
    print("A batalha vai começar!")

    for rodada in range(rodadas):
        vida1 = 10
        vida2 = 10

        if qtd_doces % 10 != 0 and rodada == 0:
            print(f"Pra aquecer, essa primeira vale menos, só {qtd_doces % 10} doces!")
        else:
            print(f"Batalha número {rodada + 1}!")

        while vida1 > 0 and vida2 > 0:
            jogada1 = input()
            jogada2 = input()
                
            jogadas = jogada1 + jogada2

            if jogada1 == jogada2:
                print("Eita, jogaram a mesma coisa dessa vez.")
                
            else:
                if "papel" in jogadas and "tesoura" in jogadas:
                    if jogada1 == "papel":
                        vida1 = max(0, vida1 - 3)
                        vida2 += 1 
                    else:
                        vida2 = max(0, vida2 - 3)
                        vida1 += 1

                elif "pedra" in jogadas and "papel" in jogadas:
                    if jogada1 == "pedra":
                        vida1 = max(0, vida1 - 2)
                        vida2 += 2 
                    else:
                        vida2 = max(0, vida2 - 2)
                        vida1 += 2 

                else:
                    if jogada1 == "pedra":
                        vida2 = max(0, vida2 - 4)
                    else:
                        vida1 = max(0, vida1 - 4)

                print(f"Esse turno terminou com {Jogador1} tendo {vida1} de vida e {Jogador2} tendo {vida2}!")

        ganhador_rodada = Jogador1 if vida1 > 0 else Jogador2
        print(f"A rodada {rodada + 1} vai para {ganhador_rodada}, que garante seus doces!")

else:
    print("Epa!!! E cadê o dono dos doces??")