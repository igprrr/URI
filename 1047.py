tempos = input().split()
hri = int(tempos[0])
min = int(tempos[1])
hrf = int(tempos[2])
minf = int(tempos[3])
if hri < hrf:
    h = hrf - hri
    if min < minf:
        m = minf - min
    if min > minf:
        h = h - 1
        m = (60 - min) + minf
    if min == minf:
        m = 0
if hri > hrf:
    h = (24 - hri) + hrf
    if min < minf:
        m = minf - min
    if min > minf:
        h = h - 1
        m = (60 - min) + minf
    if min == minf:
        m = 0
if hri == hrf:
    if min < minf:
        m = minf - min
        h = 0
    if min > minf:
        m = (60 - min) + minf
        h = 23
    if min == minf:
        h = 24
        m = 0
print('O JOGO DUROU %.0f'%h,'HORA(S) E %.0f'%m,'MINUTO(S)')