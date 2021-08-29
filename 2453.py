p = input()
msg = ''
for palavra in p.split():
    for letra in range(1, len(palavra), 2):
        msg += palavra[letra]
    msg += ' '
print(msg[:-1])