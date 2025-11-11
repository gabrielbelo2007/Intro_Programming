valores_notas = [100, 50, 20, 10, 5]
notas_usadas = [0, 0, 0, 0, 0]

def calcular_combinacoes(valor_inicial, indice_nota=0, contagem_atual=notas_usadas):

    # Caso base = combinação encontrada
    if valor_inicial == 0:

        # Adicionar notas usadas da combinação encontrada, ao total de notas usadas
        for posicao_valor in range(len(contagem_atual)):
            notas_usadas[posicao_valor] += contagem_atual[posicao_valor]

        return 1  # Vai somar ao total de combinações encontradas
    

    # Encerra a recursão quando tenta acessar um indice maior que 4
    if indice_nota == len(valores_notas):
        return 0
    
    # Essas linhas definem a nota e o total de combinações para cada chamada da função, então a cada chamada recursiva, essas duas váriaveis só são definidas uma única vez
    nota_atual = valores_notas[indice_nota]
    total_combinacoes = 0
    

    # Representa quantas vezes a nota_atual vai ser usada até que o valor chegue a 0, antes de passar para o próximo índice (número maior)
    qtd_nota_usada = 0
    while valor_inicial - (qtd_nota_usada * nota_atual) >= 0: # Checa o valor restante
        
        # Calcula o resultado após a nota ser usada
        valor_restante = valor_inicial - (qtd_nota_usada * nota_atual)
        
        # Cria uma cópia da contagem e atualiza
        nova_contagem = list(contagem_atual)
        nova_contagem[indice_nota] += qtd_nota_usada
        
        """
        Chamada recursiva: a nota atual começa com 100, e então chama novamente a função e vai descendo 50, 20, 10 até o 5, quando chega no 5 tenta entrar novamente e para no segundo if, a partir dai que a função realmente começa a contar 
        """
        # Vai aumentando a cada combinação encontrada
        total_combinacoes += calcular_combinacoes(valor_restante, indice_nota + 1, nova_contagem)
        

        """
        Enquanto o caso base não for atingido, vai aumentando a quantidade de notas usadas, inicialmente a maior quantidade de notas 5, depois uma nota 10 e o resto 5, e assim em diante...
        """
        qtd_nota_usada += 1
    
    # Executado ao fim das recursões
    return total_combinacoes

troco = int(input())

print(f"Calculando possibilidades para o valor: {troco}")

combinacoes = 0
if troco % 5 == 0:
    combinacoes = calcular_combinacoes(troco)

    if combinacoes == 1:
        print(f"\nEssa foi fácil! Só existe 1 possibilidade de pagar essa conta.")

else:
    print(f"\nInfelizmente, não há como pagar essa conta com as notas disponíveis.")

print(f"\nTotal de possibilidades: {combinacoes}")

print(f"\nUso das notas:")
print(f"R$100: usada em {notas_usadas[0]} combinações")
print(f"R$50: usada em {notas_usadas[1]} combinações")
print(f"R$20: usada em {notas_usadas[2]} combinações")
print(f"R$10: usada em {notas_usadas[3]} combinações")
print(f"R$5: usada em {notas_usadas[4]} combinações")