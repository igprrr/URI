valores = input().split()
a = int(valores[0])
b = int(valores[1])
if a > b:
    if a % b == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
if a < b:
    if b % a == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
if a == b:
    print('Sao Multiplos')