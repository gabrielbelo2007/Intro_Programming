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
    if buscador == 0:
        for local in range(3):
            procurou = 0
            while procurou == 0:
                    acao = input()
                    if acao == "Fim da busca nesse prédio.":
                        cfch_1 = pts_1 if local == 0 else cfch_1
                        ctg_1 = pts_1 - cfch_1 if local == 1 else ctg_1
                        procurou = 1
                    else:
                        pts_1 += 1

    if buscador == 1:
        for local in range(3):
            procurou = 0
            while procurou == 0:
                    acao = input()
                    if acao == "Fim da busca nesse prédio.":
                        cfch_2 = pts_2 if local == 0 else cfch_2
                        ctg_2 = pts_2 - cfch_2 if local == 1 else ctg_2
                        procurou = 1
                    else:
                        pts_2 += 1

    if buscador == 2:
        for local in range(3):
            procurou = 0
            while procurou == 0:
                    acao = input()
                    if acao == "Fim da busca nesse prédio.":
                        cfch_3 = pts_3 if local == 0 else cfch_3
                        ctg_3 = pts_3 - cfch_3 if local == 1 else ctg_3
                        break
                    pts_3 += 1

print("Vai começar o esconde-esconde UFPE 2025!\n")

print(f"Prontos ou não, lá vai {nome1}.")
for local in range(3):
    if local == 0:
        print(f"Agora {nome1} procurará no CFCH.")
        for pontos in range(cfch_1):
            print(f"{nome1} achou uma pessoa!")
            
    elif local == 1:
        print(f"Agora {nome1} procurará no CTG.")
        for pontos in range(ctg_1):
            print(f"{nome1} achou uma pessoa!")

    else:
        print(f"Agora {nome1} procurará no CIN.")
        for pontos in range(pts_1 - (cfch_1 + ctg_1)):
            print(f"{nome1} achou uma pessoa!")

print(f"\nProntos ou não, lá vai {nome2}.")
for local in range(3):
    if local == 0:
        print(f"Agora {nome2} procurará no CFCH.")
        for pontos in range(cfch_2):
            print(f"{nome2} achou uma pessoa!")
            
    elif local == 1:
        print(f"Agora {nome2} procurará no CTG.")
        for pontos in range(ctg_2):
            print(f"{nome2} achou uma pessoa!")

    else:
        print(f"Agora {nome2} procurará no CIN.")
        for pontos in range(pts_2 - (cfch_2 + ctg_2)):
            print(f"{nome2} achou uma pessoa!")

print(f"\nProntos ou não, lá vai {nome3}.")
for local in range(3):
    if local == 0:
        print(f"Agora {nome3} procurará no CFCH.")
        for pontos in range(cfch_3):
            print(f"{nome3} achou uma pessoa!")
            
    elif local == 1:
        print(f"Agora {nome3} procurará no CTG.")
        for pontos in range(ctg_3):
            print(f"{nome3} achou uma pessoa!")

    else:
        print(f"Agora {nome3} procurará no CIN.")
        for pontos in range(pts_3 - (cfch_3 + ctg_3)):
            print(f"{nome3} achou uma pessoa!")

maior_pontuacao = max(pts_1, pts_2, pts_3)
if maior_pontuacao == 0:
    print("\nNinguém foi encontrado, nenhum dos buscadores ganhou a disputa.")

else:
    if pts_1 ==  maior_pontuacao:
        print(f"\n{nome1} é o(a) melhor no esconde-esconde da UFPE!")
    elif pts_2 == maior_pontuacao:
        print(f"\n{nome2} é o(a) melhor no esconde-esconde da UFPE!")
    else:
        print(f"\n{nome3} é o(a) melhor no esconde-esconde da UFPE!")