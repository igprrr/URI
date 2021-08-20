n = int(input())
z = 0
w = 0
for i in range(n):
    x = int(input())
    if(x >= 10 and x <= 20):
        z += 1
    else:
        w += 1
print(z, 'in')
print(w, 'out')