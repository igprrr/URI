valor = input().split()
c = int(valor[0])
q = int(valor[1])
preco = 0.0
if c == 1:
    preco = 4.0 * q
elif c == 2:
    preco = 4.5 * q
elif c == 3:
    preco = 5.0 * q
elif c == 4:
    preco = 2.0 * q
elif c == 5:
    preco = 1.5 * q
print('Total: R$ %.2f'%preco)