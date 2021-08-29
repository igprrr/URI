n = int(input())
for i in range(n):
    text = input().split()
    t1, t2 = text
    t = ''
    if(len(t1) <= len(t2)):
        for i in range(len(t1)):
            t += t1[i]
            t += t2[i]
        t += t2[len(t1):]
    else:
        for i in range(len(t2)):
            t += t1[i]
            t += t2[i]
        t += t1[len(t2):]
    print(t)