n = int(input())
m = int(input())
album = []
for i in range(m):
    faltam = int(input())
    if faltam not in album:
        album.append(faltam)
print(n - len(album))