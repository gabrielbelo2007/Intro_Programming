print("RECEBA! É hoje que eu me torno o melhor dos melhores.")

numero_sessoes = int(input())
habilidade_inicial = int(input())

if habilidade_inicial <= 5:
    print("A gente tem que começar de algum lugar, né? RECEBA!")

elif habilidade_inicial <= 15:
    print("Não tem jeito, vou ser o melhor do mundo!")
    
else:
    print("O Pai tá estourado! RECEBA!")

meta = (100 - habilidade_inicial) / numero_sessoes
print(f"Meta por Partida: {meta}")

treinos_e_goleiros = input()

treinos = treinos_e_goleiros.split("-")
goleiros_especiais = ["Rokenedy", "IShowSpeed", "Sérgio Soares", "Neymar Jr", "Gabriel Vasconcelos"]

habilidade_atual = float(habilidade_inicial)

indice_batida = 0
indice_goleiro = 1
sessoes_jogadas = 0

while habilidade_atual <= 100 and sessoes_jogadas < numero_sessoes:
    tipo_batida = treinos[indice_batida] 
    goleiro = treinos[indice_goleiro]

    print(f"TIPO DE PARTIDA: {tipo_batida}")
    print(f"Nome do Goleiro: {goleiro}")

    goleiro_especial = True
    if goleiro not in goleiros_especiais:
        habilidade_goleiro = int(input())
        goleiro_especial = False  
    
    campo = input()
    campo_matriz = eval(campo)

    x = int(input())
    y = int(input())

    gol = False
    if campo_matriz[x][y] == 1:
        gol = True

    if goleiro_especial and gol:
        if goleiro == "Rokenedy":
            print("Aí não dá, impossível de fazer gol no maior do mundo.")
            gol = False

        elif goleiro == "IShowSpeed":
            print(f"REBECA? Is that you?\nIspidi mai friand, recieve!")
            habilidade_atual += meta * 1.5 if gol else 0

        elif goleiro == "Sérgio Soares":
            print("DALE DALE, PROFESSOR! Quero ver se esse tal de Python é bom mesmo…")
            
            if gol and tipo_batida == "Batida de Pênalti":
                habilidade_atual += meta
                
            else:
                gol = False
        
        elif goleiro == "Neymar Jr":
            print("Ele nem sabe agarrar! A arma dele é a sua fragilidade…")
            habilidade_atual += meta * 0.5 if gol else 0

        elif goleiro == "Gabriel Vasconcelos":
            print("HAHAHA! Eu pedi um desafio, não uma barra sem goleiro…")
            habilidade_atual += meta * 2.0 if gol else 0

    else:
        if gol and habilidade_atual > habilidade_goleiro:
            habilidade_atual += (habilidade_atual - habilidade_goleiro) 

    if gol:
        print("RECEBA! GOLAÇO! É O MELHOR DO MUNDO!")
    else:
        print("A jornada ainda não acabou!")

    if habilidade_atual > 100:
        print("NÃO TEM JEITO! EU SEMPRE SOUBE QUE IA SER O MELHOR DO MUNDO! RECEBA!")

    else:
        sessoes_jogadas += 1

        if habilidade_inicial + meta <= habilidade_atual:
            print(f"VAMO! PARTIDA {sessoes_jogadas} DE {numero_sessoes}!")

        else:
            print("Dá pra recuperar depois! Vamo seguindo!")

        habilidade_inicial = habilidade_atual
        indice_batida += 2
        indice_goleiro += 2
        
         
if habilidade_atual == 100:
    print("O trono do futebol hoje tem dois reis. Eu e Pelé! Não podia estar com alguém melhor!")

elif habilidade_atual < 100:
    print("Ano que vem tem InterCIn de novo! É só eu treinar mais…")