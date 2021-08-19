VENDEDOR = input()
SALARIO = float(input())
VENDAS = float(input())
COMISSAO = 0.15 * VENDAS
SALARIO += COMISSAO
print('TOTAL = R$ %.2f'%SALARIO)