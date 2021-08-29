n = int(input())
listas = list(map(int, input().split()))
tamanho = 0
for lista in listas:
    tamanho += lista / 2
soma = 0
for i in range(n):
    soma += listas[i]
    if soma == tamanho:
        print(i + 1)