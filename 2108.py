string = 0
while True:
    l = input().split()
    sizes = []
    if l == ['0']:
        break
    for i in l:
        sizes.append(str(len(i)))
        if len(i) >= string:
            string = len(i)
            b = i
    p = '-'.join(sizes)
    print(p)
print()
print('The biggest word: %s' % b) 