alunos = int(input())
notas = input().split(' ')
v = [0] * 101
for i in range(alunos):
    v[int(notas[i])] += 1
maior = -1
posicao = 0
for i in range(101):
    if v[i] >= maior:
        maior = v[i]
        posicao = i
print(posicao)