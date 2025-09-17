print("Ted se iludiu de novo. Esse é o momento que ele mais precisa dos amigos dele…")
print("Quantos dos amigos dele conseguirão ajudar dessa vez?")

quantidade_pessoas = int(input())
if(quantidade_pessoas > 0):
    print("Hora da lista dos amigos da vez!")
    
    if(quantidade_pessoas == 1):
        pessoa1 = input()

        if(pessoa1 == "Barney"):
            print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
        elif(pessoa1 == "Robin"):
            print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
        elif(pessoa1 == "Marshall"):
            print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
        elif(pessoa1 == "Lily"):
            print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
        else:
            print(f"{pessoa1} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")

        pessoas = pessoa1
        texto_consolo = f"- Ted foi consolado por: {pessoa1}."
        frase_qtd_pessoas = "- Saideira de um pra um. Nada melhor do que uma pessoa pra ouvir seus problemas."

    elif(quantidade_pessoas == 2):
        pessoa1 = input()

        if(pessoa1 == "Barney"):
            print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
        elif(pessoa1 == "Robin"):
            print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
        elif(pessoa1 == "Marshall"):
            print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
        elif(pessoa1 == "Lily"):
            print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
        else:
            print(f"{pessoa1} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    
        pessoa2 = input()

        if(pessoa2 == "Barney"):
            print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
        elif(pessoa2 == "Robin"):
            print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
        elif(pessoa2 == "Marshall"):
            print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
        elif(pessoa2 == "Lily"):
            print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
        else:
            print(f"{pessoa2} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")

        pessoas = pessoa1 + pessoa2
        texto_consolo = f"- Ted foi consolado por: {pessoa1} e {pessoa2}."
        frase_qtd_pessoas = "- Duas pessoas se compadeceram com a situação do pobre Ted."

    elif(quantidade_pessoas == 3):
        pessoa1 = input()

        if(pessoa1 == "Barney"):
            print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
        elif(pessoa1 == "Robin"):
            print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
        elif(pessoa1 == "Marshall"):
            print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
        elif(pessoa1 == "Lily"):
            print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
        else:
            print(f"{pessoa1} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")

        pessoa2 = input()
    
        if(pessoa2 == "Barney"):
            print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
        elif(pessoa2 == "Robin"):
            print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
        elif(pessoa2 == "Marshall"):
            print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
        elif(pessoa2 == "Lily"):
            print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
        else:
            print(f"{pessoa2} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")

        pessoa3 = input()

        if(pessoa3 == "Barney"):
            print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
        elif(pessoa3 == "Robin"):
            print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
        elif(pessoa3 == "Marshall"):
            print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
        elif(pessoa3 == "Lily"):
            print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
        else:
            print(f"{pessoa3} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")

        pessoas = pessoa1 + pessoa2 + pessoa3
        texto_consolo = f"- Ted foi consolado por: {pessoa1}, {pessoa2} e {pessoa3}."
        frase_qtd_pessoas = "- Três pessoas! Ted conseguiu se divertir bastante."

    elif(quantidade_pessoas == 4):
        pessoa1 = input()

        if(pessoa1 == "Barney"):
            print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
        elif(pessoa1 == "Robin"):
            print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
        elif(pessoa1 == "Marshall"):
            print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
        elif(pessoa1 == "Lily"):
            print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
        else:
            print(f"{pessoa1} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")

        pessoa2 = input()

        if(pessoa2 == "Barney"):
            print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
        elif(pessoa2 == "Robin"):
            print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
        elif(pessoa2 == "Marshall"):
            print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
        elif(pessoa2 == "Lily"):
            print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
        else:
            print(f"{pessoa2} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")

        pessoa3 = input()

        if(pessoa3 == "Barney"):
            print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
        elif(pessoa3 == "Robin"):
            print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
        elif(pessoa3 == "Marshall"):
            print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
        elif(pessoa3 == "Lily"):
            print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
        else:
            print(f"{pessoa3} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")

        pessoa4 = input()

        if(pessoa4 == "Barney"):
            print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
        elif(pessoa4 == "Robin"):
            print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
        elif(pessoa4 == "Marshall"):
            print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
        elif(pessoa4 == "Lily"):
            print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
        else:
            print(f"{pessoa4} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")

        pessoas = pessoa1 + pessoa2 + pessoa3 + pessoa4
        texto_consolo = f"- Ted foi consolado por: {pessoa1}, {pessoa2}, {pessoa3} e {pessoa4}."
        frase_qtd_pessoas = "- Saiu um quinteto um pouco diferente do que a gente tá acostumado, mas no fim conseguiram deixar Ted alegre."

lugar = input() if quantidade_pessoas > 0 else "MacLaren’s Pub"
if(lugar == "MacLaren’s Pub"):
    qnt_media_cervejas = int(input())
else:
    qnt_media_cervejas = 0

if(quantidade_pessoas > 0): 
    if("Marshall" in pessoas and "Lily" in pessoas and quantidade_pessoas == 2):
        print("Nada melhor que um casal para dar conselhos de relacionamento.")
    elif("Marshall" in pessoas and "Barney" in pessoas and quantidade_pessoas == 2):
        print("Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele.")
    elif("Marshall" in pessoas and "Barney" in pessoas and "Robin" in pessoas and "Lily" in pessoas):
        print("O quinteto estará reunido nessa jornada! É o momento perfeito pra brincar de “Você conhece o Ted?”.")
        frase_qtd_pessoas = "- O quinteto junto consegue resolver qualquer problema!"

    if("Barney" in pessoas and lugar == "Arena de Laser Tag"):
        print("Com certeza a Arena de Laser Tag foi escolhida por influência de Barney. Se arrume Ted, é hora de botar um terno, tomar um whisky e partir pra diversão.")
    elif("Robin" in pessoas and quantidade_pessoas == 1):
        print("Acho que Ted e Robin vão sair em um date… Tomara que Ted não roube aquela trompa azul da parede de novo.")
    elif("Marshall" in pessoas or "Barney" in pessoas or "Lily" in pessoas or "Robin" in pessoas):
        if(lugar == "MacLaren’s Pub"):
            print("Não tem erro, né? Estar no MacLaren’s é como estar em casa.")
    elif(quantidade_pessoas > 0 and lugar == "MacLaren’s Pub"):
        print("Um lugar habitual, mas com uma galera diferente. Será estranho, mas Ted vai.")

print(f"\nRelatório da situação de Ted:")
quant_total_cervejas = qnt_media_cervejas * (quantidade_pessoas + 1) if quantidade_pessoas > 0 else qnt_media_cervejas

if(quantidade_pessoas == 0):
   print("Ted foi para o MacLaren’s… Olhe em volta, Ted, você está sozinho.")
   print(f"- Quantidade de cervejas bebidas por Ted: {quant_total_cervejas} cervejas.")

else:
    print(texto_consolo)
    print(f"- O local de afogar as mágoas foi: {lugar}.")
    print(frase_qtd_pessoas)

    if(quant_total_cervejas > 0):
        print(f"- Quantidade de cervejas bebidas pelo grupo: {quant_total_cervejas} cervejas.")

    print("Pelo visto todo mundo já sabe como funciona a cabeça dele, né? Depois do rolê Ted conseguiu esfriar a cabeça e já tá pronto pra quebrar mais a cara. Quem será que serão os próximos a consolar o querido Ted Mosby?")