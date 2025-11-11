valores_notas = [100, 50, 20, 10, 5]
notas_usadas = [0, 0, 0, 0, 0]

def calcular_combinacoes(valor_inicial, indice_nota, contagem_atual):

    # Caso base = combinação encontrada
    if valor_inicial == 0:

        # Adicionar notas usadas da combinação encontrada, ao total de notas usadas
        for posicao_valor in range(len(contagem_atual)):
            notas_usadas[posicao_valor] += contagem_atual[posicao_valor]

        return 1  # Vai somar ao total de combinações encontradas
    

    # Encerra a recursão quando tenta acessar um indice maior que 4
    if indice_nota == len(valores_notas):
        return 0
    

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
        
        # Vai aumentando a cada combinação encontrada
        total_combinacoes += calcular_combinacoes(valor_restante, indice_nota + 1, nova_contagem)
        

        """
        Enquanto o caso base não for atingido, vai aumentando a quantidade de notas usadas, inicialmente a maior quantidade de notas 5, depois uma
        nota 10 e o resto 5, e assim em diante...
        """
        qtd_nota_usada += 1
    
    # Executado ao fim das recursões
    return total_combinacoes

print(calcular_combinacoes(60, 0, notas_usadas))
print(notas_usadas)