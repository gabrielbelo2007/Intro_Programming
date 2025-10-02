nome1 = input()
nome2 = input()
nome3 = input()

pts_1 = 0
pts_2 = 0
pts_3 = 0

cfch_1 = 0
ctg_1 = 0

cfch_2 = 0
ctg_2 = 0

cfch_3 = 0
ctg_3 = 0

for buscador in range(3): 
    ctg = 0
    cfch = 0
    pts = 0
    
    for local in range(3):
        procurou = 0
        while procurou == 0:
                acao = input()
                if acao == "Fim da busca nesse prédio.":
                    cfch = pts if local == 0 else cfch
                    ctg = pts - cfch if local == 1 else ctg
                    procurou = 1
                else:
                    pts += 1
    
    if buscador == 0:
        cfch_1 = cfch
        ctg_1 = ctg
        pts_1 = pts
    
    elif buscador == 1:
        cfch_2 = cfch
        ctg_2 = ctg
        pts_2 = pts
    
    else:
        cfch_3 = cfch
        ctg_3 = ctg
        pts_3 = pts

print("Vai começar o esconde-esconde UFPE 2025!")

for buscador in range(3):

    if buscador == 0:
        nome = nome1
        cfch = cfch_1
        ctg = ctg_1
        pts = pts_1

    elif buscador == 1:
        nome = nome2
        cfch = cfch_2
        ctg = ctg_2
        pts = pts_2

    elif buscador == 2:
        nome = nome3
        cfch = cfch_3
        ctg = ctg_3
        pts = pts_3

    print(f"\nProntos ou não, lá vai {nome}.")
    for local in range(3):
        if local == 0:
            print(f"Agora {nome} procurará no CFCH.")
            for pontos in range(cfch):
                print(f"{nome} achou uma pessoa!")
                
        elif local == 1:
            print(f"Agora {nome} procurará no CTG.")
            for pontos in range(ctg):
                print(f"{nome} achou uma pessoa!")

        else:
            print(f"Agora {nome} procurará no CIN.")
            for pontos in range(pts - (cfch + ctg)):
                print(f"{nome} achou uma pessoa!")

maior_pontuacao = max(pts_1, pts_2, pts_3)
if maior_pontuacao == 0:
    print("\nNinguém foi encontrado, nenhum dos buscadores ganhou a disputa.")

else:
    nome_ganhador = nome1 if pts_1 == maior_pontuacao else nome2 if pts_2 == maior_pontuacao else nome3
    print(f"\n{nome_ganhador} é o(a) melhor no esconde-esconde da UFPE!")