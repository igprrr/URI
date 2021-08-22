n = 0
med = 0
while n < 2:
    nota = float(input())
    if nota >= 0 and nota <= 10:
        n = n + 1
        med = med + nota
    if nota < 0 or nota > 10:
        print('nota invalida')
med = med / 2
print('media =',med)