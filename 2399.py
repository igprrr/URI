n = int(input())
lista = []
for i in range(n):
    lista.append(int(input()))
for m in range(n):
    if m == 0:
        y = 0
    z = lista[m]
    if m == n - 1:
        w = 0
    else:
        w = lista[m + 1]
    print(w + z + y)
    y = z