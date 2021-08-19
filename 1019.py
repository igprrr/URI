n = int(input())
horas = n // 3600
restante = n % 3600
minutos = restante // 60
segundos = restante % 60
print(str(horas)+':'+str(minutos)+':'+str(segundos))