pontos = input().split()
x = float(pontos[0])
y = float(pontos[1])
if x == 0:
    if y == 0:
        print('Origem')
    if y != 0:
        print('Eixo Y')
if y == 0:
    if x != 0:
        print('Eixo X')
if x > 0:
    if y > 0:
        print('Q1')
    if y < 0:
        print('Q4')
if x < 0:
    if y > 0:
        print('Q2')
    if y < 0:
        print('Q3')