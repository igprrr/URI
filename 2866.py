a = int(input())
while a > 0:
    a -= 1
    c = input()
    saida = ''.join(s for s in c if s.islower())
    saida = saida[::-1]
    print(saida)