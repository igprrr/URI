a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
vp = 0
for n in [a, b, c, d, e]:
    if n % 2 == 0:
        vp += 1
print(vp,'valores pares')