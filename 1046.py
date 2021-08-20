tempos = input().split()
hri = int(tempos[0])
hrf = int(tempos[1])
if hri < hrf:
    tempo = hrf - hri
else:
    tempo = (24 - hri) + hrf
print('O JOGO DUROU %.0f'%tempo,'HORA(S)')