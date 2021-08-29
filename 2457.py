letra = input()
palavra = input().split()
total = 0.0
for i in palavra:
    if letra in i:
        total += 1
total /= len(palavra)/100
print('%.1f' % total)