diai = input().split()
hri = input().split()
diaf = input().split()
hrf = input().split()
di, df = int(diai[1]), int(diaf[1])
hi, mi, si = int(hri[0]), int(hri[2]), int(hri[4])
hf, mf, sf = int(hrf[0]), int(hrf[2]), int(hrf[4])
minuto_seg = 60
hora_seg = minuto_seg * 60
dia_seg = hora_seg * 24
i = si + mi * minuto_seg + hi * hora_seg + di * dia_seg
f = sf + mf * minuto_seg + hf * hora_seg + df * dia_seg
if i < f:
    tempo = f - i
    dias = int(tempo / dia_seg)
    tempo = tempo % dia_seg
    horas = int(tempo / hora_seg)
    tempo = tempo % hora_seg
    minutos = int(tempo / minuto_seg)
    tempo = tempo % minuto_seg
    segundos = tempo
    print(dias,'dia(s)')
    print(horas,'hora(s)')
    print(minutos,'minuto(s)')
    print(segundos,'segundo(s)')
