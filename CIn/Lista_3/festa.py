entrada_inicial = input()

influencers = ["Sofia Santino", "Doarda", "Ciclopin", "Bruna Pinheiro"]
cantores = ["Thiaguinho", "Little Thiago", "Neiff", "O Diferenciado", "Veigh", "Mc Loma"]

if entrada_inicial == "WhatsApp: 0 mensagens.":
    print(f"I hate to tell you this BUT\nBia tava achando que ia fazer um mousse. O mousse virou uma piada, parceira")

    print(f"Como a vida não precisa ser only fechos, a gente vai finalizar minha franja hoje:\nEssa chapinha eu dei literalmente tipo 50 reais nela. Não é a mais potente, não é a mais mais... mas ela é algo. Às vezes a gente só precisa ser algo, não precisa ser tudo.\nE o protetor térmico? Vei, a chapinha sabe que eu tô fazendo de coração, ela nunca queimaria meu cabelo.\nEspera esfriar e você vai barbarizar quando tiver pronto\nÉ isso, tchau meus amores")

else:
    convidados = []
    while entrada_inicial != "CABOSSE! Bora simbora organizar essa festa.":

        convidado = entrada_inicial.split(" ")

        if convidado[0] == "Sofia":
            convidados.append("Sofia Santino")
        
        elif convidado[0] == "Little":
            convidados.append("Little Thiago")

        elif convidado[0] == "Bruna":
            convidados.append("Bruna Pinheiro")

        elif convidado[0] == "O":
            convidados.append("O  Diferenciado")

        elif convidado[0] == "Mc":
            convidados.append("Mc Loma")
            convidados.append("Mirella Santos")
            convidados.append("Mariely Santos")

        else:
            convidados.append(convidado[0])
            
        entrada_inicial = input()
    
    
    influencer_presente = False
    cantor_presente = False
    for convidado in convidados:

        if convidado in influencers:
            influencer_presente = True

        elif convidado in cantores:
            cantor_presente = True

    if cantor_presente and influencer_presente:
        print(f"Cachaçaria na minha casa hoje, 21h.\nTodo mundo lá em casa! Tem que ser uma festa que dure muito, tipo 27 anos e 3 meses!!")

    else:

        if cantor_presente:
            print("<PLANOS PARA FESTA>")
            nome_convidados = ", ".join(convidados)
            print(f"Convidados: {nome_convidados}.")
            print("Tipo de comemoração: Paredão - Show na minha casa!!")

        elif influencer_presente:
            print("<TARDE DE FOFOCAS>")
            nome_convidados = ", ".join(convidados)
            print(f"Convidados: {nome_convidados}.")

            for convidado in convidados:
                pauta = input()
                
                if pauta == "Medo de ficar musculosa demais por causa da academia":
                    print("AMIGA, ouça: tem nem o P do PERIGO de você ficar grandona sem querer. Não se preocupe!")

                elif pauta == "O cara que eu gosto não me quer, mas eu continuo insistindo. Acha que eu consigo algo?":
                    print("Claro que consegue, amiga! Consegue virar uma palhaça, consegue perder a autoestima... Consegue várias coisas :)")

                elif pauta == "Meu chefe só me dá um dia de folga, mas eu precisava de dois":
                    print("Tem que ter pelo menos dois dias de descanso. Se seu chefe tem uma empresa que não pode passar dois dias fechada porque vai quebrar, ele deveria fechar! Isso não é nem uma empresa, é um quiosque!")

                elif pauta == "Pessoas que adoram se fazer de coitadinhas":
                    print("Eu detesto quem gosta de ficar pagando de coitadinho(a). Se for chorar… Na verdade, não chora não, que eu não quero nem ouvir.")

                elif pauta == "Essa história de que homem sofre calado":
                    print("Vocês ficam dizendo que homem sofre, que homem sofre calado… E por que eu ainda estou ouvindo? Por que eu ainda ouço???")

            qtns_concordam = int(input())

            if qtns_concordam == 0:
                print("Apois me interne, me prenda, me jogue fora que eu tô maluca!")

            else:
                print("É isso, eu vejo tanta coisa errada nesse mundo… Mas é como dizem, né?! Life snake, a vida cobra em inglês.")