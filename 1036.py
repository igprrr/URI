valores = input().split()
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])
delta = b * b - 4 * a * c
if delta < 0 or a == 0:
    print('Impossivel calcular')
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)
    print('R1 = %.5f'%x1)
    print('R2 = %.5f'%x2)