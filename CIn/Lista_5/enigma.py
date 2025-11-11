#            0    1    2    3    4    5    6    7    8    9    10   11  12    13   14   15   16   17   18  19   20   21    22   23   24   25
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T' ,'U', 'V' ,'W', 'X', 'Y' ,'Z']

letra_inicial = input()
frase_criptografada = input()

chave_inicial = alfabeto.index(letra_inicial)

def calcular_chave(indice_criptografada, indice_chave):

    chave = (indice_criptografada - indice_chave) % 26
    return chave


indices_original = []
indices_armadilhas = []

def decifrar(frase, chave, indice=0):
    
    # Caso base
    if indice == len(frase):
        return 0

    # Caso letra válida
    if frase[indice] in alfabeto:
        indice_criptografada = alfabeto.index(frase[indice])

        chave = calcular_chave(indice_criptografada, chave)

        indices_original.append(chave)

    # Caso armadilha
    else:
        indices_armadilhas.append(indice)

    # Chamada recursiva
    decifrar(frase, chave, indice + 1)
    
decifrar(frase_criptografada, chave_inicial)


frase_original = ""
for indice in indices_original:
    frase_original += alfabeto[indice]

print("Decifrando mensagem do Trickster...")

if len(indices_armadilhas) == 0:
    print("Nenhuma armadilha encontrada! Até que o Trickster foi bonzinho.")

else:
    print(f"Esse Trickster é um picareta mesmo. Foram encontradas armadilhas nas posições: {', '.join(str(n) for n in indices_armadilhas)}")

print(f"Mensagem revelada: {frase_original}")