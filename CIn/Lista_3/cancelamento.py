print("--- Simulador de Cancelamento ---")

qtd_artistas = int(input())

artistas_seguidores = []
for artista in range(qtd_artistas):
    nome_seguidores = input()
    nomes = nome_seguidores.split("-")
    
    artistas_seguidores.append(nomes)

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
        artistas_seguidores[perfil][1] = int(artistas_seguidores[perfil][1]) * 0.85

    else:
        print("Nenhum evento relevante. Seguidores continuam os mesmos.")

print(f"\n--- RANKING FINAL DE SEGUIDORES ---")

trocou = True
artistas_ordenados = []
adicionados = 0

while trocou and adicionados < 3:
    trocou = False
    menor_valor = 0

    for perfil in range(qtd_artistas):
        if (artistas_seguidores[perfil][1] > artistas_seguidores[menor_valor][1] or artistas_seguidores[perfil][1] == artistas_seguidores[menor_valor][1]) and perfil not in artistas_ordenados:
            menor_valor = perfil
            trocou = True

    if trocou:
        artistas_ordenados.append(menor_valor)
        adicionados += 1

for posicao, perfil in zip(range(3), artistas_ordenados):
    print(f"{posicao + 1}º Lugar: {artistas_seguidores[perfil][0]} com {artistas_seguidores[perfil][1]} seguidores.")
