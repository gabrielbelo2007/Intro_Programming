print("Sejam bem-vindos à Big Sub Brasil, onde a fama é temporária, os barracos são eternos, e só um vai conquistar o título de maior subcelebridade do país!")

p1, p2 = input().split(", ")

numeros_participantes = []

# Receber números dos dois primeiros participantes
numeros_participantes.append(input().split(" "))
numeros_participantes.append(input().split(" "))

for participante in range(len(numeros_participantes)):
    
    num_participante = numeros_participantes[participante]

    # Ordenar os números
    for verificados in range(len(num_participante)):

        for numero in range(0, len(num_participante) - verificados - 1):
            if int(num_participante[numero]) < int(num_participante[numero + 1]):
                num_participante[numero], num_participante[numero + 1] = int(num_participante[numero + 1]), int(num_participante[numero])


matriz_p1 = [numeros_participantes[0][2::-1], numeros_participantes[0][-1:-4:-1]]
matriz_p2 = [numeros_participantes[1][2::-1], numeros_participantes[1][-1:-4:-1]]

desempate_p1 = 0
desempate_p2 = 0

# Adicionar a última linha da matriz
for participante in range(len(numeros_participantes)):
    
    linha_3 = []

    num_participante = numeros_participantes[participante]

    for numero in range(6, 2, -1):

        if len(linha_3) < 3:
            linha_3.append(num_participante[numero] + 1)
        
        else:
            numero_sobrou = num_participante[numero]

    if participante == 0:
        matriz_p1.append(linha_3)
        desempate_p1 = numero_sobrou
    
    else:
        matriz_p2.append(linha_3)
        desempate_p2 = numero_sobrou


# Calcular o determinante participante 1

principal_p1 = (matriz_p1[0][0] * matriz_p1[1][1] * matriz_p1[2][2]) + \
    (matriz_p1[0][1] * matriz_p1[1][2] * matriz_p1[2][0]) + \
    (matriz_p1[0][2] * matriz_p1[1][0] * matriz_p1[2][1])

secundaria_p1 = (matriz_p1[0][2] * matriz_p1[1][1] * matriz_p1[2][0]) + \
    (matriz_p1[0][0] * matriz_p1[1][2] * matriz_p1[2][1]) + \
    (matriz_p1[0][1] * matriz_p1[1][0] * matriz_p1[2][2])

determinante_p1 = principal_p1 - secundaria_p1

# Calcular o determinante participante 2

principal_p2 = (matriz_p2[0][0] * matriz_p2[1][1] * matriz_p2[2][2]) + \
    (matriz_p2[0][1] * matriz_p2[1][2] * matriz_p2[2][0]) + \
    (matriz_p2[0][2] * matriz_p2[1][0] * matriz_p2[2][1])

secundaria_p2 = (matriz_p2[0][2] * matriz_p2[1][1] * matriz_p2[2][0]) + \
    (matriz_p2[0][0] * matriz_p2[1][2] * matriz_p2[2][1]) + \
    (matriz_p2[0][1] * matriz_p2[1][0] * matriz_p2[2][2])

determinante_p2 = principal_p2 - secundaria_p2

print(f"{p1.capitalize()} e {p2.capitalize()} disputarão entre si.")

for jogada in range(2):

    if jogada == 0:
        matriz = matriz_p1 
        participante = p1 
        pontos = determinante_p1

    else:
        matriz = matriz_p2 
        participante = p2
        pontos = determinante_p2

    for linha_matriz in matriz:
            linha_como_str = [str(numero) for numero in linha_matriz]
            print(" ".join(linha_como_str))
            
    print(f"{participante.capitalize()} está com pontuação {pontos} pontos.")

nome_ganhador = ""

if determinante_p1 == determinante_p2:
    print("RODADA DESEMPATE!!")

    if desempate_p1 != desempate_p2:
        nome_ganhador = p1 if desempate_p1 > desempate_p2 else p2
        nome_perdedor = p2 if nome_ganhador == p1 else p1

        print(f"Contra todas as expectativas (inclusive as nossas), {nome_ganhador.capitalize()} venceu a rodada!")
        print(f"Seu momento de brilhar virou eclipse {nome_perdedor.capitalize()}. Melhor sorte no próximo flop!")
    
    else:
        print("Como isso é possível?? Os participantes empataram até na rodada desempate! EU DESISTO!!!")

if determinante_p1 != determinante_p2 or desempate_p1 != desempate_p2:
    
    ganhador = p1 if determinante_p1 >= determinante_p2 and desempate_p1 > desempate_p2 else p2
    print(f"Com talento duvidoso e esforço máximo, a vitória é de {ganhador.capitalize()}!")