vez = int(input())
num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
for i in range(vez):
    valor = list(input())
    for j in range(len(valor)):
        if not valor[j] in num:
            valor[j] = ";"
    lista=("".join(valor).split(";"))
    lista2 = []
    for p in lista:
        if not p =="":
            lista2.append(int(p))
    print(sum(lista2))