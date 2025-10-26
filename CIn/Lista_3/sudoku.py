board = []
tamanho_board = 9

for linha in range(tamanho_board):
    linha = input().split(" ")
    board.append(linha)

posicoes_vazias = []

for linha in range(tamanho_board):

    for coluna in range(tamanho_board):
        if board[linha][coluna] == ".":
            posicoes_vazias.append([linha, coluna])


total_conjuntos = len(posicoes_vazias)
conjunto_atual = 0

while 0 <= conjunto_atual < total_conjuntos:

    # Define a linha e a coluna que está vazia, ou que já tem um valor, em caso de ter dado erro e o algoritmo retroceder
    linha, coluna = posicoes_vazias[conjunto_atual][0], posicoes_vazias[conjunto_atual][1]

    tentativa_numero = 1 if board[linha][coluna] == "." else int(board[linha][coluna]) + 1
    
    numero_valido = False
    while tentativa_numero <= tamanho_board and not numero_valido:

        numero_valido = True

        # Verificando numeros na linha
        for valor in board[linha]:
            
            if valor != ".":
                if int(valor) == tentativa_numero:
                    numero_valido = False


        # Verificando numeros na coluna
        if numero_valido: 

            for posicao in range(tamanho_board):
                if board[posicao][coluna] != ".":

                    if int(board[posicao][coluna]) == tentativa_numero:
                        numero_valido = False
        

        # Verificar quadrados
        if numero_valido:
            
            quadrado_l = linha - linha % 3
            quadrado_c= coluna - coluna % 3

            for linha_quadrado in range(3):
                for coluna_quadrado in range(3):

                    posicao_quadrado = board[linha_quadrado + quadrado_l][coluna_quadrado + quadrado_c]
                    
                    if posicao_quadrado != ".":
                        if int(posicao_quadrado) == tentativa_numero:
                            numero_valido = False

        tentativa_numero += 1 if not numero_valido else 0

    if numero_valido:
        board[linha][coluna] = tentativa_numero
        conjunto_atual += 1
    
    else:
        board[linha][coluna] = "."
        conjunto_atual -= 1

print("Caso encerrado! Mizael provou sua inocência lógica e o Sudoku foi resolvido!")
for linha in range(tamanho_board):
        linha_formatada = []

        for coluna in range(tamanho_board):
            linha_formatada.append(str(board[linha][coluna]))

        print(" ".join(linha_formatada))