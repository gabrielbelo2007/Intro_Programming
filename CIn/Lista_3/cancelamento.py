print(f"--- Simulador de Cancelamento ---\n")

qtd_artistas = int(input())

artistas_seguidores = []
for artista in range(qtd_artistas):
    nome_seguidores = input()
    perfis = nome_seguidores.split("-")
    
    # Uma lista com os perfis (listas de nome e seguidores) dos artistas
    artistas_seguidores.append(perfis)

artistas_evento = []
for artista in range(qtd_artistas):
    evento = int(input())
    artistas_evento.append(evento)

for perfil in range(len(artistas_seguidores)):
    nome = (artistas_seguidores[perfil][0]).strip()
    seguidores = artistas_seguidores[perfil][1]

    print(f"A subcelebridade da vez é: {nome}")
    
    if artistas_evento[perfil] == 1:
        print(f"{nome} perdeu 10% dos seguidores!")
        artistas_seguidores[perfil][1] = round(int(artistas_seguidores[perfil][1]) * 0.9) 
    
    elif artistas_evento[perfil] == 2:
        print(f"{nome} ganhou 5% de seguidores!")
        artistas_seguidores[perfil][1] = round(int(artistas_seguidores[perfil][1]) * 1.05) 
    
    elif artistas_evento[perfil] == 3:
        print(f"{nome} perdeu 15% dos seguidores!")
        artistas_seguidores[perfil][1] = round(int(artistas_seguidores[perfil][1]) * 0.85)

    else:
        # Conversão em int para a ordenação posterior
        artistas_seguidores[perfil][1] = int(artistas_seguidores[perfil][1])
        print("Nenhum evento relevante. Seguidores continuam os mesmos.")

print(f"\n--- RANKING FINAL DE SEGUIDORES ---")

trocou = True
verificados = 0

while trocou and verificados < qtd_artistas - 1:
    trocou = False

    for index_perfil in range(0, qtd_artistas - 1):
        if (artistas_seguidores[index_perfil][1] < artistas_seguidores[index_perfil + 1][1]):
            artistas_seguidores[index_perfil], artistas_seguidores[index_perfil + 1] = artistas_seguidores[index_perfil + 1], artistas_seguidores[index_perfil]
            trocou = True
    
    verificados += 1

for posicao, perfil in zip(range(3), artistas_seguidores):
    print(f"{posicao + 1}º Lugar: {perfil[0].strip()} com {perfil[1]} seguidores.")
