niveis_dificuldades = input()

lista_dificuldades = niveis_dificuldades.split(" ")
lista_dificuldades = [int(nivel) for nivel in lista_dificuldades]

anagrama = []
golden_freddy = False

for numero in niveis_dificuldades:
    if numero in ["1", "9", "8", "7"] and numero not in anagrama:
        anagrama.append(numero)

if len(anagrama) == 4:
    golden_freddy = True

# Verificar Caso Especial
caso_especial = True if golden_freddy and 0 in lista_dificuldades else False

if not caso_especial:
    valido = True
    dificuldades_zeradas = 0

    if len(lista_dificuldades) == 4:

        for dificuldade in lista_dificuldades:
            
            if dificuldade < 0 or dificuldade > 20:
                valido = False

            if dificuldade == 0:
                dificuldades_zeradas += 1
    
    else:
        valido = False


    if dificuldades_zeradas < 4 and valido:
        
        relatorio = []

        # Função Recursiva
        def simulacao(energia=100, hora = 0):
            
            # PE, PD, Luz, Cam
            acoes = [False, False, False, False]

            # Caso Base
            if hora == 6:
                return energia
            
            if energia <= 0:
                return energia
            
            energia -= 1

            # Ataque Bonnie
            if hora == 0 and lista_dificuldades[0] > 0:
                
                # Ligou a luz, defender Bonnie
                energia -= (5 + 3 + (lista_dificuldades[0] * 0.25))
                acoes[2] = True

            elif hora == 1:

                # Fechou porta direita, defender Chica
                if lista_dificuldades[1] > 0:
                    energia -= (7 + 2 + (lista_dificuldades[1] * 0.35))
                    acoes[1] = True

            elif hora == 3 and lista_dificuldades[0] > 0:
                
                # Ligou a luz, defender Bonnie
                energia -= (5 + 3 + (lista_dificuldades[0] * 0.25))
                acoes[2] = True

            elif hora == 4:

                # Se Chica ativa, Foxy não ativo
                if lista_dificuldades[1] > 0 and (lista_dificuldades[3] == 0 or energia <= 50):
                    energia -= (7 + 2 + (lista_dificuldades[1] * 0.35))
                    acoes[1] = True

                # Se Chica ativa, Foxy ativo
                elif lista_dificuldades[1] > 0 and (lista_dificuldades[3] > 0 and energia > 50):

                    # Frustar Chica
                    energia -= (7 + 2 + (lista_dificuldades[1] * 0.35))
                    acoes[1] = True
                    
                    # Frustar Foxy
                    energia -= (7 + 5 + (lista_dificuldades[3] * 0.15))
                    acoes[0] = True

                # Somente Foxy ativo, independente Freddy
                elif lista_dificuldades[3] > 0 and energia > 50:
                    energia -= (7 + 5 + (lista_dificuldades[3] * 0.15))
                    acoes[0] = True

            elif hora == 5:
                
                if golden_freddy:

                    # Frustar ataque Golden Freddy
                    energia -= (9 + 10 + (lista_dificuldades[2] * 1.95))
                    acoes[3] = True

                    # Frustar ataque Freddy
                    energia -= 3 + (lista_dificuldades[2] * 0.35)
                
                # Defender Freddy
                elif lista_dificuldades[2] > 0:
    
                    # Usar câmera
                    energia -= (9 + 3 + (lista_dificuldades[2] * 0.35))
                    acoes[3] = True
                

            # Relatório
            relatorio.append(f"0{hora}:00 AM -> PE: {'SIM' if acoes[0] else 'NÃO'} | PD: {'SIM' if acoes[1] else 'NÃO'} | LZ: {'SIM' if acoes[2] else 'NÃO'} | CAM: {'SIM' if acoes[3] else 'NÃO'}")

            energia = simulacao(energia, hora + 1)
            return energia

        energia_final = simulacao()
        
        if energia_final <= 0:
            print('"Uh, Phone Guy falando. Uh, não tem mais ninguém do outro lado, não é?"')

        else:
            print(f'"Uh, olá? Ei, wow, dia sete, parabéns. E ainda com {energia_final:.2f}% de energia. Eu sabia que você conseguiria."')

            for linha in range(len(relatorio)):
                print(relatorio[linha])

    elif dificuldades_zeradas == 4:
        print('"Uh, olá? Olá? Phone Guy falando. Não tem ninguém aqui..."')
    
    else:
        print('"Uh, Phone Guy aqui. Os animatronics estão um pouco "sapecas" esta noite."')

else:
    print('''"IT'S ME"''')