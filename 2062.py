n = int(input())
m = input().split()
r = []
for i in m:
    if len(i) == 3 and i[0] == 'U' and i[1] == 'R':
        r.append('URI')
    elif len(i) == 3 and i[0] == 'O' and i[1] == 'B':
        r.append('OBI')
    else:
        r.append(i)
for j in range(n - 1):
    print(r[j], end= ' ')
print(r[n -1])
    