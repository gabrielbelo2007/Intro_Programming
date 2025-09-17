x_ted = int(input())
y_ted = int(input())

x_guarda = int(input())
y_guarda = int(input())

amigo = input()

distancia = ((x_guarda - x_ted)**2 + (y_guarda - y_ted)**2)**0.5 

if(amigo == "Barney"):
    distancia_final = round(distancia + 10)
    print(f"Pelos meus cálculos a distância final encontrada foi {distancia_final}!")

    if(distancia_final <= 50):
        print("Nossa, eu sou incrível! Vimos o guarda-chuva em 5 minutos. Tão lendário que eu poderia até ter pego ele pra mim! Desafio aceito!")
    else:
        print("Esse não era o caminho para o guarda-chuva, mas com certeza é o caminho para uma noite lendária! Challenge accepted, vista seu terno!")

elif(amigo == "Marshall"):
    distancia_final = round(distancia - 5)
    print(f"Pelos meus cálculos a distância final encontrada foi {distancia_final}!")

    if(distancia_final <= 50):
        print("Obrigado pela ajuda, Marsh! Tão bom saber que a gente pode contar com os amigos pra achar a nossa cara-metade. Encontramos o guarda-chuva!")
    else:
        print("Tudo bem, cara. O destino é paciente. O importante é que estamos juntos nessa. Vamos tentar de novo amanhã.")

elif(amigo == "Lily"):
    distancia_final = round(distancia - 10)
    print(f"Pelos meus cálculos a distância final encontrada foi {distancia_final}!")

    if(distancia_final <= 50):
        print("Ah! Não te falei? Peguei um atalho! Lilypad sabe das coisas. O guarda-chuva está aqui, e nem nos cansamos muito!")
    else:
        print("Isso não faz sentido! Meu atalho deveria ter funcionado! Que saco! Fiquei com fome de tanta caminhada.")

else:
    distancia_final = round(distancia + 5)
    print(f"Pelos meus cálculos a distância final encontrada foi {distancia_final}!")

    if(distancia_final <= 50):
        print("Bem... acho que isso realmente aconteceu. Nem foi tão difícil assim. O guarda-chuva está bem aqui, Ted. Onde está o mistério?")
    else:
        print("Sério, Ted? Um guarda-chuva? O destino é um conceito abstrato.")
