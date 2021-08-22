N = int(input())
R = []
R = input().split()
Q = 0
for i in range(1, N):
    if(int(R[i - 1]) > int(R[i])):
        Q = i + 1
        break
print(Q)