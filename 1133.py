x = int(input())
y = int(input())
n = x
if (x > y):
    x = y
    y = n
while (x < y):
    x += 1
    if (x % 5 == 2 or x % 5 == 3 and x != y):
        print(x)