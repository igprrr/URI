l = int(input())
t = input()
mat = []
for i in range(12):
    mat.append([])
for i in range(12):
    for j in range(12):
        x = float(input())
        mat[i].append(x)
if t == "S":
    result = 0
    for k in range(12):
        result = result + mat[k][l]
    print(result)
if t == "M":
    result2 = 0
    result = 0
    for k in range(12):
        result = result + mat[k][l]
    result2 = result / 12
    print('%.1f'%result2)