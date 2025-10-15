numero_desfilantes = int(input())
patrocinador_evento = input()

if patrocinador_evento == "Tha Beauty":
    associada = "Thais Linares"

elif patrocinador_evento == "DeGuê?":
    associada = "Davi Brito"

else:
    associada = "Edu e Fih"

entrada_permitida = ["Adrieli Queiroz", "Arthur Jorge", "César Cavalcanti", "Elisson Oliveira", "Filipe Moreira", "Gabriela Alves", "Joab Henrique", "Maria Fernanda", "Miriam Gonzaga", "Sofia Remindes"]

entraram = []
for desfilante in range(numero_desfilantes):
    desfilante = input()
    entraram.append(desfilante)

print(f"Senhoras e senhores, o desfile de gala do CIn vai começar!")

invasoes = 0
acrescimo_contagem = 1
for contagem, pessoa in zip(range(len(entraram)), entraram):

    if pessoa in entrada_permitida:
        print(f"Desfilante de n° {contagem + acrescimo_contagem}: {pessoa}!")

    elif pessoa == associada:
        print("Invasão tolerada por motivos de patrocínio!")
        print(f"Desfilante de n° {contagem + acrescimo_contagem}: {pessoa}!")

    else:
        print(f"{pessoa} invadiu a passarela! Segurem ele(a), produção!")

        invasoes += 1
        substituiu = False
    
        for monitor in entrada_permitida:
            if monitor not in entraram and not substituiu:
                print(f"Desfilante de n° {contagem + acrescimo_contagem}: {monitor}!")
                entraram.append(monitor)
                substituiu = True
        
        if not substituiu:
            print(f"Desfilante de n° {contagem + acrescimo_contagem}: {pessoa}?! Pelo visto não havia como substituir...")

        if invasoes == 3:
            print(f"Muitas invasões estão deixando a galera irritada... Chama o Core pra acalmar os ânimos!")

            acrescimo_contagem = 2
            print(f"Desfilante de n° {contagem + acrescimo_contagem}: Core!")

if "Gretchen" in entraram or "Tulla Luana" in entraram or "Inês Brasil" in entraram:
    print("Nas arquibancadas do CIn, sussurros indignados agitam a multidão...")
                
    for intrusa in entraram:
        if intrusa == "Gretchen":
            print('"Eles tem que respeitar os meus 37 anos de carreira! Eu hoje sou um ícone, se eu morrer hoje eu vou continuar sendo a Gretchen!"')
        
        elif intrusa == "Tulla Luana":
            print('"Ninguém ser humano está acima de mim! Mas eu estou acima de muitos... é assim que eu penso."')

        elif intrusa == "Inês Brasil":
            print('"É aquele ditado... Vamo fazer o quê?"')
        