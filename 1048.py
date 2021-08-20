sal = float(input())
if 0 < sal <= 400:
    rea = (((sal * 15) / 100) + sal)
    perc = 15
    print("Novo salario: %.2f" %rea)
    print("Reajuste ganho: %.2f" %(rea - sal))
    print("Em percentual: " + str(perc) + " %")
elif 400 < sal <= 800:
    rea = (((sal * 12) / 100) + sal)
    perc = 12
    print("Novo salario: %.2f" %rea)
    print("Reajuste ganho: %.2f" %(rea - sal))
    print("Em percentual: " + str(perc) + " %")
elif 800 < sal <= 1200:
    rea = (((sal * 10) / 100) + sal)
    perc = 10
    print("Novo salario: %.2f" %rea)
    print("Reajuste ganho: %.2f" %(rea - sal))
    print("Em percentual: " + str(perc) + " %")
elif 1200 < sal <= 2000:
    rea = (((sal * 7) / 100) + sal)
    perc = 7
    print("Novo salario: %.2f" %rea)
    print("Reajuste ganho: %.2f" %(rea - sal))
    print("Em percentual: " + str(perc) + " %")
else:
    rea = (((sal * 4) / 100) + sal)
    perc = 4
    print("Novo salario: %.2f" %rea)
    print("Reajuste ganho: %.2f" %(rea - sal))
    print("Em percentual: " + str(perc) + " %")