altura = int(input())
espacos_brancos = altura
blocos = 1

for nivel in range(altura):
    for espacos in range(espacos_brancos):
        print("⠀", end="")
    for bloco in range(blocos):
        print("#", end="")
    blocos += 2
    espacos_brancos -= 1
    print()