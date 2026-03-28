def sumavidsotkiv(kapital, vidsotki):
    return kapital + (kapital * vidsotki / 100) 

kapital = float(input('Уведи капітал -> '))
vidsotki = float(input('Уведи відсотки -> '))
print(f'Сума після нарахування відсотків: {sumavidsotkiv(kapital, vidsotki):.2f} євро') 