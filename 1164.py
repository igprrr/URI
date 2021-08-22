n = int(input())
for i in range(0, n):
    num = int(input())
    x = 1
    y = 0
    while x < num:
        if num % x == 0:
            y = y + x
        x = x + 1
    if y == num:
        print(num,'eh perfeito')
    else:
        print(num,'nao eh perfeito')