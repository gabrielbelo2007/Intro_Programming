qtd_novas_frases = int(input())

frases = ["Que tiro foi esse?", "Segura a marimba", "Tá com raiva? Morde as costas" , "Bateu de frente é só rajadão"]

for frase in range(qtd_novas_frases):
    nova_frase = input()
    frases.append(nova_frase)

frases_impressas = []
for frase in frases:
    if frase not in frases_impressas:
        print(f'"{frase}": {frases.count(frase)}')
        frases_impressas.append(frase)

frases.sort()
print(frases)