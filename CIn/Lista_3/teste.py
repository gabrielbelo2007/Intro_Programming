qtd_artistas = 3

artistas_seguidores = [["C", 10],["B", 20], ["A", 10]]

trocou = True
verificados = 0

while trocou and verificados < qtd_artistas - 1:
    trocou = False

    for perfil in range(0, qtd_artistas - 1):
        if (artistas_seguidores[perfil][1] < artistas_seguidores[perfil + 1][1]):
            artistas_seguidores[perfil], artistas_seguidores[perfil + 1] = artistas_seguidores[perfil + 1], artistas_seguidores[perfil]
            trocou = True
    
    verificados += 1

print(artistas_seguidores)

