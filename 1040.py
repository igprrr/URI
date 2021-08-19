notas = input().split()
N1 = float(notas[0])
N2 = float(notas[1])
N3 = float(notas[2])
N4 = float(notas[3])
exame = 0.0
media = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / 10
print('Media: %.1f'%media)
if(media >= 7.0):
    print('Aluno aprovado.')
if(media < 5.0):
    print('Aluno reprovado.')
if(media >= 5.0 and media <= 6.9):
    print('Aluno em exame.')
    exame = float(input())
    print('Nota do exame: %.1f'%exame)
    media = (media + exame) / 2
    if(media >= 5.0):
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: %.1f'%media)