while True:
    n = int(input())
    if(n == 0):
        break
    v = input().split()
    for i in range(n):
        v[i] = int(v[i])
    res = sorted(v)
    for m, i in enumerate(v):
        if i == res[n - 2]:
            print(m + 1)
            break