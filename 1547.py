x = int(input())
def ganhador():
    qtd, n = map(int, input().split())
    lista = list(map(int, input().split()))
    diferenca = abs(n - lista[0])
    sorteado = 0
    for i in range(1, qtd):
        if abs(n - lista[i]) < diferenca:
            diferenca = abs(n - lista[i])
            sorteado = i
    print(sorteado + 1)
for i in range(0, x):
    ganhador()