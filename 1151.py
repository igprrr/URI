n = int(input())
x = 0
y = 1
print(x, end=' ')
print(y, end=' ')
num = 2
while(1):
    z = x + y
    num += 1
    if(num == n):
        print(z)
        break
    else:
        print(z, end=' ')
        x= y
        y =z