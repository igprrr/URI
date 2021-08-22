n = int(input())
lista = list(map(int, input().split()))
a = 0
b = 0
x = lista[0]
for v in lista:
    if (v < x):
        x = v
        a = b
    b += 1
print('Menor valor: %d'%x)
print('Posicao: %d'%a)