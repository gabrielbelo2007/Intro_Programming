# Fatalis
vida_fatalis = [1800]

def golpes_fatalis(acao, lista_cacadores, lista_status):
    
    if acao == "Mar de Chamas Negras":

        for status in range(len(lista_status)):

            if lista_status[status] == "Desprotegido":
                lista_cacadores[status] = 0
    
    else:

        dano = 55 if acao == "Ataque com Cauda" else 65

        for cacador in range(len(lista_cacadores)):

            if lista_cacadores[cacador] - dano >= 0:
                lista_cacadores[cacador] -= dano

            else:
                lista_cacadores[cacador] = 0

# Armas
def great_sword(acao, fatalis):

    if acao == "Golpe Carregado":
        fatalis[0] -= 165
    
    elif acao == "Corte Largo":
        fatalis[0] -= 120
    
    elif acao == "Divisor de Mundos":
        fatalis[0] -= 200

def fuzi_arco(acao, fatalis):

    if acao == "Tiro Carregado":
        fatalis[0] -= 90
    
    elif acao == "Bala de Penetração":
        fatalis[0] -= 120
    
    elif acao == "Tiro Devastador":
        fatalis[0] -= 150

def glaive_inseto(acao, fatalis, vida_cacador):

    if acao == "Corte Aéreo":
        fatalis[0] -= 100
    
    elif acao == "Descida Carregada":
        fatalis[0] -= 120
    
    elif acao == "Kinseto":

        cor = input()

        if cor == "Vermelho":
            fatalis[0] -= 40
        
        elif cor == "Amarelo":
            fatalis[0] -= 15

        elif cor == "Verde":
            vida_cacador[1] += 40


# 0 - Cacador Great Sword | 1 - Cacador Glaive | 2 - Cacador Fuzi Arco 
vida_cacadores = [200, 200, 200]
status_cacadores = ["Desprotegido", "Desprotegido", "Desprotegido"]

print(f"Hora de Lutar contra a Historia!\n")

for turno in range(4):

    if vida_fatalis[0] > 0 and sum(vida_cacadores) > 0:

        if vida_cacadores[0] > 0:
            acao_cacador_great_sword = input()
            great_sword(acao_cacador_great_sword, vida_fatalis)

        if vida_cacadores[1] > 0:
            acao_caçador_glaive_inseto = input()
            glaive_inseto(acao_caçador_glaive_inseto, vida_fatalis, vida_cacadores)

        if vida_cacadores[2] > 0:
            acao_caçador_fuzi_arco = input()
            fuzi_arco(acao_caçador_fuzi_arco, vida_fatalis)
    
        if vida_fatalis[0] > 0:
            acao_fatalis = input()

            if acao_fatalis == "Mar de Chamas Negras":

                status_cacadores[0] = input()   # Great Sword
                status_cacadores[1] = input()   # Fuzi Arco
                status_cacadores[2] = input()   # Caçador Glaive
            
            golpes_fatalis(acao_fatalis, vida_cacadores, status_cacadores)

if vida_fatalis[0] > 0:
    print("O Fatalis conseguiu sobreviver ao combate...")
    print("O mundo corre perigo!")

else:
    print("Eu não acredito, vocês conseguiram!")
    print("Obrigado caçadores! O mundo está salvo.")