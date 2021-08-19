valor = input().split()
a = float(valor[0])
b = float(valor[1])
c = float(valor[2])
pi = 3.14159
tr = c * a / 2
print('TRIANGULO: %.3f'%tr)
ac = pi * c**2
print('CIRCULO: %.3f'%ac)
at = (a + b) * c / 2
print('TRAPEZIO: %.3f'%at)
aq = b**2
print('QUADRADO: %.3f'%aq)
ar = a * b
print('RETANGULO: %.3f'%ar)