print("Ativando a máquina...")

inventor = input()
ano = int(input())

confiavel = True if ano % len(inventor) == 0 else False

if(confiavel == False):
    if(inventor == "Frink"):
        print("Nem precisava colocar os dados! O rebigulador jamais existiria em qualquer universo!")
    else:
        print(f"Previsão instável! {inventor.capitalize()} também deve achar que o rebigulador é ridículo...")
else:
    if(inventor == "Frink"):
        print("Professor Frink irá inventar o rebigulador?! A máquina deve estar com defeito! Glavin!")
    else:
        print(F"Previsão confiável! O rebigulador será real em {ano}!")