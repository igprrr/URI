valor = float(input())
if (0 < valor <=2000):
    print ("Isento")
elif (2000 < valor <=3000):
    total = (valor - 2000)
    taxa = (total * 8) / 100
    print ("R$ %.2f"% taxa)
elif (3000 < valor <= 4500):
    total = (valor - 2000)
    total1 = total - 1000
    taxa1 = (1000 * 8) / 100
    taxa2 = (total1*18)/100
    print ("R$ %.2f"% (taxa1 + taxa2))
else:
    total = (valor - 2000)
    total1 = total - 1000
    taxa1 = (1000 * 8) / 100
    total2 = total1 - 1500
    taxa2 = (1500 * 18) / 100
    taxa = (total2 * 28) / 100
    print ("R$ %.2f" % (taxa + taxa1 + taxa2))