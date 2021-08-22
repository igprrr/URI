n = int(input())
for i in range(0, n):
    num = int(input())
    x = 0
    y = 1
    while y <= num:
        if num % y == 0:
            x = x + 1
        y = y + 1
    if x > 2:
        print(num,'nao eh primo')
    else:
        print(num,'eh primo')