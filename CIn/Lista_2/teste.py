palavra_secreta = "abacate"
acertos = "a"

texto = "Palavra: "
for i, letra in zip(len(palavra_secreta), palavra_secreta):
    if letra not in acertos and i < (len(palavra_secreta) - 1):
        texto += "_ "
    elif letra not in acertos:
        texto += "_"
    elif i < (len(palavra_secreta) - 1):
        texto += letra + " "
    else:
        texto += letra

print(texto)