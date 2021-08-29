n = int(input())
while n > 0:
    n -= 1
    a = input()
    m = int(len(a)/2) - 1
    dec = a[m::-1] + a[len(a) - 1:m:-1]
    print(dec)