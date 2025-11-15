horario = input()
minutos_restantes = 60 - int(horario[3:])

minutos_print = horario[3:] if int(horario[3:]) >= 10 else horario[4:]
print(f"O relógio marca 23 horas e {minutos_print} minuto(s)! Byte tem apenas {minutos_restantes} minuto(s) para escapar!")

tam = int(input())

def caminho_livre(linha, coluna):

    if [linha, coluna] in aboboras:
        return "abóbora"
    
    if (linha == tam or coluna == tam) or (linha < 0 or coluna < 0):
        return "bloqueado"
    
    return "livre"

# Lista de memória do menor caminho para os pontos do labirinto
tempo_caminhos = [[minutos_restantes + 1 for coluna in range(tam)] for linha in range(tam)]

menor_caminho = [minutos_restantes + 1]

def calcular_caminho(byte, ult_movimento=-1, minutos=0):
    
    # Caso base
    if byte == saida:

        if minutos < menor_caminho[0]:
            menor_caminho[0] = minutos
        return  1
    
    if minutos >= menor_caminho[0]:
        return 0
    
    if minutos == minutos_restantes:
        return 0

    # Os 4 movimentos possíveis são todas as direções
    for movimento in range(4):

        mudanca_x = 0
        mudanca_y = 0

        # Para cima
        if movimento == 0 and ult_movimento != 1:
            mudanca_x = -1

        # Para baixo
        elif movimento == 1 and ult_movimento != 0:
            mudanca_x = 1
        
        # Para direita
        elif movimento == 2 and ult_movimento != 3:
            mudanca_y = 1
        
        # Para esquerda
        elif movimento == 3 and ult_movimento != 2:
            mudanca_y = -1

        byte[0] += mudanca_x
        byte[1] += mudanca_y

        resultado = caminho_livre(byte[0], byte[1])

        if resultado != "abóbora" and resultado != "bloqueado":

            if minutos + 1 < tempo_caminhos[byte[0]][byte[1]]:
                tempo_caminhos[byte[0]][byte[1]] = minutos + 1
                calcular_caminho(byte, movimento, minutos + 1)

        byte[0] -= mudanca_x
        byte[1] -= mudanca_y
    
    return 0

labirinto = []

# Posições do labirinto
aboboras = []
saida = []
byte = []

for linhas in range(tam):
    linha = list(input())

    for coluna in range(tam):

        if linha[coluna] == "A":
            aboboras.append([linhas, coluna])
        
        elif linha[coluna] == "B":
            byte += linhas, coluna
        
        elif linha[coluna] == "S":
            saida += linhas, coluna

    labirinto.append(linha)

# Definindo posição inicial = 0 para evitar ciclos
tempo_caminhos[byte[0]][byte[1]] = 0

calcular_caminho(byte)

# Não escapou (menor caminho não foi alterado)
if menor_caminho[0] == minutos_restantes + 1:
    print("NÃÃÃÃO! Tudo isso por causa de um docinho! Você estará para sempre conosco, Byte!")

else:

    print(f"CONSEGUIMOS!! Byte precisou de {menor_caminho[0]} minuto(s) para conseguir escapar!")

    if menor_caminho[0] < (minutos_restantes - 10):
        print(f"Abóboras CInistras que nada! Byte mostrou quem é que manda e conseguiu sair faltando {minutos_restantes - menor_caminho[0]} minutos para elas acordarem")

    else:
        print("Ufa! Essa foi por pouco! Mas com ajuda dos alunos de IP essas abóboras nem pareciam tão sinistras assim.")