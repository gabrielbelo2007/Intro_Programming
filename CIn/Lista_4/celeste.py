def ataques_badeline(ataque):
    
    if ataque == "Você não tem o que é necessário para escalar.":
        return 20
    
    return 50

def reacoes_madeline(reacao):
    
    if reacao == "Calma Badeline, nós vamos conseguir.":
        return 25
    
    elif reacao == "Eu sei que somos capazes! Vamos em frente!":
        num_respiracoes = int(input())
        return 10 * num_respiracoes
    
    return 60

vida_madeline = 100

while 150 > vida_madeline > 0:
    
    # 1) Ataque
    ataque_badeline = input()
    resultado_ataque = ataques_badeline(ataque_badeline)

    if resultado_ataque == 20:
        print("Eu nunca vou conseguir chegar ao topo :(")

    else:
        print("NAAÃO EU NUNCA DEVERIA TER INVENTADO DE ESCALAR ESSA MONTANHA!")
    
    vida_madeline -= resultado_ataque

    # 2) Reação

    if vida_madeline > 0:
        reacao_madeline = input()
        vida_madeline += reacoes_madeline(reacao_madeline)

if vida_madeline >= 150:
    print("Madeline chegou ao topo! Ela se senta em um banco para descansar e apreciar a vista.")

else:
    print("Madeline e Badeline não conseguiram se entender... parece que elas nunca vão ver a cidade de cima.")