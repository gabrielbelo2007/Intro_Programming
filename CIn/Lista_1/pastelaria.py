competidor1 = input()
pasteis_comp1 = int(input())

competidor2 = input()
pasteis_comp2 = int(input())

competidor3 = input()
pasteis_comp3 = int(input())

ganhador = 0
qtd_pasteis = 0

if(competidor1 == "Lineu" or competidor2 == "Lineu" or competidor3 == "Lineu"):
    print("Lineu comeu um pastel com gosto estranho e usou sua autoridade na vigilancia sanitaria para acabar com a competição, Beiçola tá desolado!")

else:
    if(pasteis_comp1 > pasteis_comp2 and pasteis_comp1 > pasteis_comp3):
         ganhador = competidor1
         qtd_pasteis = pasteis_comp1

    elif(pasteis_comp2 > pasteis_comp1 and pasteis_comp2 > pasteis_comp1):
         ganhador = competidor2
         qtd_pasteis = pasteis_comp2

    else:
         ganhador = competidor3
         qtd_pasteis = pasteis_comp3

    print(f"A(O) campeã(o) é {ganhador}, com {qtd_pasteis} pastéis consumidos!")

    if(competidor1 == "Floriano" or competidor2 == "Floriano" or competidor3 == "Floriano"):
            if(ganhador != "Floriano"):
                 print(f"Anos comendo pastel e perdeu justo para {ganhador}, lastimável, Sr. Flor!") 

    if(ganhador == "Agostinho"):
        if(qtd_pasteis > 100):
            print("Acho que o Agostinho deve ter escondido alguns pastéis na calça, pilantra!")
        elif(qtd_pasteis > 50):
            print("Agostinho madrugou no taxi e veio cheio de fome para a competição!")
    