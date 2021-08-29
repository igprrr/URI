while(True):
    try:
        sentence = input()
        nova_sentence = ""
        contador = 0
        for i in sentence:
            if i != " " and contador % 2 == 0:
                nova_sentence += i.upper()
                contador += 1
            elif i != " " and contador % 2 == 1:
                nova_sentence += i.lower()
                contador += 1
            elif i == " ":
                nova_sentence += " "
        print(nova_sentence)
    except:
        break