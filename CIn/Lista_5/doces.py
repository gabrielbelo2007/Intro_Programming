doces = int(input())

def particoes(doces_restantes, particao_atual=doces):

    # Caso base
    if doces_restantes == 0:
        return 1
    
    # Chegou na menor partição
    if particao_atual == 0:
        return 0
    
    combinacoes = 0
    
    while doces_restantes >= 0:
        
        combinacoes += particoes(doces_restantes, (particao_atual - 1))
        doces_restantes = doces_restantes - particao_atual

    return combinacoes

print("DOCES OU TRAVESSURAS???")

num_particoes = particoes(doces)

print(f"sem travessuras por hoje! tenho {num_particoes} sacolinhas pra vocês")

if num_particoes % 2 == 0:
    print("doces equilibrados, sem travessuras!")

else:
    print("hmm... número ímpar de sacolinhas 🍭 cuidado com as bruxas!")