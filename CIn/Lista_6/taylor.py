vida_amorosa = {
    "2010": {"Jake Gyllenhaal": ("All too Well", "We are never ever getting back together", "Red")},
    "2008": {"Joe Jonas": ("Forever & Always", "Holy Ground")},
    "2009": {"Taylor Lautner": ("Back to December", "I can see you", "Midnight rain")},
    "2016": {"Tom Hiddleston": ("Getaway Car")},
    "2020": {"Joe Alwyn": ("Paper Rings", "Lover", "So Long London")},
    "2012": {"Harry Styles": ("Style", "Out of the Woods", "All You Had to Do Was Stay")},
    "2023": {"Travis Kelce": ("The Fate of Ophelia", "The Alchemy", "Wi$h Li$t")},
}

acontecimentos_carreira = {
    "Fearless": ("Ganhou o VMA 2009, porém Kanye West interrompeu seu discurso de vitória. Também ganhou o Grammy de Álbum do Ano (2010), sendo a artista mais jovem da história (na época) a receber esse prêmio."),
    "Speak Now": ("Teve uma turnê mundial massiva que consolidou seu status de superestrela global, o albúm Speak Now vendeu mais de 1 milhão de cópias na primeira semana, superando qualquer outro álbum dos últimos dois anos"),
    "1989": ('“1989” tornou-se o primeiro álbum de Taylor exclusivamente pop; a artista emplacou dois hits mundiais: Blank Space e Bad Blood. Fun Fact: Taylor nasceu em 13 de dezembro de 1989.'),
    "Reputation": ("O álbum foi uma resposta à mídia, às traições públicas e ao controle da narrativa sobre sua imagem. Além disso, em 2019, Taylor tem os direitos autorais de seus álbuns roubados."),
    "The Eras Tour": ("The Eras Tour é uma turnê comemorativa, com detalhes que buscam fazer jus á tudo que Taylor Swift fez e alcançou em seus anos de carreira. No Brasil, aconteceram seis apresentações em novembro de 2023 em São Paulo e no Rio de Janeiro.")
}

entrada = ""
eras_roubadas = []

while entrada != "Já chega de fatos sobre a Taylor, vai fazer a lista de IP":
    entrada = input()

    if entrada != "Já chega de fatos sobre a Taylor, vai fazer a lista de IP":

        if entrada == "Qual a situação de relacionamento?":

            pessoa = input()
            ano = input()

            pessoa_namorado = vida_amorosa[ano].keys()
            if pessoa in pessoa_namorado:
                status = "estão namorando"
            else:
                status = "não estão namorando"
            
            print(f"{pessoa} e Taylor Swift {status} em {ano}")

        elif entrada == "Qual pessoa está relacionada essa música?":
            
            musica = input()

            for ano, detalhes_ano in vida_amorosa.items():

                for parceiro, musicas in detalhes_ano.items():

                    if musica in musicas:
                        pessoa = parceiro

            print(f"A pessoa relacionada é {pessoa}, Taylor nunca erra em suas músicas")


        elif entrada == "Quais são todas as músicas relacionadas a essa pessoa?":

            pessoa = input()

            for ano, detalhes_ano in vida_amorosa.items():
                
                if pessoa in detalhes_ano:
                    musicas = detalhes_ano[pessoa]

            saida = f"Cartas de amor ou indiretas, as músicas dedicadas a {pessoa} são: "

            for musica in musicas:
                saida += f"{musica}, "
            
            saida = saida.strip(", ")
            print(saida)

        elif entrada == "O que aconteceu nessa era?":

            era = input()

            print(acontecimentos_carreira[era])

        elif entrada == "Wayne nunca deixará Taylor vencer! O CIn precisa manter o hate na diva pop, eu vou alterar as informações":

            era = input()

            frase_alterada = acontecimentos_carreira[era] + "Que grande mentira! Taylor Swift só mente"
            acontecimentos_carreira[era] = frase_alterada

            print("Cuidado, há um impostor no guia... Informações comprometidas")

        elif entrada == "Scooter não liga que ela comprou todos os álbuns de volta, ele vai roubar tudo dessa era":

            era = input()
            eras_roubadas.append(era)

            acontecimentos_carreira.pop(era, "")
            print(f"Para onde foi a história sobre {era}? Parece que alguém roubou tudo e não avisou a Taylor")

if len(eras_roubadas) > 0:
    
    print("Big Machine Records roubou:")
    for era in eras_roubadas:
        print(era)
