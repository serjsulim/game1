umsatz = [None, 100, 200, None, None, 300, None, 400, None, 200]
for oborot in range(len(umsatz)):
    if umsatz[oborot] == None:
        umsatz[oborot] = (umsatz[(oborot - 1) % len(umsatz)] + umsatz[(oborot + 1) % len(umsatz)])/2
print(umsatz)
