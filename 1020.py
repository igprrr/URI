dias = int(input())
anos = dias // 365
restante = dias % 365
meses = restante // 30
qdias = restante % 30
print(anos,'ano(s)')
print(meses,'mes(es)')
print(qdias,'dia(s)')