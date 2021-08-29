n = int(input())
cartas = [4, 5, 6, 7, 12, 11, 13, 1, 2, 3]
pa = 0; pb = 0
for i in range(n):
    linha = input().split()
    vet = [0] * 6
    for j in range(6):
        vet[j] = int(linha[j])
    ca = 0; cb = 0
    for j in range(3):
        ia = 0; ib = 0
        for t in range(10):
            if cartas[t] == vet[j]:
                ia = t
            if cartas[t] == vet[j + 3]:
                ib = t
        if ia >= ib:
            ca += 1
        else:
            cb += 1
            if ca == 2 or cb == 2:
                break
    if ca > cb:
        pa += 1
    else:
        pb += 1
print(pa, pb)