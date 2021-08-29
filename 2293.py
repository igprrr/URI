n, m = input().split()
n, m = int(n), int(m)
mat = []
for i in range(n):
    linha = input()
    a = linha.split()
    b = []
    for x in a:
        b.append(int(x))
    mat.append(b)
total = None
for i in range(n):
    soma = 0
    for j in range(m):
        soma += mat[i][j]
    if total == None:
        total = soma
    else:
        total = max(total, soma)
for j in range(m):
    soma = 0
    for i in range(n):
        soma += mat[i][j]
    total = max(total, soma)
print(total)