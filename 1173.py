N = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
V = int(input())
for i in range(len(N)):
    N[i] = V
    V = V * 2
    print('N[%d] = %d'%(i,N[i]))